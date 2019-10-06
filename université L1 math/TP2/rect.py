from upemtk import *
from random import randint

# création de la fenêtre graphique
cree_fenetre(600, 600)

rect_1_x = [randint(20, 580),randint(0, 599)]
rect_1_y = [randint(20, 580),randint(0, 599)]
rect_2_x = [randint(20, 580),randint(0, 599)]
rect_2_y = [randint(20, 580),randint(0, 599)]

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

texte(20, 20, "(20,20)", taille=12, ancrage="center")
texte(20, 580, "(20,580)", taille=12, ancrage="center")
texte(580, 20, "(580,20)", taille=12, ancrage="center")
texte(580, 580, "(580,580)", taille=12, ancrage="center")

texte(x1, y1-10, "(x1,y1)", taille=12, ancrage="center")
texte(x2, y2+10, "(x2,y2)", taille=12, ancrage="center")
texte(x3, y3-10, "(x3,y3)", taille=12, ancrage="center")
texte(x4, y4+10, "(x4,y4)", taille=12, ancrage="center")

# partie à compléter

'''if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
    texte(300, 300, "pas touché !", taille=24, ancrage="center")
else:
    texte(300, 300, "touché !", taille=24, ancrage="center")
'''
def intersection(x1,x2,x3,x4,y1,y2,y3,y4):
    if (x1 < x4 and x2 > x3 and y2 > y3 and y1 < y4):
        return True
    else:
        return False
'''
    if (x1>x4 or x3 > x2):
        print('False X')
        return False
    elif (y1<y4 or y3 <y2):
        print('False Y')
        return False
    return True
'''
coord_x = 'x1 : ' + str(x1) + ' x2 : ' + str(x2) + ' x3 : ' + str(x3) + ' x4 : ' + str(x4)
coord_y = 'y1 : ' + str(y1) + ' y2 : ' + str(y2) + ' y3 : ' + str(y3) + ' y4 : ' + str(y4)

texte(300, 10, coord_x, taille=12, ancrage="center")
texte(300, 20, coord_y, taille=12, ancrage="center")

if intersection(x1,x2,x3,x4,y1,y2,y3,y4) or intersection(x3,x4,x1,x2,y3,y4,y1,y2):
    texte(300, 300, "touché !", taille=24, ancrage="center")
else:
    texte(300, 300, "pas touché !", taille=24, ancrage="center")


# fermeture de la fenêtre
attend_fermeture()
