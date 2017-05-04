# from threading import Timer
# from notifier import show_message as s
# import arguments as a
from arguments import parse_arguments
from notifier import show_message, callback

# recebo a entrada (e processo o help caso pedido)
args = parse_arguments()
pomos = []

def init():
  # primeira contagem
  print("Now! counting...")
  send_work()

def send_work():
  pomos.append(1)
  # Mostro a mensagem para o trabalho
  show_message("Time to work")
  # inicializo o timer para o fim do pomodoro de trabalho
  callback(args.t, send_break)

def send_break(): 
  if len(pomos) % args.p != 0:
    show_message("Time to take a short break")
    callback(args.b, send_work)
  else:
    show_message("Time to relax...")
    callback(args.lb, send_work)

def main(opt):
  callback(3/60, init, "Get prepared! ... ")

main(args)
print(args)