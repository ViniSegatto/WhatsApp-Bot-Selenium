from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://web.whatsapp.com/')
time.sleep(30)

contatos = ['xxxxxxxxxx']
mensagem = "oi, teste bot"

def buscar_Contato(contatos):
    campo_Pesquisa = driver.find_element(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_Pesquisa.click()
    campo_Pesquisa.send_keys(contatos)
    campo_Pesquisa.send_keys(Keys.ENTER)
    time.sleep(4)

def enviar_Mensagem(mensagem):
    campo_Mensagem = driver.find_element(By.XPATH,'//div[contains(@class,"copyable-text selectable-text")]')
    campo_Mensagem.click()
    time.sleep(1)
    campo_Mensagem.send_keys(mensagem)
    campo_Mensagem.send_keys(Keys.ENTER)

for i in contatos:
    buscar_Contato(contatos)
    enviar_Mensagem(mensagem)

# chat-list-search
# selectable-text copyable-text iq0m558w
#copyable-text selectable-text
#selectable-text copyable-text 
