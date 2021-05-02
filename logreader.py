# Sviluppato da Daniel D'Angeli e Ugo Monticone, email: daniel.dangeli@syncsecurity.it

version = "0.1"
import re

# Funziona che elabora la linea per determinare i valori del log
def elabora(l):
    word = ""
    arr = []
    found = 0
    for i in range(len(l)):
        if l[i] == '"':
            found += 1
            continue #rimuove doppio apice da output
        if l[i] == " ":
            if found == 1:
                #prosegui, testo
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

def tabella(lst):
  dic = {}
  for item in lst:
    ss = item.split("=")
    dic[ss[0]] = ss[1]
  return dic

# Funzione che elabora linea per linea ed estrapola i valori inseriti in input come condizione
def outputMatrix(campo, riga):
  for valore in riga:
    if valore == campo:
      print(valore, "=", riga[valore])
      continue

print("\nLogReader", version, "\n")

log = "testlog.txt"

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

# Inserimento dei requisiti nell'array
for i in range(0, n):
  campo = int(input("Inserisci i campi da ricercare [1 = action, 2 = src, 3 = dst, 4 = msg]: "))
  lstCampi.append(dizCampi[campo])

# Check che rimuove i duplicati inseriti se ci sono
lstCampi = list(dict.fromkeys(lstCampi))

matriceDiz = []

# Legge il file
with open(log, "rt") as f:
  f = f.readlines()
  for line in f:
    linea = elabora(line)
    matriceDiz.append(tabella(linea))

for riga in matriceDiz:
  for campo in lstCampi:
    outputMatrix(campo, riga) 
