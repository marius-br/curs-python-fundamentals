print("salut , ai un milion pana la salariu ? ")

import random

def genereaza_numere_loterie():
    numere = random.sample(range(1, 50), 6)
    numere.sort()
    return numere

numere_loterie = genereaza_numere_loterie()
print("Numerele extrase sunt:", numere_loterie)
