"""Add users from file users.csv to database"""
import sqlite3
import hashlib

def add_user(username, pwd, _type):
    """Add users from file users.csv to database"""
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("""Insert into USER(user,pass,type)
          values("{0}","{1}","{2}");""".format(username, pwd, _type))
    conn.commit()
    conn.close()

with open('users.csv','r') as file:
    lines = file.read().splitlines()

for users in lines:
    (user, _type) = users.split(',')
    print(user)
    print(type)
    add_user(user, hashlib.md5(user.encode()).hexdigest(), _type)
