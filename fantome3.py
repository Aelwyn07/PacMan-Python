import random
import pygame
import time


class Fantome:
    """
    __init__:
        - x et y: sont les abscisses / ordonnées
        - adx et ady: vitesse du fantome
        - image: récupère l'image du fantome
        - fantome_rect: rectangle autour de l'image pour faciliter les déplacements
        - nombre: servira pour la fonction move()
        - deplacement: peut varier de 1 à 4, représentent les directions (dans l'ordre: haut / bas / droite / gauche)
    """

    def __init__(self, murs, image1, image2, image3, image4, point_apparition):

        self.x = point_apparition[0]
        self.y = point_apparition[1]
        self.adx = 2
        self.ady = 2
        self.image = pygame.image.load(image1)
        self.fantome_rect = self.image.get_rect()
        self.all_mur = murs
        self.deplacement = 1
        self.nombre = 0
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3
        self.image4 = image4
        self.fantome_rect.center = point_apparition[0], point_apparition[1]

    """
     La méthode move():
        - permet de selectionner l'un des 4 moyens de déplacements possibles.
        - variable nombre: permet de regarder régulièrement ou sont les murs seulement quand le fantôme
        se trouve "dans une case" (tout les 50 pixels).
        - liste: stocke les directions possibles que peut emprunter le fantôme
    """

    def move(self):
        if self.nombre == 25:
            self.nombre = 0
            liste = []
            if self.deplacement == 1:
                if self.collision_mur_haut() == False:
                    liste.append(1)
                if self.collision_mur_droite() == False:
                    liste.append(3)
                if self.collision_mur_gauche() == False:
                    liste.append(4)
                if liste == []:
                    self.deplacement = 2
                else:
                    a = random.randint(0, len(liste)-1)
                    self.deplacement = liste[a]

            elif self.deplacement == 2:
                if self.collision_mur_bas() == False:
                    liste.append(2)
                if self.collision_mur_droite() == False:
                    liste.append(3)
                if self.collision_mur_gauche() == False:
                    liste.append(4)
                if liste == []:
                    self.deplacement = 1
                else:
                    a = random.randint(0, len(liste)-1)
                    self.deplacement = liste[a]

            elif self.deplacement == 3:
                if self.collision_mur_droite() == False:
                    liste.append(3)
                if self.collision_mur_haut() == False:
                    liste.append(1)
                if self.collision_mur_bas() == False:
                    liste.append(2)
                if liste == []:
                    self.deplacement = 4
                else:
                    a = random.randint(0, len(liste)-1)
                    self.deplacement = liste[a]

            elif self.deplacement == 4:
                if self.collision_mur_gauche() == False:
                    liste.append(4)
                if self.collision_mur_haut() == False:
                    liste.append(1)
                if self.collision_mur_bas() == False:
                    liste.append(2)
                if liste == []:
                    self.deplacement = 3
                else:
                    a = random.randint(0, len(liste)-1)
                    self.deplacement = liste[a]


        if self.deplacement == 2:
            self.image = pygame.image.load(self.image2)
            self.move_down()
        if self.deplacement == 1:
            self.image = pygame.image.load(self.image1)
            self.move_up()
        if self.deplacement == 4:
            self.image = pygame.image.load(self.image4)
            self.move_left()
        if self.deplacement == 3:
            self.image = pygame.image.load(self.image3)
            self.move_right()
        self.nombre = self.nombre + 1

    """
    Les méthodes move_up / move_down / move_left / move_right:
        - si appelé par move(), déplace le fantome dans une direction définie.
        - les coordonnées x et y sont aussi actualiser.
    """

    def move_down(self):
        self.y = self.y + self.ady
        self.fantome_rect = self.fantome_rect.move(0, self.ady)


    def move_up(self):
        self.y = self.y - self.ady
        self.fantome_rect = self.fantome_rect.move(0, - self.ady)


    def move_left(self):
        self.x = self.x - self.adx
        self.fantome_rect = self.fantome_rect.move( - self.adx,0)

    def move_right(self):
        self.x = self.x + self.adx
        self.fantome_rect = self.fantome_rect.move(self.adx ,0)

    """
    les méthodes collision_mur haut / droite / gauche / bas:
        - permet de savoir ou se situe les murs pour empêcher le fantome
        de les traverser.
        - on regarde si la projection du point du fantome dans une direction a une
        distance précise est situé dans un mur (return True) ou non (return False).
    """
    def collision_mur_haut(self):
        for i in range (len(self.all_mur)):
            mur_xa = self.all_mur[i][0][0]
            mur_ya = self.all_mur[i][0][1]
            mur_xb = self.all_mur[i][1][0]
            mur_yb = self.all_mur[i][1][1]
            if (mur_xa <= self.x <= mur_xb) and (mur_ya <= self.y - 27 <= mur_yb):
                return True

        return False


    def collision_mur_bas(self):
        for i in range (len(self.all_mur)):
            mur_xa = self.all_mur[i][0][0]
            mur_ya = self.all_mur[i][0][1]
            mur_xb = self.all_mur[i][1][0]
            mur_yb = self.all_mur[i][1][1]
            if  (mur_xa <= self.x <= mur_xb) and (mur_ya <= self.y + 27 <= mur_yb):
                return True
        return False


    def collision_mur_droite(self):
        for i in range (len(self.all_mur)):
            mur_xa = self.all_mur[i][0][0]
            mur_ya = self.all_mur[i][0][1]
            mur_xb = self.all_mur[i][1][0]
            mur_yb = self.all_mur[i][1][1]
            if (mur_xa <= self.x + 26 <= mur_xb) and (mur_ya <= self.y <= mur_yb):
                return True
        return False


    def collision_mur_gauche(self):
        for i in range (len(self.all_mur)):
            mur_xa = self.all_mur[i][0][0]
            mur_ya = self.all_mur[i][0][1]
            mur_xb = self.all_mur[i][1][0]
            mur_yb = self.all_mur[i][1][1]
            if (mur_xa <= self.x - 26 <= mur_xb) and (mur_ya <= self.y <= mur_yb):
                return True
        return False
    """
    la méthode collision_pacman:
        - importe les coordonées du pacman.
        - si les coordonées du pacman entourent celles du fantome, on actualise fin qui
        met fin à la partie.
    """
    def collision_pacman(self, pacman):
        if pacman.xa <= self.x <= pacman.xb:
            if pacman.ya <= self.y <= pacman.yb:
                fin = True
                return fin


