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

bleu = (14, 180, 245)
black = (0, 0, 0)
white=(255,255,255)
pygame.init()
pygame.display.set_caption('SMASH BROS')
pygame.key.set_repeat(30, 30)

fenetre_smash_bros = pygame.display.set_mode((720, 480))

rectangle = pygame.Rect(0, 450, 720, 480)

fenetre_smash_bros.fill(bleu)

pygame.draw.rect(fenetre_smash_bros, black, rectangle)

joueur1 = pygame.image.load("image/heros1_marche1D.png").convert()
position_joueur1 = joueur1.get_rect()
position_joueur1.center= 100,398
fenetre_smash_bros.blit(joueur1,position_joueur1)
joueur1.set_colorkey(white)

joueur2 = pygame.image.load("image/heros1_marche1G.png").convert()
position_joueur2 = joueur2.get_rect()
position_joueur2.center= 350,398
fenetre_smash_bros.blit(joueur2, position_joueur2)
joueur2.set_colorkey(white)

pygame.display.flip()

launched = True
while launched:
    #limitation de la boucle
    pygame.time.Clock().tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and position_joueur2.x > 1 :
        position_joueur2 = position_joueur2.move(-5, 0)
    if key[pygame.K_d] and position_joueur2.x < 685:
        position_joueur2 = position_joueur2.move(5, 0)
    if key[pygame.K_w] and position_joueur2.y > 0:
        position_joueur2 = position_joueur2.move(0, -5)
    if key[pygame.K_s] and position_joueur2.y <348:
        position_joueur2 = position_joueur2.move(0, 5)

    if key[pygame.K_LEFT] and position_joueur1.x > 1 :
        position_joueur1 = position_joueur1.move(-5, 0)
    if key[pygame.K_RIGHT] and position_joueur1.x < 685:
        position_joueur1 = position_joueur1.move(5, 0)
    if key[pygame.K_UP] and position_joueur1.y > 0:
        position_joueur1 = position_joueur1.move(0, -5)
    if key[pygame.K_DOWN] and position_joueur1.y <348:
        position_joueur1 = position_joueur1.move(0, 5)

    fenetre_smash_bros.fill(bleu)
    pygame.draw.rect(fenetre_smash_bros, black, rectangle)
    fenetre_smash_bros.blit(joueur1, position_joueur1)
    fenetre_smash_bros.blit(joueur2, position_joueur2)
    pygame.display.flip()
