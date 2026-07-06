# Passo 1: Entrar no Sistema

def esperar():
    time.sleep(0.5)

import pyautogui
import time
pyautogui.press("win")
esperar()
pyautogui.write("opera")
esperar()
pyautogui.press("enter")
time.sleep(5)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
esperar()
pyautogui.press("enter")
esperar()

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
pyautogui.press("tab")

# Passo 3: Importar a base de dados
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos 
