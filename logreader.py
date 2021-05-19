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
  
  print("\nLogReader 0.4b\n")
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
    if valore == campo:
      print(valore, "=", bcolors.WARNING + riga[valore] + bcolors.ENDC)
      break

# Funziona che chiede in input i log da leggere e parsa i file
def parser():
  logs = []
  nLog = int(input("Quanti log vuoi leggere?: "))
  clear()

  for i in range(0, nLog):
    print("Inserisci la path del", i + 1, "log: ")
    log = input()

    with open(log, "rt") as f:
      f = f.readlines()
      logs.append(f)
      continue
    
  matriceDiz = []

  # Legge ed elabora il file
  for log in logs:
    for line in log:
      linea = elabora(line)
      matriceDiz.append(tabella(linea))
  return matriceDiz

# TODO #
def noInput(logs):
  
  return 0

# TODO #
def ipSearch(logs):
  ip = input("Inserisci l'ip da ricercare: ")
  cont = 0
  for riga in logs:
    for campo in riga:
      if riga[campo] == ip:
        cont += 1
  clear()
  print(f"{bcolors.WARNING}L'IP è stato trovato", cont, f"volte{bcolors.ENDC}")  
  return 0

def fieldSearch(logs):
  # Dizionario dei parametri
  dizCampi = {
    1: "action",
    2: "src",
    3: "dst",
    4: "msg"
  }

  n = int(input("Inserisci quanti valori vuoi ricercare [Min 1, Max 4]: "))

  while n < 1 or n > 4:
    n = int(input("Input errato, riprovare: "))

  lstCampi = []
  clear()

  # Inserimento dei requisiti nell'array
  for i in range(0, n):
    campo = int(input("Inserisci i campi da ricercare [1 = action, 2 = src, 3 = dst, 4 = msg]: "))
    lstCampi.append(dizCampi[campo])

  # Check che rimuove i duplicati inseriti se ci sono
  lstCampi = list(dict.fromkeys(lstCampi))
  
  for riga in logs:
    for campo in lstCampi:
      outputMatrix(campo, riga)
  return 0

# Main Thread
def main():
  syncsec()

  logs = parser()
  clear()

  print("MENU:\n1. Panoramica generale dei log scelti\n2. Ricerca ip\n3. Ricerca campi specifici\n")
  scelta = int(input("Selezionare un opzione: "))
  clear()
  
  if scelta == 1:
    noInput(logs)
  elif scelta == 2:
    ipSearch(logs)
  elif scelta == 3:
    fieldSearch(logs)
  
  return 0

# Condizione che verifica se lo script fa parte di un modulo oppure se lo script e' solo in esecuzione. Se e' solo in esecuzione fa partire il main thread
if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print(f"\n{bcolors.WARNING}Script interrotto dall'utente{bcolors.ENDC}")
    exit()