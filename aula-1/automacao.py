from copy import copy
from operator import pos
from pyautogui import *
from pandas import *
from time import sleep
import datetime
import pyperclip

#hotkey('ctrl', 't')

# Abrindo o Navegador pelo iniciar
# press('win')
# write('chrome')
# press('enter')
# sleep(5)
# write('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
# press('enter')
# sleep(5)
# doubleClick(x=363, y=297)
# sleep(5)
# click(x=363, y=296)
# sleep(3)
# click(x=1479, y=200)
# sleep(2)
# click(x=1164, y=556)
# time.sleep(5)

tabela = read_excel(r'C:\Users\wesley.dias.CFC\Downloads\Vendas - Dez.xlsx')
quantidade = tabela['Quantidade'].sum()

faturamento = tabela['Valor Final'].sum()
print(tabela)

# hotkey('ctrl', 't')
# copy('Relatório de Vendas')
# hotkey('ctrl', 'v')
# press('enter')

texto = f""" Prezados, bom dia

O faturamento de ontem foi de R$ {faturamento:,.2f}
A quantidade de produto foi de:  {quantidade:,}

Wesley
"""
pyperclip.copy(texto)
print(texto)
# hotkey('ctrl', 'v')