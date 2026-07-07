# Passo 1: Entrar no Sistema
import pyautogui
import pandas
def esperar():
    time.sleep(1)

import pyautogui
import time
pyautogui.press("win")
esperar()
pyautogui.write("opera")
esperar()
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
esperar()
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Fazer Login

pyautogui.click(x=747, y=361)
esperar()
pyautogui.write("meuemail@gmail.com")
esperar()
pyautogui.press("tab")
esperar()
pyautogui.write("senha123")
esperar()
pyautogui.press("tab")
esperar()
pyautogui.press("enter")
esperar()

# Passo 3: Importar a base de dados

import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:

    # Passo 4: Cadastrar um produto
    # Passo 5: Repetir o passo 4 até acabar a lista de produtos 

    pyautogui.click(x=727, y=249)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    time.sleep(1)

    obs = str(tabela.loc[linha, "obs"])
    pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    time.sleep(1)
    pyautogui.press('pgup')
    time.sleep(1)
