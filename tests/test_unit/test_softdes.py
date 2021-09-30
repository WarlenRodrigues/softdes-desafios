import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../src"))
from softdes import lambda_handler

base = os.path.dirname(os.path.abspath(__file__))

event_1 = {
        "ndes": "1",
        "code":"code",
        "args": [[1], [2], [3]],
        "resp": [0, 0, 0],
        "diag": ["a", "b", "c"]
    }


def test_lambda_handler_correct_submission():
    with open(os.path.join(base, "data/desafio1_correct.py"), "r") as desafio1:
        code = desafio1.read()
    
    event_1["code"] = code
    res = lambda_handler(event_1)
    assert len(res) == 0
    assert type(res) == str

def test_lambda_handler_invalid_submission():
    with open(os.path.join(base, "data/desafio1_invalid.py"), "r") as desafio1:
        code = desafio1.read()
    event_1["code"] = code
    res = lambda_handler(event_1)
    assert type(res) == str
    assert res == "Nome da função inválido. Usar 'def desafio1(...)'"

def test_lambda_handler_wrong_submission():
    with open(os.path.join(base, "data/desafio1_wrong.py"), "r") as desafio1:
        code = desafio1.read()
    event_1["code"] = code
    diag = " "
    res = lambda_handler(event_1)
    assert type(res) == str
    assert res == diag.join(event_1["diag"])