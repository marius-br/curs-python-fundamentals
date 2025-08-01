"""
Assignment 6 (lines 1-23)
Scrie o funcție media(lista_numere) care primește o listă de numere și returnează media lor
aritmetică.
Testează funcția cu 3 liste diferite:
- [10, 20, 30]
- [1, 2, 3, 4, 5]
- []
Extensie: tratează cazul în care lista este goală (returnează "Lista este goală").
"""

def average(num_list):
    total = 0
    for i in num_list:
        total += i
    if len(num_list) != 0:
        avg = total / len(num_list)
    else:
        avg = "Lista este goala"
    return avg

lista_numere = [6,12,35]
print(f"Media numerelor din lista este: ", round(average(lista_numere),2))
print("New line, just to check")