from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import urllib
import os


navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com")
#enviar a mensagem

while len(navegador.find_elements(By.ID, 'side')) < 1:  # elemento que diz que que a tela carregou
    time.sleep(1)

time.sleep(2)  # garantia

# Whatsapp ja carregou
tabela = pd.read_excel("Envios.xlsx")
#print(tabela[['nome', 'mensagem', 'arquivo']])

for linha in tabela.index:
    nome = tabela.loc[linha, "nome"]
    mensagem = tabela.loc[linha, "mensagem"]
    arquivo = tabela.loc[linha, "arquivo"]
    telefone = tabela.loc[linha, "telefone"]
    texto = mensagem.replace("fulano", nome)
    texto = urllib.parse.quote(texto)
    print(texto)

    # enviar a mensagem
    link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"

    navegador.get(link)

    # esperar a tela do whatsapp carregar -> espera um elemento que só existe na tela já carregada aparecer
    while len(navegador.find_elements(By.ID, 'side')) < 1:  # -> lista for vazia -> que o elemento não existe ainda
        time.sleep(2)
    time.sleep(2)  # só uma garantia

    # você tem que verificar se o número é inválido
    if len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
        time.sleep(2)
    time.sleep(1)

    # esperar a tela do whatsapp carregar -> espera um elemento que só existe na tela já carregada aparecer
    while len(navegador.find_elements(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[1]/button[2]/div/span')) < 1:  # -> lista for vazia -> que o elemento não existe ainda
        time.sleep(1)
    time.sleep(2)  # só uma garantia


    # enviar a mensagem
    navegador.find_element(By.XPATH,
                           '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()

    if arquivo != "N":
        caminho_completo = os.path.abspath(f"arquivos/{arquivo}")
        navegador.find_element(By.XPATH,
                               '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click()
        navegador.find_element(By.XPATH,
                               '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/input').send_keys(
            caminho_completo)
        time.sleep(2)
        navegador.find_element(By.XPATH,
                               '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()

    time.sleep(5)





#ok funcionado 12/12







