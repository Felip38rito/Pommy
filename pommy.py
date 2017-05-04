#!/usr/bin/python3

''' Interface principal do Pommy '''
from arguments import parse_arguments
from notifier import show_message, callback

# recebo a entrada (e processo o help caso pedido)
cli_arguments = parse_arguments()
pomos = []

def init():
  '''Primeira contagem'''
  print("Now! counting...")
  send_work()

def send_work():
  ''' Envia o sinal de trabalho para a desktop'''
  pomos.append(1)
  # Mostro a mensagem para o trabalho
  show_message("Time to work")
  # inicializo o timer para o fim do pomodoro de trabalho
  callback(cli_arguments.t, send_break)

def send_break():
  ''' Envia o sinal de parada para o desktop '''
  if len(pomos) % cli_arguments.p != 0:
    show_message("Time to take a short break")
    callback(cli_arguments.b, send_work)
  else:
    show_message("Time to relax...")
    callback(cli_arguments.lb, send_work)

def main():
  ''' Procedimento inicial executado no carregamento '''
  callback(3/60, init, "Get prepared! ... ")

main()
