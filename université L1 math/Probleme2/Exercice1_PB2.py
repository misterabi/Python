from turtle import *

color('black')


def droite(longueur, angle):
    fd(longueur)
    lt(angle)


penup()
tp = pos()
setposition(-100, -100)
pendown()

while True:

    speed(10)
    droite(195, 90)
    droite(195, 30)
    droite(195, 120)
    droite(195, 30)
    droite(195, 180)
    droite(195, 270)
    droite(195, 270)
    droite(195, 270)
    droite(39, 270)
    droite(65, 90)
    droite(39, 90)
    droite(65, 270)
    penup()
    droite(39, 270)
    droite(117, 0)
    pendown()
    for loop in range(4):
        droite(39, 90)
    break
done()
