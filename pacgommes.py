import pygame
from pygame.locals import *

class PacGommes:
    """
    Classe PacGommes
    Données :
        fen : fenêtre dans laquelle est affichée pac-gomme
        x : abscisse de pac-gomme
        y : ordonnée de pac-gomme
        points : les points que rapporte la pac-gomme lorsqu'elle est mangée
        couleur : la couleur de la pac-gomme
    Résultat :
        Ne retourne rien, crée une nouvelle pac-gomme
        """
    def __init__(self, fen, x, y, points=10, couleur=(240, 240, 10)):
        self.fen = fen
        self.x = x
        self.y = y
        self.points = points
        self.couleur = couleur

    def dessiner(self):
        """
        Données : pas de paramètres dans cette méthode
        Résultats : Ne retourne rien, dessine la pac-gomme
        """
        pygame.draw.circle(self.fen, self.couleur, (self.x, self.y), 8, 0)

    def manger(self, pacman):
        """
        Données : objet permettant de connaître la position de Pac-Man
        Résultats : retourne Faux si la balle n'est pas à la même position que
        Pac-Man, sinon retourne le nombre de points de la balle pour l'ajouter
        au score
        """
        if pacman.xa <= self.x <= pacman.xb:
            if pacman.ya<=self.y<=pacman.yb:
                return self.points
        return False
