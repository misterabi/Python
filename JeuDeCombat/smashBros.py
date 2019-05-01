import pygame
import threading
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
bleu = (14, 180, 245)
black = (0, 0, 0)
white = (255, 255, 255)
red = 255, 0, 0


directionVitesse=5
CooldDown=1

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

class player(pygame.sprite.Sprite):

    sequences = [(0, False), (0, 1, False), (1, 6, True), (14, 3, False), (19, 1, False), (25, 1, False)]

    def __init__(self,position,image):
        pygame.sprite.Sprite.__init__(self)

        self.spriteSheet = pygame.image.load(image).convert_alpha()

        self.image = self.spriteSheet.subsurface(pygame.Rect(0, 0, 64, 90))
        self.rect = pygame.Rect(0, 0, 32, 64)
        self.rect.center = position
        self.isJump=False
        self.jumpCount=10
        self.sens_personnage_droite=True
        self.sens_personnage_gauche=False

        self.cooldown=1
        self.numeroSequence = 0
        self.numeroImage = 0
        self.flip = False

        self.deltaTime = 0
        self.vitesse = 2

    def update(self):

        self.deltaTime = self.deltaTime + 16

        if self.deltaTime >= 50:
            self.deltaTime = 0

            n = player.sequences[self.numeroSequence][0] + self.numeroImage
            self.image = self.spriteSheet.subsurface(pygame.Rect(n % 10 * 64, n // 10 * 100, 64, 90))
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
    def jump(self):
        self.setSequence(4)
    def goRight(self):
        self.rect = self.rect.move(self.vitesse, 0)
        self.flip = False
        self.setSequence(2)

    def goLeft(self):
        self.rect = self.rect.move(-self.vitesse, 0)
        self.flip = True
        self.setSequence(2)
    def punch(self):
        self.setSequence(5)

    def rect(self):
        self.image = player.spriteSheet.subsurface(pygame.Rect(320, 180, 64, 90))

    def shoot(self,speed):
        if self.sens_personnage_droite is True:
            ball = Ball((self.rect.centerx+30,self.rect.centery),speed)
        if self.sens_personnage_gauche is True:
            ball = Ball((self.rect.centerx-30,self.rect.centery),speed)

        bullets.add(ball)

class Ball(pygame.sprite.Sprite):
    def __init__(self,position,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/fireball1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed= speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.y > 720:
            self.kill()
def mouvement(joueur,ennemie,leurre,gauche,droite,accroupir,saut,tire,coup):
    global directionVitesse
    if event.type == pygame.KEYDOWN and event.key is leurre or droite or gauche or accroupir or saut or  tire or coup :
        if gauche and joueur.rect.x > 1:
            joueur.goLeft()
        if droite and ennemie.rect.x < 685 and not joueur.rect.colliderect(ennemie.rect):
            joueur.goRight()

        if event.type == pygame.KEYUP:
            if droite:
                joueur.sens_personnage_gauche=False
                joueur.sens_personnage_droite=True
                directionVitesse=5
            if gauche:
                joueur.sens_personnage_droite=False
                joueur.sens_personnage_gauche=True
                directionVitesse=-5
        if joueur.cooldown >=1 and tire :
            pygame.time.Clock().tick(50)
            joueur.punch()
            abi.cooldown -= 1
            if joueur.rect.colliderect(ennemie.rect):
                print("toucher")

        if joueur.cooldown >=1.5 and coup:
            joueur.shoot(directionVitesse)
            joueur.cooldown -= 2
        if not joueur.isJump:
            if accroupir:
                joueur.crouch()

            if saut:
                joueur.isJump = True
                print("saut")

        if joueur.isJump is True:
            if joueur.jumpCount >= -10:
                neg = 1
                if joueur.jumpCount < 0:
                    neg = -1
                pygame.time.Clock().tick(50)
                joueur.rect = joueur.rect.move(0, -(joueur.jumpCount ** 2) * 0.3 * neg)

                joueur.jumpCount -= 1
            else:
                joueur.isJump = False
                joueur.jumpCount = 10

    else:
        joueur.stand()
    if joueur.cooldown <1.6:
        joueur.cooldown+=0.1

# creation des joueur
all_sprite=pygame.sprite.Group()
damage=pygame.sprite.Group()
bullets=pygame.sprite.Group()
enemie=pygame.sprite.Group()
allie=pygame.sprite.Group()

abi = player((100, 408),"image/heros1.png")
JC = player((350, 408),"image/skeletonBase.png")

enemie.add(JC)
allie.add(abi)
all_sprite.add(abi)
all_sprite.add(JC)


pygame.display.flip()

launched = True
while launched:

    pygame.time.Clock().tick(50)
    # touche de clavier

    key = pygame.key.get_pressed()
    Left1 = key[pygame.K_a]
    Right1 = key[pygame.K_d]
    Down1 = key[pygame.K_s]
    Jump1 = key[pygame.K_z]
    fire1 = key[pygame.K_g]
    punching1 = key[pygame.K_f]
    bloc1=key[pygame.K_SPACE]

    Left2 = key[pygame.K_LEFT]
    Right2 = key[pygame.K_RIGHT]
    Down2 = key[pygame.K_DOWN]
    Jump2 = key[pygame.K_UP]
    fire2= key[pygame.K_RCTRL]
    punching2=key[pygame.K_RALT]
    bloc2=key[pygame.K_RSHIFT]

    test=key[pygame.K_j]
    hits1 = pygame.sprite.groupcollide(bullets, enemie, True, False)
    hits2 = pygame.sprite.groupcollide(bullets, allie, True, False)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    mouvement(abi,JC,test,Left1,Right1,Down1,Jump1,fire1,punching1)
    mouvement(JC,abi,test,Left2,Right2,Down2,Jump2,fire2,punching2)

    if bloc2 and hits1:
        print("no damage,player2")
    elif not bloc1 and hits1:
        print("aie,player2")
    if bloc1 and hits2:
        print("no damage,player1")
    elif  not bloc2 and hits2:
        print("aie,player1")





    bullets.update()
    all_sprite.update()
    fenetre_smash_bros.fill(bleu)
    pygame.draw.rect(fenetre_smash_bros, black, rectangle)
    all_sprite.draw(fenetre_smash_bros)
    bullets.draw(fenetre_smash_bros)

    pygame.display.flip()
