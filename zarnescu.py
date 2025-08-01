#scris functie coinflip, prezentand parametrii de print si print de expresie
import random
print(f"Moneda a cazut ","cap." if (random.randint(0, 1)) else "pajura.", " Neat!", sep='')
