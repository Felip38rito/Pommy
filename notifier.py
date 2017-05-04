'''
Notifier interface for pommy
'''
from threading import Timer
import os
import sys

def show_message(message):
  ''' Exibe mensagem para o usuario '''
  if sys.platform == 'linux':
    print("*-- Linux: Verifique se sua distro tem o notify-send instalado. *")
    os.system('notify-send "%s" --icon=gnome-devel' % message)
  elif sys.platform == 'darwin':
    print("*-- macOS : Verifique se o terminal-notifier está instalado (Homebrew) *")
    os.system('terminal-notifier -message "%s" -title "Pomy" -sound default' % message)
  # else:
    # No Windows precisamos de uma abordagem mais alternativa

  # print('notify-send "%s"' % message)

def callback(wait, func, message=""):
  '''inicializo um timer (recebo em minutos)'''
  timer = Timer(wait * 60, func)
  # Se alguem tem algo a dizer, que diga
  if len(message) > 0:
    print(message)
  # executo a thread
  timer.start()
  print("Aguardando %3.1f minutos..." % wait)
