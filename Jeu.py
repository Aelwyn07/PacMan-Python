from random import randint
import pygame, sys
import time
from pygame.locals import *
from random import randint
import pygame
pygame.init()


"""
        __init__:
        - points: le nombre de points durant la partie
        - perdu: permet de savoir si la partie est perdu ou pas
"""

class Jeu ():
    def __init__(self,fenetre):
        self.points=0
        self.perdu=False


    """
    show_score():
        méthode qui permet d'afficher le score
    """
    def show_score(self):
        police=pygame.font.SysFont("monospace",20)
        texte = "Score :"+ str(self.points)
        image_texte=police.render(texte, 1, (0,0,0))
        return image_texte


    """
    add_points():
        méthode qui permet d'ajouter un nombre de point défini a l'appelle de la
        commande
    """



    def add_points(self, points):
        self.points += points


    """
    win():
        méthode pour savoir si la partie est gagné a partir du nombre de
        pacgommes présent

    """
    def win (self,l_pac):
        if len(l_pac)==0:
            police_v=pygame.font.SysFont("monospace",50)
            texte_v = "WIN !!!!"
            image_texte_v=police_v.render(texte_v, 1, (255,0,0))
        else :
            police_v=pygame.font.SysFont("monospace",50)
            texte_v = " "
            image_texte_v=police_v.render(texte_v, 1, (255,0,0))
        return image_texte_v

    """
    loose():
        méthode pour savoir si la partie est perdu et qui modifie la variable
        perdu

    """

    def loose (self,col):
        txt=""
        police_l = pygame.font.SysFont("monospace",50)
        if col == True :
            txt = "LOOSE"
            self.perdu=True
        if self.perdu == True:
            txt = "LOOSE"
        image_texte_l = police_l.render(txt, 1, (255,0,0))
        return image_texte_l

