from selenium_config import Chrome_Driver
from time import sleep

# Aluno faz login com sucesso
# Aluno entra senha incorreta
# Aluno envia desafio com resposta incorreta
# Aluno envia desafio com resposta correta

browser = Chrome_Driver
browser.get("http://manu:manu@127.0.0.1:5000/")

# browser.quit()
