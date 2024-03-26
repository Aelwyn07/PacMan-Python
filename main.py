import pygame
from Pac_man import Pac_man
from pacgommes import PacGommes
from labyrinthe import Mur
from pygame.locals import *
from fantome3 import Fantome
from Jeu import Jeu
import time
import random

pygame.init()
ecran = 1000, 1000
screen = pygame.display.set_mode((ecran))

longueur_lab = 700
largeur_lab = 450
x_lab = 100
y_lab = 100

# Crée toutes les PacGommes
liste_pacgommes = []
x_vert = random.randrange(y_lab+25, y_lab+longueur_lab, 50)
y_vert = random.randrange(y_lab+25, y_lab+largeur_lab, 50)
for x in range(y_lab+25, y_lab+longueur_lab, 50):
    for y in range(y_lab+25, y_lab+largeur_lab, 50):
        if x == x_vert and y == y_vert:
            liste_pacgommes.append(PacGommes(screen, x, y, 50, (5, 255, 5)))
        else:
            liste_pacgommes.append(PacGommes(screen, x, y))

def creation_mur():
    """ Fonction stockant les coordonnées des murs dans une liste"""
    # Bordure
    for x in range(x_lab, longueur_lab+x_lab, 50):
        liste_murs.append([(x, y_lab-2), (x+50, y_lab+2)])
        liste_murs.append([(x, y_lab+largeur_lab-2), (x+50, y_lab+largeur_lab+2)])
    for y in range(y_lab, largeur_lab+y_lab, 50):
        liste_murs.append([(x_lab-2, y), (x_lab+2, y+50)])
        liste_murs.append([(x_lab+longueur_lab-2, y), (x_lab+longueur_lab+2, y+50)])

    # Murs horizontaux
    liste_murs.append([(100, 148), (150, 152)])
    liste_murs.append([(150, 148), (200, 152)])
    liste_murs.append([(400, 148), (450, 152)])
    liste_murs.append([(450, 148), (500, 152)])
    liste_murs.append([(650, 148), (700, 152)])
    liste_murs.append([(750, 148), (800, 152)])
    liste_murs.append([(300, 198), (350, 202)])
    liste_murs.append([(350, 198), (400, 202)])
    liste_murs.append([(550, 248), (600, 252)])
    liste_murs.append([(750, 248), (800, 252)])
    for x in range(150, 500, 50):
        liste_murs.append([(x, 298), (x+50, 302)])
    liste_murs.append([(500, 348), (550, 352)])
    liste_murs.append([(550, 348), (600, 352)])
    liste_murs.append([(300, 398), (350, 402)])
    liste_murs.append([(350, 398), (400, 402)])
    liste_murs.append([(700, 398), (750, 402)])
    liste_murs.append([(750, 398), (800, 402)])
    liste_murs.append([(100, 448), (150, 452)])
    liste_murs.append([(200, 498), (250, 502)])
    liste_murs.append([(250, 498), (300, 502)])
    liste_murs.append([(400, 498), (450, 502)])
    liste_murs.append([(600, 498), (650, 502)])

    # Murs verticaux
    liste_murs.append([(148, 350), (152, 400)])
    liste_murs.append([(148, 400), (152, 450)])
    liste_murs.append([(198, 150), (202, 200)])
    liste_murs.append([(198, 200), (202, 250)])
    liste_murs.append([(248, 150), (252, 200)])
    liste_murs.append([(248, 350), (252, 400)])
    liste_murs.append([(248, 400), (252, 450)])
    liste_murs.append([(248, 500), (252, 550)])
    liste_murs.append([(298, 300), (302, 350)])
    liste_murs.append([(298, 350), (302, 400)])
    liste_murs.append([(398, 150), (402, 200)])
    liste_murs.append([(398, 200), (402, 250)])
    liste_murs.append([(448, 350), (452, 400)])
    liste_murs.append([(448, 400), (452, 450)])
    for y in range(200, 350, 50):
        liste_murs.append([(498, y), (502, y+50)])
    liste_murs.append([(598, 200), (602, 250)])
    liste_murs.append([(598, 250), (602, 300)])
    liste_murs.append([(598, 400), (602, 450)])
    liste_murs.append([(598, 450), (602, 500)])
    liste_murs.append([(648, 150), (652, 200)])
    liste_murs.append([(698, 300), (702, 350)])
    liste_murs.append([(698, 350), (702, 400)])
    liste_murs.append([(748, 200), (752, 250)])
    liste_murs.append([(748, 250), (752, 300)])
    liste_murs.append([(748, 400), (752, 450)])

# Crée les murs du labyrinthe
liste_murs = []
creation_mur()
murs = []
for elt in liste_murs:
    murs.append(Mur(screen, elt[0][0], elt[0][1], elt[1][0], elt[1][1]))

jeu=Jeu(screen)
# Création de Pac-Man
pac_man = Pac_man(ecran,30,screen,liste_murs)

# Création des fantômes
fantome1 = Fantome(liste_murs,"fantome_haut.png","fantome_bas.png","fantome_droite.png","fantome_gauche.png",(225,425))
fantome2 = Fantome(liste_murs,"fantome_haut_r.png","fantome_bas_r.png","fantome_droite_r.png","fantome_gauche_r.png",(225, 225))
fantome3 = Fantome(liste_murs,"fantome_haut_b.png","fantome_bas_b.png","fantome_droite_b.png","fantome_gauche_b.png",(625,425))

run=True

while run:
    screen.fill((255, 255, 255))

    pac_man.draw()

    for m in murs:
        m.dessiner()
    i = 0
    for elt in liste_pacgommes:
        elt.dessiner()
        if elt.manger(pac_man) != False:
            liste_pacgommes.pop(i)
            if jeu.perdu == False:
                jeu.add_points(10)
        i += 1
    fantome1.move()
    fantome2.move()
    fantome3.move()


    screen.blit(jeu.win(liste_pacgommes),(ecran[0]/2 , 5))
    screen.blit(jeu.loose(fantome1.collision_pacman(pac_man)),(ecran[0]/2 , 5))
    screen.blit(jeu.loose(fantome2.collision_pacman(pac_man)),(ecran[0]/2 , 5))
    screen.blit(jeu.loose(fantome3.collision_pacman(pac_man)),(ecran[0]/2 , 5))
    screen.blit(pac_man.draw(), (pac_man.xa,pac_man.ya))
    screen.blit(jeu.show_score(), (10,10))
    screen.blit(fantome1.image, fantome1.fantome_rect)
    screen.blit(fantome2.image, fantome2.fantome_rect)
    screen.blit(fantome3.image, fantome3.fantome_rect)
    pygame.display.update()

    for event in pygame.event.get():
        pac_man.dir(event)
        if event.type == pygame.QUIT:
            run = False
    pac_man.colision()
    pac_man.move()

    time.sleep(0.001)
pygame.quit()
