# functia input intoarce valori de tip string
# int(input) converteste la int stringul primit
x=int(input("Dati x:"))
y=int(input("Dati y:"))

#print(x)
#print("x")
#print(x+y)
#print(x>y)

if x%2==0: # daca numarul se imparte fara rest la 2.
    print(f"{x} este par") # cu f inainte de " pot folosi variabile in acolade la print
else:
    print("x este impar")

for i in range(5): # range 5 merge iterativ de la 0 la 4
    print(f"i-{i}")

a = 1
while a <= 10:

    if a == 5:
        break # intrerupe executia buclei

    if a%2 != 0:
        a+=1
        continue # trece la interatia urmatoare ignorand codul de ma jos din while

    print(a)
    a += 1 # a=a+1

text = "Salut, eu sunt Python!"
print(len(text)) # len pe un text returneaza nr de carctere
print(text[0]) # la indexul 0 avem litera S.
