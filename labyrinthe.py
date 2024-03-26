import pygame
from pygame.locals import *

class Mur:
    """
    Classe Mur
    Données :
        fen : fenêtre dans laquelle est affichée le mur
        xa : abscisse du mur en haut à gauche
        ya : ordonnée du mur en haut à gauche
        xb : abscisse du mur en bas à droite
        yb : ordonnée du mur en bas à droite
        self.rect : rectangle noir représentant le mur
    Résultat :
        Ne retourne rien, crée un nouveau mur
        """
    def __init__(self, fen, xa, ya, xb, yb):
        self.fen = fen
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.rect = Rect(self.xa, self.ya, self.xb-self.xa, self.yb-self.ya)

    def dessiner(self):
        """
        Données : méthode sans paramètres
        Résultat : Ne retourne rien, dessine le mur"""
        pygame.draw.rect(self.fen, (0,0,0), self.rect)
