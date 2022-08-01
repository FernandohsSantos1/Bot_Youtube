import pyautogui as pyg
import pyperclip as pc
import time

#Delay para execução entre ações
pyg.PAUSE=0.5

#Abrir o windows, pesquisar google chrome e abri-lo
pyg.press('win')
pyg.write('google', interval = 0.2)
pyg.press('Enter')

#Abrir a aba desejada (Precisa de delay para o navegador aceitar)
#URL possui ? e o pyg não usa caracteres especiais para isso é necessário
#importar o pyperclip para copiar e colar, assim ele pode copiar e colar
#os caracteres especiais
pc.copy('https://www.youtube.com/watch?v=VGW9PQfcdA8')
pyg.hotkey('ctrl', 'v')
pyg.press('Enter')

#tempo de "descanso" para o site abrir
time.sleep(3)

#Selecionar o campo com mouse baseado na position
pyg.click(x=1500, y=790)

for i in range(0,5,1):
    pyg.write('BORA LIPEIRA')
    pyg.press('Enter')
    time.sleep(5)

print(f'O texto foi enviado {i+1}x\n'
       'Encerrando sistema...'  )