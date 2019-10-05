from upemtk import *
from random import randint

# création de la fenêtre graphique
cree_fenetre(600, 600)

rect_1_x = [randint(0, 599),randint(0, 599)]
rect_1_y = [randint(0, 599),randint(0, 599)]
rect_2_x = [randint(0, 599),randint(0, 599)]
rect_2_y = [randint(0, 599),randint(0, 599)]

rect_1_x.sort()
rect_1_y.sort()
rect_2_x.sort()
rect_2_y.sort()

# sélection des coins et dessin du premier rectangle
x1, x2 = rect_1_x[0], rect_1_x[1]
y1, y2 = rect_1_y[0], rect_1_y[1]
rectangle(x1, y1, x2, y2, couleur='blue', epaisseur=3)

# sélection des coins et dessin du second rectangle
x3, x4 = rect_2_x[0], rect_2_x[1]
y3, y4 = rect_2_y[0], rect_2_y[1]
rectangle(x3, y3, x4, y4, couleur='red', epaisseur=3)

# partie à compléter

'''if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
    texte(300, 300, "pas touché !", taille=24, ancrage="center")
else:
    texte(300, 300, "touché !", taille=24, ancrage="center")
'''
def intersection(x1,x2,x3,x4,y1,y2,y3,y4):
    if (x1>x4 or x3 > x2):
        return False
    elif (y1<y4 or y3 <y2):
        return False
    return True
if x1 > x2:
    x1,x2=x2,x1

coord = 'X1 : ' + str(x1) + ' x2 : ' + str(x2) + ' X3 : ' + str(x3) + ' X4 : ' + str(x4) + ' y1 : ' + str(y1) + ' y2 : ' + str(y2) + ' y3 : ' + str(y3) + ' y4 : ' + str(y4)
texte(300, 50, coord, taille=12, ancrage="center")

if intersection(x1,x2,x3,x4,y1,y2,y3,y4):
    texte(300, 300, "touché !", taille=24, ancrage="center")
else:
    texte(300, 300, "pas touché !", taille=24, ancrage="center")


# fermeture de la fenêtre
attend_fermeture()
