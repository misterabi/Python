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
	Touche 0 : sauter
	Touche 1 : attaquer 
 Si un joueur A attaque un joueur B alors le joueur B perd une vie.
 Définition de attaquer : premier qui touche l'autre
Phase de développement:
1/ Afficher 2 joueurs sur un écran
2/ Déplacer un joueur sur l'écran en fonction des clics clavier
3/ Attaquer un joueur
4/ Calculer victoire
"""
# couleur
time=16
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


class player(pygame.sprite.Sprite):
    spriteSheet = pygame.image.load("image/heros.png").convert_alpha()
    sequences = [(0,False),(0,1,False), (1,6,True),(7,10,False)]

    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)

        self.image = player.spriteSheet.subsurface(pygame.Rect(0, 0, 32, 64))
        self.rect = pygame.Rect(0, 0, 32, 64)
        self.rect.center = position

        self.numeroSequence = 0
        self.numeroImage = 0
        self.flip = False

        self.deltaTime = 0
        self.vitesse = 1

    def update(self, time):
        self.deltaTime = self.deltaTime + time

        if self.deltaTime >= 50:
            self.deltaTime = 0

            n = player.sequences[self.numeroSequence][0] + self.numeroImage
            self.image = player.spriteSheet.subsurface(pygame.Rect(n % 10 * 32, n // 10 * 64, 32, 64))
            if self.flip:
                self.image = pygame.transform.flip(self.image, True, False)

            self.numeroImage = self.numeroImage + 1

            if self.numeroImage == player.sequences[self.numeroSequence][1]:
                if player.sequences[self.numeroSequence][2]:
                    self.numeroImage = 0
                else:
                    self.numeroImage = self.numeroImage - 1

    def setSequence(self, n):
        if self.numeroSequence != n:
            self.numeroImage = 0
            self.numeroSequence = n
    def stand(self):
        self.setSequence(1)
    def crouch(self):
        self.setSequence(3)
    def goRight(self):
        self.rect = self.rect.move(self.vitesse, 0)
        self.flip = False
        self.setSequence(2)

    def goLeft(self):
        self.rect = self.rect.move(-self.vitesse, 0)
        self.flip = True
        self.setSequence(2)
def draw():
    sol.draw()

class fire_ball:
    # creation d'un sprite boule de feu directionnel
    def __init__(self,):
        pygame.sprite.Sprite.__init__(self)

# creation de platform

sol = platform("image/sol.bmp", (0, 450, 720, 480))

# creation des joueur

abi = player((100, 417))
JC = player((350, 417))


isJump1 = False
jumpCount1 = 10
isJump2 = False
jumpCount2 = 10
pygame.display.flip()

launched = True
while launched:

    pygame.time.Clock().tick(100)
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
    #pb nous pouvons sauter seulement si nous appuyons sur vancer et sauter
    if event.type == pygame.KEYDOWN and event.key is key[pygame.K_j] or Jump1 or Right1 or Left1:
        if Left1 and abi.rect.x > 1:
            abi.goLeft()
        if Right1 and abi.rect.x < 685:
            abi.goRight()
        if not isJump1:
            if Down1 and abi.rect.y > 348:
                abi.crouch()
            if Jump1:
                isJump1 = True
        else:
            if jumpCount1 >= -10:
                neg = 1
                if jumpCount1 < 0:
                    neg = -1
                pygame.time.Clock().tick(50)
                abi.rect = abi.rect.move(0, -(jumpCount1 ** 2) * 0.5 * neg)
                jumpCount1 -= 1
            else:
                isJump1 = False
                jumpCount1 = 10
    else:
        abi.stand()
    if event.type == pygame.KEYDOWN and event.key is key[pygame.K_j] or Jump2 or Right2 or Left2:
        if Left2 and JC.rect.x > 1:
            JC.goLeft()
        if Right2 and JC.rect.x < 685:
            JC.goRight()
        if not isJump2:
            if Down2 and JC.rect.y < 348:
                JC.crouch()
            if Jump2:
                isJump2 = True
        else:
            if jumpCount2 >= -10:
                neg = 1
                if jumpCount2 < 0:
                    neg = -1
                pygame.time.Clock().tick(50)
                JC.rect = JC.rect.move(0, -(jumpCount2 ** 2) * 0.5 * neg)
                jumpCount2 -= 1
            else:
                isJump2 = False
                jumpCount2 = 10
    else:
        JC.stand()

    player.update(abi,time)
    player.update(JC, time)
    fenetre_smash_bros.fill(bleu)
    pygame.draw.rect(fenetre_smash_bros, black, rectangle)
    fenetre_smash_bros.blit(JC.image, JC.rect)
    fenetre_smash_bros.blit(abi.image, abi.rect)
    draw()
    pygame.display.flip()
