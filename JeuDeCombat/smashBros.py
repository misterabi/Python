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

pygame.init()
pygame.display.set_caption('SMASH BROS')
pygame.key.set_repeat(30, 30)

fenetre_smash_bros = pygame.display.set_mode((720, 480))

rectangle = pygame.Rect(0, 450, 720, 480)

fenetre_smash_bros.fill(bleu)

pygame.draw.rect(fenetre_smash_bros, black, rectangle)

joueur1 = pygame.image.load("image/heros1_base.png").convert()
fenetre_smash_bros.blit(joueur1,(50,245))
position_joueur1 = joueur1.get_rect()

joueur2 = pyjama.load("image/heros1_base.png").convert()
fenetre_smash_bros.blit(joueur2,(400,245))
position_joueur2 = joueur2.get_rect()



pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        if event.type == pygame.KEYDOWN:
     	    if event.key == pygame.K_LEFT:
                position_joueur1 = position_joueur1.move(-5,0)
     	    if event.key == pygame.K_RIGHT:
                position_joueur1 = position_joueur1.move(5,0)
     	    if event.key == pygame.K_UP:
                position_joueur1 = position_joueur1.move(0,-5)
     	    if event.key == pygame.K_DOWN:
                position_joueur1 = position_joueur1.move(0,5)

    fenetre_smash_bros.fill(bleu)
    pygame.draw.rect(fenetre_smash_bros, black, rectangle)
    fenetre_smash_bros.blit(joueur1, position_joueur1)
    pygame.display.flip()

# Ce code est à continuer...




