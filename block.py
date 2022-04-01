import pygame
from pygame.locals import *


fichier_level = open('fichier/level.txt', mode='r+')
level = int(fichier_level.readline())


class Block(pygame.sprite.Sprite):
    def __init__(self, game):
        #variables du jeu
        super().__init__()
        self.v = 0
        self.x = None
        self.boucle = 0
        self.velocity = 1
        self.game = game
        self.image = pygame.image.load("assets/Idle.png")
        self.rect = self.image.get_rect()
        self.tab = []
        self.i = 0
        self.nob = 0
        self.coucou = 0
        if self.game.monde==1: #image du monde 1
            #importe les images de terre
             self.haut = pygame.image.load("assets/terre/TileSet_16.png")
             self.bas = pygame.image.load("assets/terre/TileSet_0002.png")
             self.tout = pygame.image.load("assets/terre/TileSet_09.png")
             self.gauche_haut = pygame.image.load("assets/terre/TileSet_34.png")
             self.droit_haut = pygame.image.load("assets/terre/TileSet_33.png")
             self.gauche_bas = pygame.image.load("assets/terre/TileSet_17.png")
             self.droit_bas = pygame.image.load("assets/terre/TileSet_15.png")
             self.droite = pygame.image.load("assets/terre/TileSet_10.png")
             self.gauche = pygame.image.load("assets/terre/TileSet_08.png")
             self.gauche1 = pygame.image.load("assets/terre/TileSet_017 - Copie.png")
             self.droite1 = pygame.image.load("assets/terre/TileSet_017.png")
             self.entourer = pygame.image.load("assets/terre/TileSet_002.png")
             self.entourer = pygame.transform.scale(self.entourer, (64, 64))
             self.gauche1 = pygame.transform.scale(self.gauche1, (64, 64))
             self.droite1 = pygame.transform.scale(self.droite1, (64, 64))
             self.haut = pygame.transform.scale(self.haut, (64, 64))
             self.bas = pygame.transform.scale(self.bas, (64, 64))
             self.tout = pygame.transform.scale(self.tout, (64, 64))
             self.gauche_haut = pygame.transform.scale(self.gauche_haut, (64, 64))
             self.gauche_bas = pygame.transform.scale(self.gauche_bas, (64, 64))
             self.droit_bas = pygame.transform.scale(self.droit_bas, (64, 64))
             self.droit_haut = pygame.transform.scale(self.droit_haut, (64, 64))
             self.droite = pygame.transform.scale(self.droite, (64, 64))
             self.gauche = pygame.transform.scale(self.gauche, (64, 64))

            #importe les images d'eau et creer la liste
             self.wather1 = pygame.image.load("assets/eau/Water1.png")
             self.wather2 = pygame.image.load("assets/eau/Water2.png")
             self.wather3 = pygame.image.load("assets/eau/Water3.png")
             self.wather4 = pygame.image.load("assets/eau/Water4.png")
             self.wather5 = pygame.image.load("assets/eau/Water5.png")
             self.wather6 = pygame.image.load("assets/eau/Water6.png")
             self.wather7 = pygame.image.load("assets/eau/Water7.png")
             self.wather8 = pygame.image.load("assets/eau/Water8.png")
             self.wather1 = pygame.transform.scale2x(self.wather1)
             self.wather2 = pygame.transform.scale2x(self.wather2)
             self.wather3 = pygame.transform.scale2x(self.wather3)
             self.wather4 = pygame.transform.scale2x(self.wather4)
             self.wather5 = pygame.transform.scale2x(self.wather5)
             self.wather6 = pygame.transform.scale2x(self.wather6)
             self.wather7 = pygame.transform.scale2x(self.wather7)
             self.wather8 = pygame.transform.scale2x(self.wather8)
             self.watherframe = [self.wather1, self.wather1, self.wather2, self.wather2, self.wather3, self.wather3,
                                 self.wather4, self.wather4, self.wather5, self.wather5, self.wather6, self.wather6,
                                 self.wather7, self.wather7, self.wather8, self.wather8]
             self.watherindex = 0

             
        if self.game.monde == 2:#image du monde 2
            #terre du monde 2
            self.haut = pygame.image.load("assets/lave/TileSet_16.png")
            self.bas = pygame.image.load("assets/lave/TileSet_0002.png")
            self.tout = pygame.image.load("assets/lave/TileSet_09.png")
            self.gauche_haut = pygame.image.load("assets/lave/TileSet_34.png")
            self.droit_haut = pygame.image.load("assets/lave/TileSet_33.png")
            self.gauche_bas = pygame.image.load("assets/lave/TileSet_17.png")
            self.droit_bas = pygame.image.load("assets/lave/TileSet_15.png")
            self.droite = pygame.image.load("assets/lave/TileSet_10.png")
            self.gauche = pygame.image.load("assets/lave/TileSet_08.png")
            self.gauche1 = pygame.image.load("assets/lave/TileSet_017 - Copie.png")
            self.droite1 = pygame.image.load("assets/lave/TileSet_017.png")
            self.entourer = pygame.image.load("assets/lave/TileSet_002.png")
            self.entourer = pygame.transform.scale(self.entourer, (64, 64))
            self.gauche1 = pygame.transform.scale(self.gauche1, (64, 64))
            self.droite1 = pygame.transform.scale(self.droite1, (64, 64))
            self.haut = pygame.transform.scale(self.haut, (64, 64))
            self.bas = pygame.transform.scale(self.bas, (64, 64))
            self.tout = pygame.transform.scale(self.tout, (64, 64))
            self.gauche_haut = pygame.transform.scale(self.gauche_haut, (64, 64))
            self.gauche_bas = pygame.transform.scale(self.gauche_bas, (64, 64))
            self.droit_bas = pygame.transform.scale(self.droit_bas, (64, 64))
            self.droit_haut = pygame.transform.scale(self.droit_haut, (64, 64))
            self.droite = pygame.transform.scale(self.droite, (64, 64))
            self.gauche = pygame.transform.scale(self.gauche, (64, 64))

            #eau du monde 2 : lave
            self.wather1 = pygame.image.load("assets/lave/lava/lava1.png")
            self.wather2 = pygame.image.load("assets/lave/lava/lava2.png")
            self.wather3 = pygame.image.load("assets/lave/lava/lava3.png")
            self.wather4 = pygame.image.load("assets/lave/lava/lava4.png")
            self.wather5 = pygame.image.load("assets/lave/lava/lava5.png")
            self.wather6 = pygame.image.load("assets/lave/lava/lava6.png")
            self.wather7 = pygame.image.load("assets/lave/lava/lava7.png")
            self.wather8 = pygame.image.load("assets/lave/lava/lava8.png")
            self.wather9 = pygame.image.load("assets/lave/lava/lava9.png")
            self.wather10 = pygame.image.load("assets/lave/lava/lava10.png")
            self.wather11 = pygame.image.load("assets/lave/lava/lava11.png")
            self.wather12 = pygame.image.load("assets/lave/lava/lava12.png")
            self.wather13 = pygame.image.load("assets/lave/lava/lava13.png")
            self.wather14 = pygame.image.load("assets/lave/lava/lava14.png")
            self.wather15 = pygame.image.load("assets/lave/lava/lava15.png")
            self.wather16 = pygame.image.load("assets/lave/lava/lava16.png")
            self.wather1 = pygame.transform.scale2x(self.wather1)
            self.wather2 = pygame.transform.scale2x(self.wather2)
            self.wather3 = pygame.transform.scale2x(self.wather3)
            self.wather4 = pygame.transform.scale2x(self.wather4)
            self.wather5 = pygame.transform.scale2x(self.wather5)
            self.wather6 = pygame.transform.scale2x(self.wather6)
            self.wather7 = pygame.transform.scale2x(self.wather7)
            self.wather8 = pygame.transform.scale2x(self.wather8)
            self.wather9 = pygame.transform.scale2x(self.wather9)
            self.wather10 = pygame.transform.scale2x(self.wather10)
            self.wather11 = pygame.transform.scale2x(self.wather11)
            self.wather12 = pygame.transform.scale2x(self.wather12)
            self.wather13 = pygame.transform.scale2x(self.wather13)
            self.wather14 = pygame.transform.scale2x(self.wather14)
            self.wather15 = pygame.transform.scale2x(self.wather15)
            self.wather16 = pygame.transform.scale2x(self.wather16)
            self.watherframe = [self.wather1,self.wather1, self.wather2,self.wather2, self.wather3,self.wather3, self.wather4,self.wather4, self.wather5,self.wather5, self.wather6,self.wather6,
                                self.wather7,self.wather7, self.wather8,self.wather8, self.wather9,self.wather9, self.wather10,self.wather10, self.wather11,self.wather11, self.wather12,self.wather12,
                                self.wather13,self.wather13, self.wather14,self.wather14, self.wather15,self.wather15, self.wather16,self.wather16]
            self.watherindex = 0


        if self.game.monde == 3:#monde 3
            #importation des image de la terre du monde 3
            self.haut = pygame.image.load("assets/ice/TileSet_16.png")
            self.bas = pygame.image.load("assets/ice/TileSet_0002.png")
            self.tout = pygame.image.load("assets/ice/TileSet_09.png")
            self.gauche_haut = pygame.image.load("assets/ice/TileSet_34.png")
            self.droit_haut = pygame.image.load("assets/ice/TileSet_33.png")
            self.gauche_bas = pygame.image.load("assets/ice/TileSet_17.png")
            self.droit_bas = pygame.image.load("assets/ice/TileSet_15.png")
            self.droite = pygame.image.load("assets/ice/TileSet_10.png")
            self.gauche = pygame.image.load("assets/ice/TileSet_08.png")
            self.gauche1 = pygame.image.load("assets/ice/TileSet_017 - Copie.png")
            self.droite1 = pygame.image.load("assets/ice/TileSet_017.png")
            self.entourer = pygame.image.load("assets/ice/TileSet_002.png")
            self.entourer = pygame.transform.scale(self.entourer, (64, 64))
            self.gauche1 = pygame.transform.scale(self.gauche1, (64, 64))
            self.droite1 = pygame.transform.scale(self.droite1, (64, 64))
            self.haut = pygame.transform.scale(self.haut, (64, 64))
            self.bas = pygame.transform.scale(self.bas, (64, 64))
            self.tout = pygame.transform.scale(self.tout, (64, 64))
            self.gauche_haut = pygame.transform.scale(self.gauche_haut, (64, 64))
            self.gauche_bas = pygame.transform.scale(self.gauche_bas, (64, 64))
            self.droit_bas = pygame.transform.scale(self.droit_bas, (64, 64))
            self.droit_haut = pygame.transform.scale(self.droit_haut, (64, 64))
            self.droite = pygame.transform.scale(self.droite, (64, 64))
            self.gauche = pygame.transform.scale(self.gauche, (64, 64))


            #importe les image de l'eau du monde 3
            self.wather1 = pygame.image.load("assets/eau/w/Water1.png")
            self.wather2 = pygame.image.load("assets/eau/w/Water2.png")
            self.wather3 = pygame.image.load("assets/eau/w/Water3.png")
            self.wather4 = pygame.image.load("assets/eau/w/Water4.png")
            self.wather5 = pygame.image.load("assets/eau/w/Water5.png")
            self.wather6 = pygame.image.load("assets/eau/w/Water6.png")
            self.wather7 = pygame.image.load("assets/eau/w/Water7.png")
            self.wather8 = pygame.image.load("assets/eau/w/Water8.png")
            self.wather1 = pygame.transform.scale2x(self.wather1)
            self.wather2 = pygame.transform.scale2x(self.wather2)
            self.wather3 = pygame.transform.scale2x(self.wather3)
            self.wather4 = pygame.transform.scale2x(self.wather4)
            self.wather5 = pygame.transform.scale2x(self.wather5)
            self.wather6 = pygame.transform.scale2x(self.wather6)
            self.wather7 = pygame.transform.scale2x(self.wather7)
            self.wather8 = pygame.transform.scale2x(self.wather8)
            self.watherframe = [self.wather1, self.wather1, self.wather2, self.wather2, self.wather3, self.wather3,
                                self.wather4, self.wather4, self.wather5, self.wather5, self.wather6, self.wather6,
                                self.wather7, self.wather7, self.wather8, self.wather8]
            self.watherindex = 0

            
        if self.game.monde == 4:#monde 4
            #importation des images du monde 4 de terre
            self.haut = pygame.image.load("assets/cave/TileSet_16.png")
            self.bas = pygame.image.load("assets/cave/TileSet_0002.png")
            self.tout = pygame.image.load("assets/cave/TileSet_9.png")
            self.gauche_haut = pygame.image.load("assets/cave/TileSet_34.png")
            self.droit_haut = pygame.image.load("assets/cave/TileSet_33.png")
            self.gauche_bas = pygame.image.load("assets/cave/TileSet_17.png")
            self.droit_bas = pygame.image.load("assets/cave/TileSet_15.png")
            self.droite = pygame.image.load("assets/cave/TileSet_10.png")
            self.gauche = pygame.image.load("assets/cave/TileSet_08.png")
            self.gauche1 = pygame.image.load("assets/cave/TileSet_017 - Copie.png")
            self.droite1 = pygame.image.load("assets/cave/TileSet_017.png")
            self.entourer = pygame.image.load("assets/cave/TileSet_002.png")
            self.entourer = pygame.transform.scale(self.entourer, (64, 64))
            self.gauche1 = pygame.transform.scale(self.gauche1, (64, 64))
            self.droite1 = pygame.transform.scale(self.droite1, (64, 64))
            self.haut = pygame.transform.scale(self.haut, (64, 64))
            self.bas = pygame.transform.scale(self.bas, (64, 64))
            self.tout = pygame.transform.scale(self.tout, (64, 64))
            self.gauche_haut = pygame.transform.scale(self.gauche_haut, (64, 64))
            self.gauche_bas = pygame.transform.scale(self.gauche_bas, (64, 64))
            self.droit_bas = pygame.transform.scale(self.droit_bas, (64, 64))
            self.droit_haut = pygame.transform.scale(self.droit_haut, (64, 64))
            self.droite = pygame.transform.scale(self.droite, (64, 64))
            self.gauche = pygame.transform.scale(self.gauche, (64, 64))


            #importation des images du monde 4 d'eau
            self.wather1 = pygame.image.load("assets/eau/w/Water1.png")
            self.wather2 = pygame.image.load("assets/eau/w/Water2.png")
            self.wather3 = pygame.image.load("assets/eau/w/Water3.png")
            self.wather4 = pygame.image.load("assets/eau/w/Water4.png")
            self.wather5 = pygame.image.load("assets/eau/w/Water5.png")
            self.wather6 = pygame.image.load("assets/eau/w/Water6.png")
            self.wather7 = pygame.image.load("assets/eau/w/Water7.png")
            self.wather8 = pygame.image.load("assets/eau/w/Water8.png")
            self.wather1 = pygame.transform.scale2x(self.wather1)
            self.wather2 = pygame.transform.scale2x(self.wather2)
            self.wather3 = pygame.transform.scale2x(self.wather3)
            self.wather4 = pygame.transform.scale2x(self.wather4)
            self.wather5 = pygame.transform.scale2x(self.wather5)
            self.wather6 = pygame.transform.scale2x(self.wather6)
            self.wather7 = pygame.transform.scale2x(self.wather7)
            self.wather8 = pygame.transform.scale2x(self.wather8)
            self.watherframe = [self.wather1, self.wather1, self.wather2, self.wather2, self.wather3, self.wather3,
                                self.wather4, self.wather4, self.wather5, self.wather5, self.wather6, self.wather6,
                                self.wather7, self.wather7, self.wather8, self.wather8]
            self.watherindex = 0


    def check(self, x, y, nb, fonction, v):
        if v == 0:
            l = 0
            n = 0

            if nb[2] == 999:
                self.remove()
            for player in self.game.check_collision(self, self.game.all_players):
                for i in range(len(self.game.blocktab)):
                    if self.game.player.rect.x + nb[2] + 50 > self.game.blocktab[i][
                        0] and not self.game.player.rect.x >= self.game.blocktab[i][
                        0] + 10 and self.game.player.rect.y + self.game.player.rect.height > self.game.blocktab[i][
                        1] + 1 and self.game.player.rect.y < self.game.blocktab[i][1] + self.game.blocktab[i][3] - 1:
                        l += 1
                    if self.game.player.rect.x - nb[2] < self.game.blocktab[i][0] + self.game.blocktab[i][
                        2] and not self.game.player.rect.x <= self.game.blocktab[i][0] + self.game.blocktab[i][
                        2] - 10 and self.game.player.rect.y + self.game.player.rect.height > self.game.blocktab[i][
                        1] + 1 and self.game.player.rect.y < self.game.blocktab[i][1] + self.game.blocktab[i][3] - 1:
                        n += 1

                if y == 1:
                    if l == 0:
                        if nb[0] <= nb[1] // 2:
                            self.game.player.rect.x += nb[2]
                    if n == 0:
                        if not nb[0] <= nb[1] // 2:
                            self.game.player.rect.x -= nb[2]
                if y == 2:
                    if nb[0] <= nb[1] // 2:
                        self.game.player.rect.y -= nb[2]
                    if not nb[0] <= nb[1] // 2:
                        self.game.player.rect.y += nb[2]

            if y == 1:
                if not nb[1] % 2 == 0:
                    nb[1] += 1
                if nb[0] <= nb[1] // 2:
                    self.game.blocktab[x][0] += nb[2]
                    self.rect.x += nb[2]

                else:
                    self.game.blocktab[x][0] -= nb[2]
                    self.rect.x -= nb[2]
            if y == 2:
                if not nb[1] % 2 == 0:
                    nb[1] += 1
                if nb[0] <= nb[1] // 2:
                    self.game.blocktab[x][1] -= nb[2]
                    self.rect.y -= 2

                else:
                    self.game.blocktab[x][1] += nb[2]
                    self.rect.y += 2

        if v == 1:
            self.game.nbechelleI = [0, 0, 0]
            self.coucou = 0
            self.INt = 0
            rect = pygame.Rect(self.game.blocktab[x][0], self.game.blocktab[x][1], self.game.blocktab[x][2],
                               self.game.blocktab[x][3])
            if rect.x <= self.game.player.rect.x and rect.x + rect.width >= self.game.player.rect.x and rect.y <= self.game.player.rect.y + self.game.player.rect.height and rect.y + self.rect.width >= self.game.player.rect.y:
                for i in range(len(self.game.blocktab)):
                    if self.game.blocktab[i][0] <= self.game.player.rect.x and self.game.blocktab[i][
                        0] + self.game.player.rect.width >= self.game.player.rect.x and self.game.blocktab[i][
                        1] + self.game.player.rect.width >= self.game.player.rect.y and self.game.blocktab[i][
                        1] <= self.game.player.rect.y + self.game.player.rect.height + 6 and not \
                    self.game.blocktab[i][4][5] == 1:
                        self.coucou += 1
                        self.INt = i

                if self.coucou > 0:
                    self.game.player.rect.y += self.game.blocktab[self.INt][1] - (
                                self.game.player.rect.y + self.game.player.rect.height)

                else:

                    self.game.player.rect.y += 6

    def i_am_moving_left(self): #deplace le block
        self.rect.x -= self.velocity

    def remove(self): #suprime le block
        self.game.all_blockx.remove(self)





