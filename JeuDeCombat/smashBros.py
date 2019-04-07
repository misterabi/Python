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
pygame.init()

# couleur
time=16
bleu = (14, 180, 245)
black = (0, 0, 0)
white = (255, 255, 255)
red = 255, 0, 0

keys = pygame.key.get_pressed()
Left1 =keys[pygame.K_a]
Right1 = keys[pygame.K_d]
Up1 = keys[pygame.K_w]
Down1 =keys[pygame.K_s]
Jump1 = keys[pygame.K_SPACE]
Left2 = keys[pygame.K_LEFT]
Right2 = keys[pygame.K_RIGHT]
Up2 = keys[pygame.K_UP]
Down2 =keys[pygame.K_DOWN]
Jump2 =keys[pygame.K_RCTRL]

isJump1 = False
jumpCount1 = 10
isJump2 = False
jumpCount2 = 10


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
    sequences = [(0,False),(0,1,False), (1,6,True),(7,2,False)]

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

def deplacement(gauche, droite, se_baisser, saut, check_saut, hauteur_saut, joueur):
    if gauche and joueur.rect.x > 1:
        joueur.gotLeft()
    if droite and joueur.rect.y <685:
        joueur.goRight()
    if not check_saut :
        if se_baisser and joueur.rect.y > 348:
            Joueur.crouch()
        if saut:
            check_saut = True
    if check_saut:
        if hauteur_saut >= -10:
            neg=1
            if hauteur_saut < 0:
                neg=-1
            pygame.time.Clock().tick(50)
            joueur.rect = joueur.rect.move(0,-(hauteur_saut ** 2)* 0.5 * neg)
            hauteur_saut -= 1
        else:
            check_saut=False
            hauteur_saut = 10
    else:
        joueur.stand()

class fire_ball:
    # creation d'un sprite boule de feu directionnel
    def __init__(self,):
        pygame.sprite.Sprite.__init__(self)

# creation de platform

sol = platform("image/sol.bmp", (0, 450, 720, 480))

# creation des joueur

abi = player((100, 417))
JC = player((350, 417))



pygame.display.flip()

launched = True
while launched:

    pygame.time.Clock().tick(100)
    # touche de clavier
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

    deplacement(Left1,Right1,Down1,Jump1,isJump1,jumpCount1,abi)
    deplacement(Left2,Right2,Down2,Jump2,isJump2,jumpCount2,JC)

    player.update(abi,time)
    player.update(JC, time)
    fenetre_smash_bros.fill(bleu)
    pygame.draw.rect(fenetre_smash_bros, black, rectangle)
    fenetre_smash_bros.blit(JC.image, JC.rect)
    fenetre_smash_bros.blit(abi.image, abi.rect)
    draw()
    pygame.display.flip()
