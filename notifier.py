from threading import Timer
import os
import sys
# Send a notify to operational system
def show_message(message):
  # por enquanto linux
  if sys.platform == 'linux':
    print("*-- Linux: Verifique se sua distro tem o notify-send instalado. *")
    os.system('notify-send "%s"' % message)
  elif sys.platform == 'darwin': 
    print("*-- macOS : Verifique se o terminal-notifier está instalado (Homebrew) *")
    os.system('terminal-notifier -message "%s" -title "Pomy" -sound default' % message)
  # else:
    # No Windows precisamos de uma abordagem mais alternativa

  # print('notify-send "%s"' % message)

def callback(wait, f, message = ""):
  # inicializo um timer (recebo em minutos)
  t = Timer(wait * 60, f)
  # Se alguem tem algo a dizer, que diga
  if len(message) > 0:
    print(message)
  # executo a thread
  t.start()
  print("Aguardando %d minutos..." % wait)
