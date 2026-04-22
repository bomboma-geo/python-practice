nombres = []

for i in range(5):
    valeur = int(input("Entrez un nombre : "))
    nombres.append(valeur)

print("Liste :", nombres)
print("Somme :", sum(nombres))
print("Max :", max(nombres))
print("Min :", min(nombres))

def calcul_moyenne(liste):
    return sum(liste) / len(liste)

moyenne = calcul_moyenne(nombres)
print("Moyenne :", moyenne)

if moyenne >= 10:
    print("Admis")
else:
    print("Refusé")
