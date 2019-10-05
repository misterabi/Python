from random import randint
"""
piece = randint(0, 1)
if piece == 0:
    print("pile")
else:
    print("face")
"""

dividende = randint(100, 999)
diviseur = randint(2, 9)

print("Le nombre", dividende, " est divisible par ", diviseur,"?Répondre par 'o' pour oui et 'n' pour non")

reponse = (input("reponse :"))
if reponse == "n":
    reponse = False
elif reponse == "o":
    reponse = True
else:
    print("Réponse invalide")
    exit(-1)
if dividende % diviseur == 0:
    est_divisible = True
else:
    est_divisible = False
if reponse is est_divisible:
    print('Bravo !')
else:
    print('Perdu !')
