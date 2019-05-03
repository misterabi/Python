import pygame


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
red = (255, 0, 0)

directionVitesse = 5
pygame.init()

# titre
pygame.display.set_caption('SMASH BROS')
pygame.key.set_repeat(30, 30)
# taille de la fenetre
fenetre_smash_bros = pygame.display.set_mode((720, 480))

# creation du sol
rectangle = pygame.Rect(0, 450, 720, 480)
pygame.draw.rect(fenetre_smash_bros, black, rectangle)


class player(pygame.sprite.Sprite):
    sequences = [(0, False), (0, 1, False), (1, 6, True), (14, 3, False), (19, 1, False), (25, 1, False)]

    def __init__(self, position, image, coordonne):
        pygame.sprite.Sprite.__init__(self)

        self.spriteSheet = pygame.image.load(image).convert_alpha()

        self.image = self.spriteSheet.subsurface(pygame.Rect(0, 0, 64, 90))
        self.rect = pygame.Rect(0, 0, 32, 64)
        self.rect.center = position
        self.health = 100
        self.alive = True

        self.sens_personnage_droite = True
        self.sens_personnage_gauche = False

        self.isJump = False
        self.jumpCount = 10
        self.cooldownSuperPower = 15
        self.cooldownFire = 1
        self.numeroSequence = 0
        self.numeroImage = 0
        self.flip = False

        self.deltaTime = 0
        self.vitesse = 2

        all_sprite.add(self)

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

    def shoot(self, speed):
        if self.sens_personnage_droite is True:
            ball = Ball((self.rect.centerx + 30, self.rect.centery), speed, "image/fireball1.png", False)
        if self.sens_personnage_gauche is True:
            ball = Ball((self.rect.centerx - 30, self.rect.centery), speed, "image/fireball1.png", True)

        bullets.add(ball)

    def SuperPower(self, speed):
        if self.sens_personnage_droite is True:
            Superball = Ball((self.rect.centerx + 30, self.rect.centery), speed, "image/Superfireball.png", False)
        if self.sens_personnage_gauche is True:
            Superball = Ball((self.rect.centerx - 30, self.rect.centery), speed, "image/Superfireball.png", True)
        SuperPower.add(Superball)

    def Health_player_image(self, flip, coordonne_image):
        health_player_bar_image = healthBarImage(flip, coordonne_image)
        sprite_healthBar_image.add(health_player_bar_image)

    def Health_bar_player(self, coordonne, reducteur):
        sprite_healthbar_rect = HealthBar(coordonne, reducteur, self.health)
        sprite_healthBar.add(sprite_healthbar_rect)


class Ball(pygame.sprite.Sprite):
    def __init__(self, position, speed, image, flip):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = speed
        self.flip = flip

    def update(self):
        self.rect.x += self.speed
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)
        if self.rect.y > 720:
            self.kill()


class icon(pygame.sprite.Sprite):
    def __init__(self, image, coordonne):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = coordonne
        sprite_icon.add(self)


class healthBarImage(pygame.sprite.Sprite):
    def __init__(self, flip, coordonne_image ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/healthBar.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = coordonne_image
        if flip:
            self.image = pygame.transform.flip(self.image, True, False)


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, coordonne, reducteur, health):
        self.image = pygame.image.load("image/healthBar1Step.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = coordonne
        self.x2 = self.rect.right
        self.reducteur = reducteur
        self.health = health

    def update(self):
        self.rect.right = 150 * self.health / 150 * self.reducteur


def mouvement(joueur, ennemie, leurre, gauche, droite, saut, tire, coup, bloc, hitFire, hitSuperPower, ):
    global directionVitesse
    if event.type == pygame.KEYDOWN and event.key is leurre or droite or gauche or saut or tire or coup:
        if gauche and joueur.rect.x > 1:
            joueur.goLeft()
        if droite and joueur.rect.x < 685:
            joueur.goRight()

        if event.type == pygame.KEYUP:
            if droite:
                joueur.sens_personnage_gauche = False
                joueur.sens_personnage_droite = True
                directionVitesse = 5
            if gauche:
                joueur.sens_personnage_droite = False
                joueur.sens_personnage_gauche = True
                directionVitesse = -5

        if not joueur.isJump:
            if saut:
                joueur.isJump = True

        if joueur.isJump is True:
            if joueur.jumpCount >= -10:
                neg = 1
                if joueur.jumpCount < 0:
                    neg = -1
                joueur.rect = joueur.rect.move(0, -(joueur.jumpCount ** 2) * 0.3 * neg)

                joueur.jumpCount -= 1
            else:
                joueur.isJump = False
                joueur.jumpCount = 10
        # coup de poing#
        if joueur.cooldownFire >= 1 and coup:
            joueur.punch()
            joueur.cooldownFire -= 1
            if joueur.rect.colliderect(ennemie.rect):
                if ennemie.rect.x > 10 and ennemie.rect.x < 670:
                    ennemie.health -= 2.5
                    ennemie.rect = ennemie.rect.move(directionVitesse * 3, 0)
                    print("toucher")
                    joueur.cooldownSuperPower -= 1

        # boule de feu#
        if joueur.cooldownFire >= 1.5 and tire:
            joueur.shoot(directionVitesse)
            joueur.cooldownFire -= 2
        # Super Attaque#
        if tire and coup and joueur.cooldownSuperPower <= 0:
            joueur.SuperPower(directionVitesse)
            joueur.cooldownSuperPower = 15
        if tire and coup and joueur.cooldownSuperPower >= 0:
            print("il vous reste:", joueur.cooldownSuperPower)


    else:
        joueur.stand()
    if joueur.cooldownFire < 1.6:
        joueur.cooldownFire += 0.1
    # collision attaque distance#
    if bloc and hitFire:
        joueur.health -= 0
    elif not bloc and hitFire:
        joueur.health -= 2
        ennemie.cooldownSuperPower -= 0.5
        if joueur.rect.x > 10 and joueur.rect.x < 670:
            joueur.rect = joueur.rect.move(directionVitesse * 3, 0)

    if hitSuperPower:
        joueur.health -= 15
    if joueur.health <= 0:
        joueur.alive = False
        joueur.kill()


def EndGame(playeurHealth1, playeurHealth2):
    global launched
    if not playeurHealth1:
        pygame.display.quit
    if not playeurHealth2:
        pygame.display.quit


# creation des joueur
all_sprite = pygame.sprite.Group()
SuperPower = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemie = pygame.sprite.Group()
allie = pygame.sprite.Group()
sprite_icon = pygame.sprite.Group()
sprite_healthBar_image = pygame.sprite.Group()
sprite_healthBar = pygame.sprite.Group()

abi = player((100, 408), "image/heros1.png", ((40, 23), (150, 9)))
JC = player((350, 408), "image/skeletonBase.png", ((675, 23), (-150, 9)))
abi_Icon = icon("image/HeroIcon.png", (20, 25))
JC_Icon = icon("image/SkeletonIcon.png", (690, 25))
abi_healthbar_image = (False, (35, 25), abi.health)
JC_healthbar_image = (True, (650, 25), JC.health)

enemie.add(JC)
allie.add(abi)

pygame.display.flip()

launched = True
while launched:

    # pygame.time.Clock().tick(500)

    # touche de clavier

    key = pygame.key.get_pressed()
    Left1 = key[pygame.K_a]
    Right1 = key[pygame.K_d]
    Jump1 = key[pygame.K_z]
    fire1 = key[pygame.K_g]
    punching1 = key[pygame.K_f]
    bloc1 = key[pygame.K_SPACE]

    Left2 = key[pygame.K_LEFT]
    Right2 = key[pygame.K_RIGHT]
    Jump2 = key[pygame.K_UP]
    fire2 = key[pygame.K_RCTRL]
    punching2 = key[pygame.K_RALT]
    bloc2 = key[pygame.K_RSHIFT]

    test = key[pygame.K_j]
    hitsFirePlayer1 = pygame.sprite.groupcollide(bullets, allie, True, False)
    hitsFirePlayer2 = pygame.sprite.groupcollide(bullets, enemie, True, False)
    hitSuperPowerPlayer1 = pygame.sprite.groupcollide(SuperPower, allie, True, False)
    hitSuperPowerPlayer2 = pygame.sprite.groupcollide(SuperPower, enemie, True, False)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    mouvement(abi, JC, test, Left1, Right1, Jump1, fire1, punching1, bloc1, hitsFirePlayer1, hitSuperPowerPlayer1)
    mouvement(JC, abi, test, Left2, Right2, Jump2, fire2, punching2, bloc2, hitsFirePlayer2, hitSuperPowerPlayer2)

    abi.Health_player_image(True, (115, 30))
    JC.Health_player_image(False, (600, 30))

    if not abi.alive:
        launched = False
    if not JC.alive:
        launched = False

    SuperPower.update()
    bullets.update()
    all_sprite.update()
    fenetre_smash_bros.fill(bleu)
    pygame.draw.rect(fenetre_smash_bros, black, rectangle)
    all_sprite.draw(fenetre_smash_bros)
    bullets.draw(fenetre_smash_bros)
    SuperPower.draw(fenetre_smash_bros)
    sprite_icon.draw(fenetre_smash_bros)
    sprite_healthBar_image.draw(fenetre_smash_bros)

    pygame.display.flip()
