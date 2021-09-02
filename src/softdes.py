# pylint: disable=exec-used
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:00:39 2017

@author: rauli
"""

from datetime import datetime
import sqlite3
import hashlib
import numbers
from flask import Flask, request, render_template
from flask_httpauth import HTTPBasicAuth


DBNAME = './quiz.db'

class InvalidFunction(Exception):
    """Invalid function exception"""
    message = "Função inválida."

def lambda_handler(event):
    """Validate studants exercices"""
    try:
        def not_equals(first, second):
            if isinstance(first, numbers.Number) and isinstance(second, numbers.Number):
                return abs(first - second) > 1e-3
            return first != second

        ndes = int(event['ndes'])
        code = event['code']
        args = event['args']
        resp = event['resp']
        diag = event['diag']
        exec(code, locals())


        test = []
        for index, arg in enumerate(args):
            if not 'desafio{0}'.format(ndes) in locals():
                return "Nome da função inválido. Usar 'def desafio{0}(...)'".format(ndes)
            if not_equals(eval('desafio{0}({1})'.format(ndes, *arg)), resp[index]):
                test.append(diag[index])

        return " ".join(test)
    except InvalidFunction:
        return "Função inválida."

def converte_data(orig):
    """Convert data"""
    return orig[8:10]+'/'+orig[5:7]+'/'+orig[0:4]+' '+orig[11:13]+':'+orig[14:16]+':'+orig[17:]

def get_quizes(user):
    """Get all created quizes from database"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    if user in ("admin", "fabioja"):
        cursor.execute("SELECT id, numb from QUIZ")
    else:
        cursor.execute("SELECT id, numb from QUIZ where release < '{0}'".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    info = [reg for reg in cursor.fetchall()]
    conn.close()
    return info

def get_user_quiz(userid, quizid):
    """Get user quizes from database"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute("SELECT sent,answer,result from USERQUIZ where userid = '{0}' and quizid = {1} order by sent desc".format(userid, quizid))
    info = [reg for reg in cursor.fetchall()]
    conn.close()
    return info

def set_user_quiz(userid, quizid, sent, answer, result):
    """Insert user quiz"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute("insert into USERQUIZ(userid,quizid,sent,answer,result) values (?,?,?,?,?);", (userid, quizid, sent, answer, result))
    conn.commit()
    conn.close()

def get_quiz(_id, user):
    """Get quiz by id"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    if user in ("admin", "fabioja"):
        cursor.execute("SELECT id, release, expire, problem, tests, results, diagnosis, numb from QUIZ where id = {0}".format(_id))
    else:
        cursor.execute("SELECT id, release, expire, problem, tests, results, diagnosis, numb from QUIZ where id = {0} and release < '{1}'".format(_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    info = [reg for reg in cursor.fetchall()]
    conn.close()
    return info

def set_info(pwd, user):
    """Set user info"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE USER set pass = ? where user = ?",(pwd, user))
    conn.commit()
    conn.close()

def get_info(user):
    """Get user info"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute("SELECT pass, type from USER where user = '{0}'".format(user))
    print("SELECT pass, type from USER where user = '{0}'".format(user))
    info = [reg[0] for reg in cursor.fetchall()]
    print(info)
    conn.close()
    if len(info) == 0:
        return None
    return info[0]

auth = HTTPBasicAuth()

app = Flask(__name__, static_url_path='')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?TX'

@app.route('/', methods=['GET', 'POST'])
@auth.login_required
def main():
    """Main function"""
    msg = ''
    page = 1
    challenges=get_quizes(auth.username())
    sent = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if request.method == 'POST' and 'ID' in request.args:
        _id = request.args.get('ID')
        quiz = get_quiz(_id, auth.username())
        if len(quiz) == 0:
            msg = "Boa tentativa, mas não vai dar certo!"
            page = 2
            return render_template('index.html', username=auth.username(),
                    challenges=challenges, p=page, msg=msg)

        quiz = quiz[0]
        if sent > quiz[2]:
            msg = "Sorry... Prazo expirado!"

        files = request.files['code']
        filename = './upload/{0}-{1}.py'.format(auth.username(), sent)
        files.save(filename)
        with open(filename,'r') as temp_file:
            answer = temp_file.read()

        args = {"ndes": _id, "code": answer, "args": eval(quiz[4]),
                "resp": eval(quiz[5]), "diag": eval(quiz[6]) }

        feedback = lambda_handler(args)

        result = 'Erro'
        if len(feedback) == 0:
            feedback = 'Sem erros.'
            result = 'OK!'

        set_user_quiz(auth.username(), _id, sent, feedback, result)


    if request.method == 'GET':
        if 'ID' in request.args:
            _id = request.args.get('ID')
        else:
            _id = 1

    if len(challenges) == 0:
        msg = "Ainda não há desafios! Volte mais tarde."
        page = 2
        return render_template('index.html', username=auth.username(),
                    challenges=challenges, p=page, msg=msg)
    quiz = get_quiz(_id, auth.username())

    if len(quiz) == 0:
        msg = "Oops... Desafio invalido!"
        page = 2
        return render_template('index.html', username=auth.username(),
                    challenges=challenges, p=page, msg=msg)

    answers = get_user_quiz(auth.username(), _id)

    return render_template('index.html', username=auth.username(), 
            challenges=challenges, quiz=quiz[0], e=(sent > quiz[0][2]), 
            answers=answers, p=page, msg=msg, expi = converte_data(quiz[0][2]))

@app.route('/pass', methods=['GET', 'POST'])
@auth.login_required
def change():
    """Change user password"""
    if request.method == 'POST':
        velha = request.form['old']
        nova = request.form['new']
        repet = request.form['again']

        page = 1
        msg = ''
        if nova != repet:
            msg = 'As novas senhas nao batem'
            page = 3
        elif get_info(auth.username()) != hashlib.md5(velha.encode()).hexdigest():
            msg = 'A senha antiga nao confere'
            page = 3
        else:
            set_info(hashlib.md5(nova.encode()).hexdigest(), auth.username())
            msg = 'Senha alterada com sucesso'
            page = 3
    else:
        msg = ''
        page = 3

    return render_template('index.html', username=auth.username(),
                challenges=get_quizes(auth.username()), p=page, msg=msg)


@app.route('/logout')
def logout():
    """Execute logout"""
    return render_template('index.html',p=2, msg="Logout com sucesso"), 401

@auth.get_password
def get_password(username):
    """Get user passwort"""
    return get_info(username)

@auth.hash_password
def hash_pw(password):
    """Return user hashed password"""
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port=80)
