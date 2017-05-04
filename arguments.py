''' Parseador de argumentos da linha de comando '''
import argparse

parser = argparse.ArgumentParser(description="Pomodoro Interface")
parser.add_argument("-t", help="Tempo de cada pomodoro", type=int, default=40)
parser.add_argument("-b", help="Tempo de cada break curto", type=int, default=5)
parser.add_argument("-lb", help="Tempo de cada break longo", type=int, default=15)
parser.add_argument("-p", help="Quantidade de pomos com timer curto", type=int, default=3)

def parse_arguments():
  ''' Executa o parseamento '''
  args = parser.parse_args()
  print("*** Pommy ***")
  print("* Tempo dos pomodoros %d minutos *" % args.t)
  print("* Break curto %d minutos *" % args.b)
  print("* Break longo %d minutos *" % args.lb)
  return args
