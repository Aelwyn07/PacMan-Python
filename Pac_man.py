from random import randint
import pygame, sys
import time
from pygame.locals import *
from random import randint
import pygame
pygame.init()


ecran =640, 480
pygame.display.init()
fenetre = pygame.display.set_mode(ecran)
fenetre.fill([0,0,0])
all_mur=[((100,100),(150,150)),((200,100),(250,150))]


class Pac_man :
    """
    données:
        écran: la taille de l'écran
        xa et ya: la position en haut a gauche de la hitbox du pac man
        xb et yb: la position en bas a droite de la hitbox du pac man
        dx et dy: les variables de mouvement / direction
        color : la couleur du pacman (va etre modifié a terme par une image)
        taille: la longueur d'un coté du pac man

    """
    def __init__(self, ecran,taille,fenetre,all_mur):  #ajouter la liste des coordonées des murs
        self.xa = ecran[0]/2-taille / 2
        self.ya =ecran[1]/2-taille / 2
        self.xb =self.xa+taille
        self.yb =self.ya+taille
        self.dx = 0
        self.dy = 0
        self.color = (0,255,0)
        self.taille=taille
        self.all_mur=all_mur
        self.fenetre=fenetre

        """
        La méthode draw permet de dessiner le pac man sur l'écran
        """


    def draw(self):
        pac=self.rot_image()
        pac=pygame.transform.scale(pac, (self.taille, self.taille))
        return pac

        """
        Les méthode move_... permettent de modifier les variables dx et dy de
        direction.
        """

    def rot_image(self):
        if self.dy==0 and self.dx==0 :
            return pygame.image.load("pac_man.png").convert_alpha()
        if self.dy==2 and self.dx==0 :
            return pygame.image.load("pac_man_bas.png").convert_alpha()
        if self.dy==-2 and self.dx==0 :
            return pygame.image.load("pac_man_haut.png").convert_alpha()
        if self.dy==0 and self.dx==-2 :
            return pygame.image.load("pac_man_gauche.png").convert_alpha()
        if self.dy==0 and self.dx==2 :
            return pygame.image.load("pac_man.png").convert_alpha()

    def move_b(self):
        self.dy = 2
        self.dx = 0
    def move_h(self):
        self.dy = -2
        self.dx = 0
    def move_l(self):
        self.dx = -2
        self.dy = 0
    def move_r(self):
        self.dx = 2
        self.dy = 0

        """
        # la methode dir permet de savoir quel touche est appuyer et changer dx et
        dy grace aux fonction move_...
        """
    def dir (self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.move_b()
            elif event.key == pygame.K_RIGHT:
                self.move_r()
            elif event.key == pygame.K_LEFT:
                self.move_l()
            elif event.key == pygame.K_UP:
                self.move_h()
            elif event.key == pygame.K_DOWN:
                self.move_b()

        """
        La méthode colision permet de savoir si il y a une colision avec un mur
        dans le labyrinthe et si colision il y a, change les variables dx et dy
        pour que le pac man ne bouge plus
        """

    def colision(self):
        for i in range (len(self.all_mur)):
            a,b=self.all_mur[i]
            mur_xa, mur_ya=a
            mur_xb, mur_yb=b
            if mur_xa<=self.xa+self.dx<=mur_xb or mur_xb>=self.xb +self.dx>=mur_xa:
                if mur_ya<=self.ya+self.dy<=mur_yb or mur_yb>=self.yb +self.dy>=mur_ya:
                    self.dy = 0
                    self.dx = 0
            if self.xa+self.dx<=mur_xa<=self.xb +self.dx or self.xa+self.dx<=mur_xb<=self.xb +self.dx:
                if self.ya+self.dy<=mur_ya<=self.yb +self.dy or self.ya+self.dy<=mur_yb<=self.yb +self.dy:
                    self.dy = 0
                    self.dx = 0


    """
    La méthode move permet de modifié la position du pac man selon le variables
    de mouvement dx et dy
    """
    def move (self):
        self.xa += self.dx
        self.ya += self.dy
        self.xb += self.dx
        self.yb += self.dy






