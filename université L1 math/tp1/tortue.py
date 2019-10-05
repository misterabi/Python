#### debut de partie a modifier ####

from math import *

nbLignes=int(input("nombre de coté de la figure : "))
lgLigne=int(input("longeur de chaque coté : "))
angle= 360/nbLignes
xInit=-(lgLigne)/2  
yInit=-(lgLigne)/2
print(angle)

#### fin de partie a modifier ####







### Ne pas modifier ce qui suit ###

from turtle import *

setup(600, 600)
reset()
up()
goto(xInit, yInit)
down()
a=0
while a<nbLignes:
  a+=1
  forward(lgLigne)
  left(angle)
 
exitonclick()
