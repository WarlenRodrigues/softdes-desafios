# pylint: disable=bare-except
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

Chrome_Driver = webdriver.Chrome(ChromeDriverManager().install())
Chrome_Driver.implicitly_wait(5)
# Aluno faz login com sucesso
# Aluno entra senha incorreta
# Aluno envia desafio com resposta incorreta
# Aluno envia desafio com resposta correta
base = os.path.dirname(os.path.abspath(__file__))
browser = Chrome_Driver


def test_login_ok():
    browser.get(f'http://manu:manu@127.0.0.1:5000/')
    nav_title_xpath = '//*[@id="navbarsExampleDefault"]/ul/li/a'
    try:
        link_element = browser.find_element_by_xpath(nav_title_xpath)
        if link_element:
            assert True
        else:
            assert False

    except:
        assert False


def test_login_fail():
    try:
        browser.get("http://fail:fail@127.0.0.1:5000/")
        assert False
    except:
        assert True


def test_challenge_correct():
    browser.get(f'http://manu:manu@127.0.0.1:5000/')
    input_xpath = '//*[@id="resposta"]'
    result_xpath = '/html/body/div[2]/div/main/div[2]/table/tbody/tr/td[3]'
    try:
        input_element = browser.find_element_by_xpath(input_xpath)
        input_element.send_keys(os.path.join(base, "data/desafio1_correct.py"))

        send_button_element = browser.find_element_by_xpath(
            '//button[normalize-space()="Enviar"]')
        send_button_element.click()
        result_element = browser.find_element_by_xpath(result_xpath)
        result_text = result_element.get_attribute('innerHTML').strip()
        assert result_text == 'OK!'

    except:
        assert False

def test_challenge_wrong():
    browser.get(f'http://manu:manu@127.0.0.1:5000/')
    input_xpath = '//*[@id="resposta"]'
    result_xpath = '/html/body/div[2]/div/main/div[2]/table/tbody/tr/td[3]'
    try:
        input_element = browser.find_element_by_xpath(input_xpath)
        input_element.send_keys(os.path.join(base, "data/desafio1_wrong.py"))

        send_button_element = browser.find_element_by_xpath(
            '//button[normalize-space()="Enviar"]')
        send_button_element.click()
        result_element = browser.find_element_by_xpath(result_xpath)
        result_text = result_element.get_attribute('innerHTML').strip()
        assert result_text == 'Erro'

    except:
        assert False
