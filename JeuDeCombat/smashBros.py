import pygame
from pygame.rect import Rect

"""
Jeu Smash Bros
Objectif : Survivre
Nombre de joueurs maximum : 2
Nombre de vie par joueur  : 3
Règles de jeu :
 Joueur 1 :
	Touches directionnelle : déplacer
	Touche ESPACE : sauter
	Touche V : attaquer 
 Joueur 2 : 
	Touches Z,Q,S,D : déplacer
	Touche crtl : sauter
	Touche maj : attaquer 
 Si un joueur A attaque un joueur B alors le joueur B perd une vie.

 Définition de attaquer : premier qui touche l'autre

Phase de développement:
1/ Afficher 2 joueurs sur un écran
2/ Déplacer un joueur sur l'écran en fonction des clics clavier
3/ Attaquer un joueur
4/ Calculer victoire
"""
# couleur

bleu = (14, 180, 245)
black = (0, 0, 0)
white = (255, 255, 255)
red = 255, 0, 0

pygame.init()

# titre
pygame.display.set_caption('SMASH BROS')
pygame.key.set_repeat(30, 30)
# taille de la fenetre
fenetre_smash_bros = pygame.display.set_mode((720, 480))

# creation du sol
rectangle = pygame.Rect(0, 450, 720, 480)
fenetre_smash_bros.fill(bleu)
pygame.draw.rect(fenetre_smash_bros, black, rectangle)


class platform(Rect, object):
    def __init__(self, image, rect):
        Rect.__init__(self, rect)
        self.image = pygame.image.load(image).convert()

    def draw(self):
        fenetre_smash_bros.blit(self.image, self)


class player:

    def __init__(self, source, position):
        self.source = pygame.image.load(source).convert()
        self.rect = self.source.get_rect()
        self.rect.center = position
        fenetre_smash_bros.blit(self.source, self.rect)
        self.source.set_colorkey(white)

    def damage(self, punch, distance, SuperPower):
        self.punch = punch
        self.distance = distance
        self.SuperPower = SuperPower
    def health(self,healthmax,life):
        self.heathmax=healthmax
        self.Number_life=life

def draw():
    sol.draw()

class fire_ball:
    # creation d'un sprite boule de feu directionnel
    def __init__(self, droite, haut, bas, gauche):
        pygame.sprite.Sprite.__init__(self)

# creation de platform

sol = platform("image/sol.bmp", (0, 450, 720, 480))

# creation des joueur

abi = player("image/heros1_marche1D.png", (100, 398))
JC = player("image/heros1_marche1G.png", (350, 398))


isJump1 = False
jumpCount1 = 10
isJump2 = False
jumpCount2 = 10
pygame.display.flip()

launched = True
while launched:
    # limitation de la boucle
    pygame.time.Clock().tick(50)
    # touche de clavier

    key = pygame.key.get_pressed()
    Left1 = key[pygame.K_a]
    Right1 = key[pygame.K_d]
    Up1 = key[pygame.K_w]
    Down1 = key[pygame.K_s]
    Jump1 = key[pygame.K_SPACE]
    Left2 = key[pygame.K_LEFT]
    Right2 = key[pygame.K_RIGHT]
    Up2 = key[pygame.K_UP]
    Down2 = key[pygame.K_DOWN]
    Jump2 = key[pygame.K_RCTRL]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    if Left1 and abi.rect.x > 1:
        abi.rect = abi.rect.move(-5, 0)
    if Right1 and abi.rect.x < 685:
        abi.rect = abi.rect.move(5, 0)
    if not (isJump1):
        if Down1 and abi.rect.y < 348:
            abi.rect = abi.rect.move(0, 5)
        if Jump1:
            isJump1 = True
    else:
        if jumpCount1 >= -10:
            neg = 1
            if jumpCount1 < 0:
                neg = -1
            abi.rect = abi.rect.move(0, -(jumpCount1 ** 2) * 0.5 * neg)
            jumpCount1 -= 1
        else:
            isJump1 = False
            jumpCount1 = 10
    if Left2 and JC.rect.x > 1:
        JC.rect = JC.rect.move(-5, 0)
    if Right2 and JC.rect.x < 685:
        JC.rect = JC.rect.move(5, 0)
    if not (isJump2):
        if Down2 and JC.rect.y < 348:
            JC.rect = JC.rect.move(0, 5)
        if Jump2:
            isJump2 = True
    else:
        if jumpCount2 >= -10:
            neg = 1
            if jumpCount2 < 0:
                neg = -1
            JC.rect = JC.rect.move(0, -(jumpCount2 ** 2) * 0.5 * neg)
            jumpCount2 -= 1
        else:
            isJump2 = False
            jumpCount2 = 10
    fenetre_smash_bros.fill(bleu)
    pygame.draw.rect(fenetre_smash_bros, black, rectangle)
    fenetre_smash_bros.blit(JC.source, JC.rect)
    fenetre_smash_bros.blit(abi.source, abi.rect)
    draw()
    pygame.display.flip()
