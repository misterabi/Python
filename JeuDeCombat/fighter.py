import pygame
import constante

# couleur
black = (0, 0, 0)
white = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Yellow = (255, 255, 0)
Orange = (255, 165, 0)

directionSpeed = 5
pygame.init()

# chargement des sons
pygame.mixer.music.load('sons/music_background.ogg')
# lance la music

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
# titre
pygame.display.set_caption('FIGHTER')
pygame.key.set_repeat(30, 30)
# taille de la fenetre
fenetre_fighter = pygame.display.set_mode((constante.ScreenWidth, constante.ScreenHeight))


class player(pygame.sprite.Sprite):

    debout = (0, 1, False)
    marche = (1, 6, True)
    coup_de_poing = (25, 1, False)
    defence = (29,1,False)

    animations = [debout, marche, coup_de_poing,defence]

    def __init__(self, position, image):
        pygame.sprite.Sprite.__init__(self)

        self.spriteSheet = pygame.image.load(image).convert_alpha()

        self.image = self.spriteSheet.subsurface(
            pygame.Rect(0, 0, constante.ImagePersonnageWidth, constante.ImagePersonnageHeight))
        self.rect = pygame.Rect(0, 0, constante.ImagePersonnageWidth / 2, constante.ImagePersonnageWidth)
        self.rect.center = position
        self.health = constante.PersonnageHealth
        self.alive = True

        self.sens_personnage_droite = True

        self.isJump = False
        self.jumpCount = 10
        self.cooldownSuperPower = 0
        self.cooldownFire = 1

        self.numeroAnimation = 0
        self.numeroImage = 0
        self.flip = False

        self.fps = 0
        self.vitesse = 5

        all_sprite.add(self)

    def update(self):

        self.fps = self.fps + 16

        if self.fps >= constante.FpsAnimationLimite:
            self.fps = 0

            # recuperation du premier tableau dans le tableau animation puis le premier element du tableau premier
            # n : nombre

            n = player.animations[self.numeroAnimation][0] + self.numeroImage
            self.image = self.spriteSheet.subsurface(
                pygame.Rect(n % 10 * constante.ImagePersonnageWidth, n // 10 * constante.ImagePersonnageHeight,
                            constante.ImagePersonnageWidth, constante.ImagePersonnageHeight))
            if self.flip:
                self.image = pygame.transform.flip(self.image, True, False)

            self.numeroImage += 1

            if self.numeroImage == player.animations[self.numeroAnimation][1]:
                if player.animations[self.numeroAnimation][2]:
                    self.numeroImage = 0
                else:
                    self.numeroImage -= 1

    def setAnimation(self, n):
        if self.numeroAnimation != n:
            self.numeroImage = 0
            self.numeroAnimation = n

    def stand(self):
        self.setAnimation(0)

    def goRight(self):
        self.rect = self.rect.move(self.vitesse, 0)
        self.flip = False
        self.setAnimation(1)

    def goLeft(self):
        self.rect = self.rect.move(-self.vitesse, 0)
        self.flip = True
        self.setAnimation(1)

    def punch(self):
        self.setAnimation(2)

    def defence(self):
        self.setAnimation(3)

    def shoot(self, speed):
        if self.sens_personnage_droite is True:
            ball = Ball((self.rect.centerx + 40, self.rect.centery), speed, constante.BouleDeFeuImage, False)
        else:
            ball = Ball((self.rect.centerx - 40, self.rect.centery), speed, constante.BouleDeFeuImage, True)

        bullets.add(ball)

    def SuperPower(self, speed):
        if self.sens_personnage_droite is True:
            Superball = Ball((self.rect.centerx + 40, self.rect.centery), speed, constante.SuperBouleDeFeuImage, False)
        else:
            Superball = Ball((self.rect.centerx - 40, self.rect.centery), speed, constante.SuperBouleDeFeuImage, True)
        SuperPower.add(Superball)

    def Health_player_image(self, flip, coordonne_image):
        health_player_bar_image = healthBarImage(flip, coordonne_image)
        sprite_healthBar_image.add(health_player_bar_image)


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
        if self.rect.y > constante.ScreenWidth:
            self.kill()


class icon(pygame.sprite.Sprite):
    def __init__(self, image, coordonne):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = coordonne
        sprite_icon.add(self)


class healthBarImage(pygame.sprite.Sprite):
    def __init__(self, flip, coordonne_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(constante.HealthBarImage).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = coordonne_image
        if flip:
            self.image = pygame.transform.flip(self.image, True, False)


def background():
    image = pygame.image.load(constante.BackgroundImage)
    fenetre_fighter.blit(image, (0, 0))


def PowerBar(Allie_cooldownSuperPower, ennemie_cooldownSuperPower):
    if Allie_cooldownSuperPower > 10:
        Allie_cooldownSuperPower = 10
    pygame.draw.rect(fenetre_fighter, constante.bleu, (68, 36, (Allie_cooldownSuperPower * 123) / 10, 3))

    if ennemie_cooldownSuperPower > 10:
        ennemie_cooldownSuperPower = 10
    pygame.draw.rect(fenetre_fighter, constante.bleu, (650, 36, (ennemie_cooldownSuperPower * 123) / 10 * -1, 3))


def healthBarPlayer(Allie_health, ennemie_health):
    if Allie_health > 75:
        playerBarColor_Allie = Green
    elif Allie_health > 50:
        playerBarColor_Allie = Yellow
    elif Allie_health > 25:
        playerBarColor_Allie = Orange
    else:
        playerBarColor_Allie = Red

    if ennemie_health > 75:
        playerBarColor_ennemie = Green
    elif ennemie_health > 50:
        playerBarColor_ennemie = Yellow
    elif ennemie_health > 25:
        playerBarColor_ennemie = Orange
    else:
        playerBarColor_ennemie = Red
    pygame.draw.rect(fenetre_fighter, playerBarColor_Allie, (40, 23, ((Allie_health * 150) / 100 * 1), 9))
    pygame.draw.rect(fenetre_fighter, playerBarColor_ennemie, (675, 23, ((ennemie_health * 150) / 100 * -1), 9))


def mouvement(joueur, ennemie, leurre, gauche, droite, saut, tire, coup, bloc, hitFire, hitSuperPower):
    global directionSpeed
    if event.type == pygame.KEYDOWN and event.key is leurre or droite or gauche or saut or tire or coup:
        if gauche and joueur.rect.x > 1 and not bloc:
            joueur.goLeft()
        if droite and joueur.rect.x < constante.ScreenWidth - constante.ImagePersonnageWidth * 0.75 and not bloc:
            joueur.goRight()

        if event.type == pygame.KEYUP:
            if droite:
                joueur.sens_personnage_droite = True
            if gauche:
                joueur.sens_personnage_droite = False

        if joueur.sens_personnage_droite:
            directionSpeed = constante.vitesseDeplacement
        else:
            directionSpeed = -constante.vitesseDeplacement

        if not joueur.isJump:
            if saut:
                joueur.isJump = True

        # coup de poing#
        if joueur.cooldownFire >= 1 and coup:
            joueur.punch()
            joueur.cooldownFire -= 1
            if joueur.rect.colliderect(ennemie.rect):
                if ennemie.rect.x > 1 and ennemie.rect.x < constante.ScreenWidth - constante.ImagePersonnageWidth * 0.75:
                    ennemie.health -= constante.PersonnagePunch
                    ennemie.rect = ennemie.rect.move(directionSpeed * 3, 0)
                    joueur.cooldownSuperPower += constante.PersonnageCooldownPunch

        # boule de feu#
        if joueur.cooldownFire >= 1.5 and tire:
            joueur.shoot(directionSpeed)
            joueur.cooldownFire -= 2
        # Super Attaque#
        if tire and coup and joueur.cooldownSuperPower >= 10:
            joueur.SuperPower(directionSpeed)
            joueur.cooldownSuperPower = 0

    else:
        joueur.stand()
    if joueur.cooldownFire < 1.6:
        joueur.cooldownFire += 0.1
    # collision attaque distance#
    if bloc and hitFire:
        joueur.health -= 0
        joueur.defence()

    elif not bloc and hitFire:
        joueur.health -= constante.PersonnageFireBall
        ennemie.cooldownSuperPower += constante.PersonnageCooldownFireBall
        if joueur.rect.x > 10 and joueur.rect.x < 670:
            joueur.rect = joueur.rect.move(directionSpeed * 3, 0)

    if hitSuperPower:
        joueur.health -= constante.PersonnageSuperFireBall
    if joueur.health <= 0:
        joueur.alive = False
        joueur.kill()

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


def EndGame(playeur1Alive, playeur2Alive):
    if not playeur1Alive:
        image = pygame.image.load(constante.ImageVainqueurSquelette)
        fenetre_fighter.blit(image, (0, 0))
        pygame.mixer.music.stop
    if not playeur2Alive:
        image = pygame.image.load(constante.ImageVainqueurHeros)
        fenetre_fighter.blit(image, (0, 0))
        pygame.mixer.music.stop


# creation des groups
all_sprite = pygame.sprite.Group()
SuperPower = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemie = pygame.sprite.Group()
allie = pygame.sprite.Group()
sprite_icon = pygame.sprite.Group()
sprite_healthBar_image = pygame.sprite.Group()
sprite_healthBar = pygame.sprite.Group()

# creation du personnage
abi = player((100, 200), "image/heros1.png")
JC = player((600, 200), "image/skeletonBase.png")

# creation des logos des personnage
abi_Icon = icon("image/HeroIcon.png", (20, 25))
JC_Icon = icon("image/SkeletonIcon.png", (690, 25))

# creation de l'interface de la barre de vie
abi_healthbar_image = (False, (35, 25), abi.health)
JC_healthbar_image = (True, (650, 25), JC.health)

enemie.add(JC)
allie.add(abi)

pygame.display.flip()

launched = True
while launched:

    # pygame.time.Clock().tick(50)
    pygame.time.Clock().tick(1000)

    # touche de clavier

    key = pygame.key.get_pressed()
    Left1 = key[pygame.K_a]
    Right1 = key[pygame.K_d]
    Jump1 = key[pygame.K_w]
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

    sprite_healthBar.update()
    SuperPower.update()
    bullets.update()
    all_sprite.update()
    background()
    all_sprite.draw(fenetre_fighter)
    bullets.draw(fenetre_fighter)
    SuperPower.draw(fenetre_fighter)
    sprite_icon.draw(fenetre_fighter)
    sprite_healthBar_image.draw(fenetre_fighter)
    healthBarPlayer(abi.health, JC.health)
    PowerBar(abi.cooldownSuperPower, JC.cooldownSuperPower)
    EndGame(abi.alive, JC.alive)

    pygame.display.flip()
