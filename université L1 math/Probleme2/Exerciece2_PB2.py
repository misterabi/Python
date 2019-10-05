from turtle import *


def rectangle():
    for loop in range(2):
        fd(120)
        lt(90)
        fd(180)
        lt(90)


def octogone():
    for loop in range(8):
        fd(60)
        lt(45)


def promenade():
    speed(10)
    for loop in range(36):
        forward(200)
        left(170)


def carre(couleur_carre):
    if couleur_carre:
        couleur = "black"
    else:
        couleur = "white"

    fillcolor(couleur)
    begin_fill()
    print(couleur_carre)
    for loop in range(4):
        fd(30)
        lt(90)
    end_fill()


def damier():
    colorier = False
    for loop in range(6):
        PositionTortue_X = xcor()
        PositionTortue_Y = ycor()
        for loop in range(6):
            colorier = not colorier
            carre(colorier)
            fd(30)
        PositionTortue_Y += 30
        penup()
        goto(PositionTortue_X, PositionTortue_Y)
        pendown()
        colorier = not colorier


while True:
    penup()
    tp = pos()
    setposition(-300, -100)
    pendown()
    rectangle()
    fd(220)
    octogone()
    fd(140)
    promenade()
    fd(270)
    damier()
    break
done()


