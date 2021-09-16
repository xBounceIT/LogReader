# Sviluppato da Daniel D'Angeli e Ugo Monticone, email: daniel.dangeli@syncsecurity.it

from os import system
def clear():
  system('cls')
  return 0

def syncsec():
  print("\n  $$$$$$\                                    $$$$$$\                                    $$\  $$\              ")
  print("$$  __$$\                                  $$  __$$\                                    \__| $$ |             ")
  print("$$ /  \__$$\   $$\$$$$$$$\  $$$$$$$\       $$ /  \__|$$$$$$\  $$$$$$$\$$\   $$\ $$$$$$\ $$\$$$$$$\  $$\   $$\ ")
  print("\$$$$$$\ $$ |  $$ $$  __$$\$$  _____|      \$$$$$$\ $$  __$$\$$  _____$$ |  $$ $$  __$$\$$ \_$$  _| $$ |  $$ |")
  print(" \____$$\$$ |  $$ $$ |  $$ $$ /             \____$$\$$$$$$$$ $$ /     $$ |  $$ $$ |  \__$$ | $$ |   $$ |  $$ |")
  print("$$\   $$ $$ |  $$ $$ |  $$ $$ |            $$\   $$ $$   ____$$ |     $$ |  $$ $$ |     $$ | $$ |$$\$$ |  $$ |")
  print("\$$$$$$  \$$$$$$$ $$ |  $$ \$$$$$$$\       \$$$$$$  \$$$$$$$ \$$$$$$$ \$$$$$$  $$ |     $$ | \$$$$  \$$$$$$$ |")
  print(" \______/ \____$$ \__|  \__|\_______|       \______/ \_______|\_______|\______/\__|     \__|  \____/ \____$$ |")
  print("         $$\   $$ |                                                                                 $$\   $$ |")
  print("         \$$$$$$  |                                                                                 \$$$$$$  |")
  print("          \______/                                                                                   \______/ \n")
  
  print("\nLogReader v0.5.5\n")
  return 0

# Classe per i colori del testo
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Funziona che elabora la linea per determinare i valori del log
def elabora(l):
  word = ""
  arr = []
  found = 0
  for i in range(len(l)):
    if l[i] == '"':
      found += 1
      continue # rimuove doppio apice da output
    if l[i] == " ":
      if found == 1:
        word += l[i]
        continue
      else:
        arr.append(word)
        word = ""
        found = 0
        continue
    word += l[i]
  arr.append(word)
  return arr

# Funzione che prende la linea come parametro e crea un dizionario dividendo la chiave dal valore
def tabella(lst):
  dic = {}
  for item in lst:
    ss = item.split("=")
    dic[ss[0]] = ss[1]
  return dic

# Funzione che elabora le linee della matrice ed estrapola i valori inseriti in input come condizione
def outputMatrix(campo, riga):
  for valore in riga: 
    frase = ""
    if valore == campo:
      frase = (valore + "=" + riga[valore])
      break
  return frase

# Funziona che chiede in input i log da leggere e parsa i file
def parser():
  logs = []
  while True:
    try:
      nLog = int(input("Quanti log vuoi leggere?: "))
      if nLog == 0:
        clear()
        print(f"{bcolors.WARNING}Non puoi inserire 0 log.{bcolors.ENDC}")
        continue
      clear()
      break
    except ValueError:
      clear()
      print(f"{bcolors.WARNING}Valore inserito non numerico.{bcolors.ENDC}")
      continue

  countLog = 0

  for i in range(0, nLog):
    while True:
      try:   
        print("Inserisci la path del", i + 1, "log: ")
        log = input()
        clear()
        with open(log, "rt") as f:
          print(f"Lettura di{bcolors.OKCYAN}", log, f"{bcolors.ENDC}in corso...")
          f = f.readlines()
          logs.append(f)
          countLog += 1
          break
      except FileNotFoundError:
        clear()
        scelta = input("File non trovato, reinserire? [y/n]: ")
        scelta = scelta.lower()
        while scelta != "y" and scelta != "n":
          clear()
          scelta = input("Risposta invalida, reinserire? [y/n]: ")
          scelta = scelta.lower()
        if scelta == "y":
          continue
        elif scelta == "n":
          print("Salto...")
          break

  if countLog == 0:
    exit(f"{bcolors.WARNING}Nessun log inserito, termino{bcolors.ENDC}")

  matriceDiz = []

  # Legge ed elabora il file
  for log in logs:
    for line in log:
      linea = elabora(line)
      matriceDiz.append(tabella(linea))
  return matriceDiz

# TODO #
def noInput(logs):

  cntIp = 0
  cntSrc = 0
  cntPort = 0
    
  count = 0
  return 0

def ipSearch(logs):
  dots = 0
  cont = 0
  numbers = 0
  ip = input("Inserisci l'IP da ricercare: ")    
  
  # check formato ip
  for c in ip:
    if c == ".":
      dots += 1
    elif c.isdigit():
      numbers += 1
  
  if dots != 3 or numbers > 12 or numbers < 4:
    clear()
    print(f"L'IP{bcolors.WARNING}", ip, f"{bcolors.ENDC}non è formattato correttamente")
    ipSearch(logs)

  for riga in logs:
    for campo in riga:
      if riga[campo] == ip:
        cont += 1
  clear()
  print(f"L'IP{bcolors.WARNING}", ip, f"{bcolors.ENDC}è stato trovato{bcolors.WARNING}", cont, f"{bcolors.ENDC}volte")
  menu(logs)
  return 0

def fieldSearch(logs):
  # Dizionario dei parametri
  dizCampi = {
    1: "action",
    2: "src",
    3: "dst",
    4: "msg"
  }

  n = 0

  while True and n < 1 or n > 4:
    try:
      n = int(input("Inserisci quanti campi vuoi ricercare [Min 1, Max 4]: "))
      if n == 0:
        clear()
        print(f"{bcolors.WARNING}Impossibile ricercare 0 campi, riprova{bcolors.ENDC}")
        continue
      else:
        break
    except ValueError:
      clear()
      print(f"{bcolors.WARNING}Input inserito non numerico, riprovare{bcolors.ENDC}")

  lstCampi = []
  clear()

  # Inserimento dei requisiti nell'array
  for i in range(0, n):
    while True:
      try:
        campo = int(input("Inserisci i campi da ricercare [1 = action, 2 = src, 3 = dst, 4 = msg]: "))
        break
      except ValueError:
        clear()
        print(f"{bcolors.WARNING}Valore inserito non numerico, riprova{bcolors.ENDC}\n")
    lstCampi.append(dizCampi[campo])

  # Check che rimuove i duplicati inseriti se ci sono
  lstCampi = list(dict.fromkeys(lstCampi))

  # Condizione del join per fare comparire in output una riga pulita, altrimenti output con parentesi quadrate
  cond = " "

  for riga in logs:
    frase = []
    for campo in lstCampi:
      frase.append(outputMatrix(campo, riga))
    print(f"{bcolors.WARNING}", cond.join(frase), f"{bcolors.ENDC}")

  menu(logs)
  return 0

def menu(logs):
  while True:
    try:
      print("\nMENU:\n1. Panoramica generale dei log scelti\n2. Ricerca ip\n3. Ricerca campi specifici\n4. Esci\n")
      scelta = int(input("Selezionare un opzione: "))
      break
    except ValueError:
      clear()
      print(f"{bcolors.WARNING}Valore inserito non numerico.{bcolors.ENDC}")
  clear()

  while scelta < 1 or scelta > 4:
    print(f"{bcolors.WARNING}Opzione inserita non valida. Reinserire{bcolors.ENDC}")
    menu(logs)
    clear()

  if scelta == 1:
    noInput(logs)
  elif scelta == 2:
    ipSearch(logs)
  elif scelta == 3:
    fieldSearch(logs)
  elif scelta == 4:
    exit(f"{bcolors.WARNING}Script terminato con successo.{bcolors.ENDC}")

# Main Thread
def main():
  syncsec()
  logs = parser()
  clear()
  menu(logs)
  return 0

# Condizione che verifica se lo script fa parte di un modulo oppure se lo script e' solo in esecuzione. Se e' solo in esecuzione fa partire il main thread
if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    exit(f"\n{bcolors.WARNING}Script interrotto dall'utente{bcolors.ENDC}")