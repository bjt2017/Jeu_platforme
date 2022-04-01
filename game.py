import pygame  # importation des classes
import time  # importation des classes
from block import Block  # importation des classes
from deco_block import Deco_block  # importation des classes
from flat import Flat  # importation des classes
from menu import menu  # importation des classes
from object import Object  # importation des classes
from piege import Piege  # importation des classes
from player import Player  # importation des classes
from editor import Editor  # importation des classes
from magic import Magic  # importation des classes
from monster import Monster  # importation des classes
from audio import Audio  # importation des sons

flat = Flat()
sauter = False
fichier_level = open('fichier/level.txt', mode='r+')
level = int(fichier_level.readline())


class Game:  # je cree une classe game
    def __init__(self, tomber, monde, skin):  # j'innisialise la classe
        # je cree toute les variable utiliser dans game
        self.playing = False
        self.skin = skin
        self.skin_acheter = {1: [True, 100], 2: [False, 200], 3: [False, 300]}
        self.bg = pygame.image.load('assets/background/Background.png')
        self.bg = pygame.transform.scale(self.bg, (1080 + 8, 704))  # je redimentionne le font d'ecran
        self.background_rect_1 = self.bg.get_rect()  # je recupert le rectangle de cette image
        self.background_rect_2 = self.bg.get_rect()  # je recupert le rectangle de cette image
        self.background_rect_3 = self.bg.get_rect()  # je recupert le rectangle de cette image
        self.background_rect_2.x = self.background_rect_2.x + self.background_rect_2.width  # je positionne le background
        self.background_rect_3.x = self.background_rect_3.x - self.background_rect_3.width  # je positionne le background
        self.boul_feu1 = 1  # variable du jeu
        self.monde = monde  # variable du jeu
        self.coin = 800  # variable du jeu
        self.avance = False  # variable du jeu
        self.block_a = 0  # variable du jeu
        self.taille = -64 * self.block_a  # variable du jeu
        self.ajouter = int(self.taille / -64)  # variable du jeu
        self.matrice = [[0] * (self.ajouter + 17),  # matrice utiliser dans le jeu
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17)]
        self.spawn_distance = 0  # variable du jeu
        self.rectportail = 0  # variable du jeu
        self.nbv = 0  # variable du jeu
        self.gogol = 0  # variable du jeu
        self.nbechelle = 0  # variable du jeu
        self.nbechelleI = [0, 0, 0]  # tableau du jeu
        self.nbechelleII = [0, 0, 2, 0, 0]  # tableau du jeu
        self.avancementP = 4  # variable du jeu
        self.boul_feu = 0  # variable du jeu
        self.nb = 0  # variable du jeu
        self.startCo = []  # tableau du jeu
        self.nbb_block = 0  # variable du jeu
        self.tomber = tomber  # variable du jeu
        self.tab = []  # variable du jeu
        self.tab2 = []  # variable du jeu
        self.blocktab = []  # variable du jeu
        self.monster = Monster(self)  # sprite
        self.object = Object(self)  # sprite
        self.magic = Magic(self)  # sprite
        self.decotab = []  # tableau du jeu
        self.level = level  # variable du jeu
        self.pressed = {}  # biblioteque
        self.pressed2 = {}  # biblioteque
        self.sauter_ani2 = 0  # variable du jeu
        self.flat = Flat()  # sprite
        self.deco_block = Deco_block(self)  # sprite
        self.block = Block(self)  # sprite
        self.player = Player(self)  # sprite
        self.piege = Piege(self)  # sprite
        self.menu = menu(self)  # sprite
        self.audio = Audio()  # audio
        self.portal_sound = 'vrai'  # audio

        self.all_monster = pygame.sprite.Group()  # groupe de sprite des monstre
        self.all_object = pygame.sprite.Group()  # groupe de sprite des objects
        self.all_players = pygame.sprite.Group()  # groupe de sprite des player presque inutiliser
        self.all_players.add(self.player)  # on ajoute un player au groupe des sprites player
        self.all_blockx = pygame.sprite.Group()  # groupe de sprite des blockx
        self.all_deco_block = pygame.sprite.Group()  # groupe de sprite des block de deco
        self.all_magic = pygame.sprite.Group()  # groupe de sprite des projectiles
        self.x = 0  # variable
        self.pomme1 = 0  # variable
        self.mouv = False  # variable
        self.avancement = 2  # variable
        self.avancementI = 0  # variable
        self.avancementO = 0  # variable
        self.verify_mouvO = False  # variable
        self.verify_mouvO1 = False  # variable
        self.BlockSp = 0  # variable
        self.mmmm = 0  # variable
        self.avancementT = 0  # variable
        self.block_list = []  # variable
        self.alert = True  # variable
        self.objecttab = []  # variable
        self.portal = [0, 0, 0]  # variable
        self.xy = 0  # variable
        self.alert1 = False  # variable
        self.editor = False  # variable
        self.player._vie()  # variable
        self.open = False  # variable
        self.transiton = False  # variable
        self.transitontab = [0, 0, [0, 0], 0, 0]  # variable
        self.nb_depacement = 0  # variable

    def variable(self, skin_a, skin):
        self.skin_acheter = skin_a
        self.skin = skin

    def MAgic(
            self):  # Fontion qui permet de faire bouger les projectilles de les faire spawn et qui regarde les colision
        if self.editor == True:
            self.boule = False
        else:
            self.boule = False
        if self.boule == True:
            self.magic.check_collision()
            self.verify_spawn_boule()
            self.mouv_boule_de_feu()

    def cree_mat(self, x):  # creation d'une matrice qui fait la taille de l'ecran
        self.taille = -64 * x
        self.ajouter = int(self.taille / -64)
        self.matrice = [[0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17),
                        [0] * (self.ajouter + 17)]

    def start(self):  # debut du programe
        block = Block(self)
        self.spawn_Block(0, -1000, 64, 16, "assets/Start (Idle).png", [10, 64, 0, 2, True, 0, 0, [0, 0, 0], [0, 0, 0]],
                         0)
        self.player.rect.x = 0
        self.player.rect.y = -1000 - 64

    def mouv_eau(self):  # fonction qui change l'image de tout les block d'eau
        if self.block.watherindex < len(self.block.watherframe) - 1:
            self.block.watherindex += 1
        else:
            self.block.watherindex = 0
        for i in range(len(self.block_list)):
            if self.block_list[i][6] == 1:
                for y in self.all_blockx:
                    if y.rect.x == self.block_list[i][0] and y.rect.y == self.block_list[i][1]:
                        y.image = self.block.watherframe[self.block.watherindex]

    def sort(self):  # trie du tableau qui cotient tout les blocks (tris en fonction de ordonner)
        mat = []
        for i in range(len(self.blocktab)):
            mat.append([self.blocktab[i][1], i])
        mat.sort()
        matI = []
        for i in range(len(mat)):
            matI.append(self.blocktab[mat[i][1]])
        self.blocktab = matI

        mat = []
        for i in range(len(self.block_list)):
            mat.append([self.block_list[i][1], i])
        mat.sort()
        matI = []
        for y in range(len(mat)):
            matI.append(self.block_list[mat[y][1]])
        self.block_list = matI

    def spaw_monster(self, x, y):  # fonction qui fait aparaitre un enemies et qui cree un nouvelle object
        monster = Monster(self)
        monster.rect.x = x
        monster.rect.y = y
        self.all_monster.add(monster)

    def spawn_pomme(self, x, y):  # fonction qui place des pommes en fontion de l'abssise et de l'ordonner
        pomme = Object(self)
        pomme.rect.x = x
        pomme.rect.y = y
        pomme.image = self.object.coinimage1
        self.objecttab.append([x, y, 0, 0])
        self.all_object.add(pomme)

    def spawn_blockFor(self, x, y, tran_x, tran_y, image, option, v):  # fonction qui trouve ou placer le block
        self.x = 0
        global collone, ligne
        if not option[0] == 10:
            # portail
            if option[8][0] == 5:
                for i in range(1, 100):
                    if x >= (tran_x * (i - 1)) + (self.avancementI) and x < (64 * i) + (self.avancementI * self.nbv):
                        collone = i
                for i in range(1, 100):

                    if not self.open == True:
                        if y >= 64 * (i - 1) - 64 and y < 64 * i - 64:
                            ligne = i
                    else:

                        if y >= 64 * (i - 1) - 128 and y < 64 * i - 128:
                            ligne = i


            # block de y = 64
            elif v < 10:
                for i in range(1, 100):
                    if x >= (tran_x * (i - 1)) + (self.avancementI) and x < (tran_x * i) + (
                            self.avancementI * self.nbv):
                        collone = i
                for i in range(1, 100):
                    if y >= tran_y * (i - 1) and y < tran_y * i:
                        ligne = i
            # tout les autre block comment l'arbre par exemple
            else:
                for i in range(1, 100):
                    if x >= (64 * (i - 1)) + (self.avancementI) and x < (64 * i) + (self.avancementI * self.nbv):
                        collone = i
                for i in range(1, 100):
                    if y >= 64 * (i - 1) and y < 64 * i:
                        ligne = i

            # verify si un block n'est pas deja pose a cette emplacement
            for i in range(len(self.blocktab)):

                if self.blocktab[i][0] == (tran_x * (collone - 1)) + self.avancementT and self.blocktab[i][1] == (
                        tran_y * (ligne - 1)):
                    self.x = 1
            if self.x == 0 or option[8][0] == 5:
                c = 0
                l = 0
                if option[7][0] == 1:
                    for i in range(1, 100):
                        if x >= (tran_x * (i - 1)) + (self.avancementT) and x < (tran_x * i) + (
                                self.avancementT * self.nbv):
                            c = i
                    for i in range(1, 100):
                        if y >= tran_y * (i - 1) and y < tran_y * i:
                            l = i
                    self.matrice[l - 1][c - 1] = option[7][1]
                # portail
                if option[8][0] == 5:
                    self.portal[0] += 1
                # start
                if option[5] == 3:
                    self.player.rect.x = (tran_x * (collone - 1)) + self.avancementT
                    self.player.rect.y = (
                                ((((((tran_y * (ligne - 1)) + (1 * ligne)) + 2) - 2 * (ligne - 1)) + 7) - 70) + ligne)
                    self.spawn_distance = 64 * collone - 1
                # normal block
                if v == 0:
                    self.spawn_Block((tran_x * (collone - 1)) + self.avancementI, (tran_y * (ligne - 1)), tran_x,
                                     tran_y, image, option, v)
                # eau
                elif v == 1:
                    self.spawn_Block((tran_x * (collone - 1)) + self.avancementI,
                                     ((tran_y * (ligne - 1)) + (1 * ligne)) + 1, tran_x, tran_y, image, option, v)
                # portail
                elif v == 8:
                    self.spawn_Block((tran_x * (collone - 1)) + self.avancementI,
                                     ((64 * (ligne - 1)) + (1 * ligne)) + 1 - tran_y, tran_x, tran_y, image, option, v)
                    self.BlockSp += 1
                # arbre
                elif v == 10:
                    self.spawn_deco_Block((64 * (collone - 1)) + self.avancementI - 64,
                                          (64 * (ligne - 1)) - tran_y + 64, tran_x, tran_y, image, option, v)
                # pierre
                elif v == 9:
                    self.spawn_pomme((tran_x * (collone - 1)) + self.avancementI, (tran_y * (ligne - 1)))

    # block de decoration

    def spawn_deco_Block(self, x, y, tran_x, tran_y, image, option, v):  # creation d'un nouvelle object block de deco
        deco_block = Deco_block(self)
        deco_block.image = pygame.image.load(image)
        deco_block.image = pygame.transform.scale(deco_block.image, (tran_x, tran_y))
        deco_block.rect = deco_block.image.get_rect()
        deco_block.rect.x = x
        deco_block.rect.y = y
        self.all_deco_block.add(deco_block)
        self.decotab.append([x, y, tran_x, tran_y, image, option, v])

    def spawn_Block(self, x, y, tran_x, tran_y, image, option, v):  # creation d'un nouvelle object block
        if option[6] == 0:
            block = Block(self)
            block.image = pygame.image.load(image)
            block.image = pygame.transform.scale(block.image, (tran_x, tran_y))
            block.rect = block.image.get_rect()
            block.rect.x = x
            block.rect.y = y
            self.all_blockx.add(block)

            if option[5] == 3:
                self.startCo.append([block.rect.x, block.rect.y])

            self.tab.append(0)
            self.tab2.append(0)
            self.blocks = block
            self.blocktab.append([x, y, tran_x, tran_y, option])
            self.block_list.append([x, y, tran_x, tran_y, image, option, v])
            self.update_block()
            return self.tab, self.tab2

    def spawn_boule_de_feu(self, direction, angle):  # cree un nouveau projectille
        magic = Magic(self)
        for i in range(1, 9):
            if direction == 'droite':
                magic.frame.append(
                    pygame.transform.rotate(pygame.image.load('assets/boule de feu/boule' + str(i) + '.png'),
                                            0 + angle))
            elif direction == 'gauche':
                magic.frame.append(
                    pygame.transform.rotate(pygame.image.load('assets/boule de feu/boule' + str(i) + '.png'),
                                            180 - angle))
        magic.image = magic.frame[0]
        magic.angle = angle
        magic.rect = magic.image.get_rect()
        magic.rect.x = self.player.rect.x
        magic.rect.y = self.player.rect.y - 5 * angle / 10
        magic.magic = 1
        magic.direction = direction
        self.all_magic.add(magic)

    def mouv_boule_de_feu(self):  # fait bouger toute les boule de feu
        for magic in self.all_magic:
            if magic.magic == 1:
                if magic.direction == 'droite':
                    magic.rect.x += (9 - magic.angle / 10)
                    magic.rect.y -= magic.angle / 10


                elif magic.direction == 'gauche':
                    magic.rect.x -= (9 - magic.angle / 10)
                    magic.rect.y -= magic.angle / 10
                if magic.index < len(magic.frame) - 1:
                    magic.index += 1
                else:
                    magic.index = 0
                magic.image = magic.frame[magic.index]

    def verify_block(
            self):  # verify si il faut change l'image du block si il y a un block au dessus de lui ou sur les cotés
        x = 0
        for block in self.all_blockx:
            if self.blocktab[x][4][2] == self.blocktab[x][4][1] + 1:
                self.blocktab[x][4][2] = 0
            else:
                self.blocktab[x][4][2] += 1
            block.check(x, self.blocktab[x][4][0],
                        [self.blocktab[x][4][2], self.blocktab[x][4][1], self.blocktab[x][4][3]],
                        self.blocktab[x][4][5], 0)
            x += 1
        self.nbechelleI = [0, 0, 0]

        for i in range(len(self.blocktab)):
            if self.blocktab[i][4][5] == 1:
                self.block.check(i, self.blocktab[i][4][0],
                                 [self.blocktab[i][4][2], self.blocktab[i][4][1], self.blocktab[i][4][3]],
                                 self.blocktab[i][4][5], 1)
            if self.blocktab[i][4][5] == 2:
                self.block.check(i, self.blocktab[i][4][0],
                                 [self.blocktab[i][4][2], self.blocktab[i][4][1], self.blocktab[i][4][3]],
                                 self.blocktab[i][4][5], 2)

    def changer(self, l, c, chiffre):  # change l'image du block si il y a un block au dessus de lui ou sur les cotés
        self.direction = [0, 0, 0, 0]
        self.conter = 0
        if l != 0 and l != 10 and c != 0 and c != len(self.matrice[0]) - 1:
            if self.matrice[l][c + 1] > 0:
                self.direction[0] = 1
            if self.matrice[l][c - 1] > 0:
                self.direction[1] = 1
            if self.matrice[l - 1][c] > 0:
                self.direction[2] = 1
            if self.matrice[l + 1][c] > 0:
                self.direction[3] = 1
        else:
            if l == 0 and not (c == 0 or c == len(self.matrice[0]) - 1):
                if self.matrice[l][c + 1] > 0:
                    self.direction[0] = 1
                if self.matrice[l][c - 1] > 0:
                    self.direction[1] = 1
                if self.matrice[l + 1][c] > 0:
                    self.direction[3] = 1
                self.direction[2] = 0
            else:
                if c == 0 and l == 0:
                    if self.matrice[l][c + 1] > 0:
                        self.direction[0] = 1
                    if self.matrice[l + 1][c] > 0:
                        self.direction[3] = 1
                    self.direction[2] = 0
                    self.direction[1] = 0

                if c == len(self.matrice[0]) - 1 and l == 0:
                    if self.matrice[l][c - 1] > 0:
                        self.direction[1] = 1
                    if self.matrice[l + 1][c] > 0:
                        self.direction[3] = 1
                    self.direction[2] = 0
                    self.direction[0] = 1

            if l == 10 and not (c == 0 or c == len(self.matrice[0]) - 1):
                if self.matrice[l][c + 1] > 0:
                    self.direction[0] = 1
                if self.matrice[l][c - 1] > 0:
                    self.direction[1] = 1
                if self.matrice[l - 1][c] > 0:
                    self.direction[2] = 1
                self.direction[3] = 0
            else:
                if l == 10 and c == 0:
                    if self.matrice[l][c + 1] > 0:
                        self.direction[0] = 1
                    if self.matrice[l - 1][c] > 0:
                        self.direction[2] = 1
                    self.direction[1] = 0
                    self.direction[3] = 0

                if l == 10 and c == len(self.matrice[0]) - 1:
                    if self.matrice[l][c - 1] > 0:
                        self.direction[1] = 1
                    if self.matrice[l - 1][c] > 0:
                        self.direction[2] = 1
                    self.direction[3] = 0
                    self.direction[0] = 0

            if c == 0 and not (l == 0 or l == 10):
                if self.matrice[l][c + 1] > 0:
                    self.direction[0] = 1
                if self.matrice[l - 1][c] > 0:
                    self.direction[2] = 1
                if self.matrice[l + 1][c] > 0:
                    self.direction[3] = 1
                self.direction[1] = 0

            if c == len(self.matrice[0]) - 1 and not (l == 0 or l == 10):
                if self.matrice[l][c - 1] > 0:
                    self.direction[1] = 1
                if self.matrice[l - 1][c] > 0:
                    self.direction[2] = 1
                if self.matrice[l + 1][c] > 0:
                    self.direction[3] = 1
                self.direction[0] = 0
        for i in range(len(self.direction)):
            self.conter += self.direction[i]
        if self.conter > 0:
            self.changer_image(chiffre, self.direction)

    def update_block(self):  # appelle les fonction pour changer l'imge des blocks
        for i in range(len(self.matrice)):
            for y in range(len(self.matrice[0])):
                if self.matrice[i][y] > 0:
                    self.changer(i, y, self.matrice[i][y])

    def trouver_sprite(self, chiffre):  # trouve le block a changer dans le groupe de sprite all_block
        self.i = 0
        for i in range(len(self.blocktab)):
            if self.blocktab[i][4][7][1] == chiffre:
                self.i = i
        for block in self.all_blockx:
            if block.rect.x == self.blocktab[self.i][0] and block.rect.y == self.blocktab[self.i][1]:
                return block

    def changer_image(self, chiffre, mini_matix):  # change l'image des blocks
        self.blocks = self.trouver_sprite(chiffre)
        if mini_matix == [0, 0, 1, 0] or mini_matix == [1, 1, 1, 0]:
            self.blocks.image = self.block.haut
        if mini_matix == [0, 0, 0, 1] or mini_matix == [1, 1, 0, 1]:
            self.blocks.image = self.block.bas
        if mini_matix == [1, 1, 0, 0]:
            self.blocks.image = self.block.entourer
        if mini_matix == [1, 1, 1, 1]:
            self.blocks.image = self.block.tout
        if mini_matix == [1, 0, 0, 1]:
            self.blocks.image = self.block.droit_haut
        if mini_matix == [0, 1, 0, 1]:
            self.blocks.image = self.block.gauche_haut
        if mini_matix == [0, 1, 1, 0]:
            self.blocks.image = self.block.gauche_bas
        if mini_matix == [1, 0, 1, 0]:
            self.blocks.image = self.block.droit_bas
        if mini_matix == [0, 1, 1, 1]:
            self.blocks.image = self.block.droite
        if mini_matix == [1, 0, 1, 1]:
            self.blocks.image = self.block.gauche
        if mini_matix == [0, 0, 1, 1]:
            self.blocks.image = self.block.tout
        if mini_matix == [0, 1, 0, 0]:
            self.blocks.image = self.block.gauche1
        if mini_matix == [1, 0, 0, 0]:
            self.blocks.image = self.block.droite1

    def avancementx(self, x):  # cette fonction fait bouger tout les blocks plus le background
        if x == 0:
            pass
        elif x < 0:
            self.background_rect_1.x -= 2
            self.background_rect_2.x -= 2
            self.background_rect_3.x -= 2
        else:
            self.background_rect_1.x += 2
            self.background_rect_2.x += 2
            self.background_rect_3.x += 2
        self.avancementI += x
        self.avancementT += x
        try:
            self.startCo[0][0] += x
        except:
            print("yo")
        for block in self.all_blockx:
            block.rect.x += x
        for magic in self.all_magic:
            magic.rect.x += x
        for i in range(len(self.blocktab)):
            self.blocktab[i][0] += x
            self.block_list[i][0] += x
        for pomme in self.all_object:
            pomme.rect.x += x
        for i in range(len(self.objecttab)):
            self.objecttab[i][0] += x
        for deco_block in self.all_deco_block:
            deco_block.rect.x += x
        for i in range(len(self.decotab)):
            self.decotab[i][0] += x
        for monster in self.all_monster:
            monster.rect.x += x

    def dessine_player(self, screen):  # dessine le player sur l'ecran
        screen.blit(self.player.surface, self.player.rect)

    def update(self, screen, tomber):  # fonction appeler dans main

        self.MAgic()  # apple la fonction qui fait spawn les projectille
        self.menu.nombre(self.coin, 3, screen, 14, 50, 0, 24, 32, 30)  # affiche le nombre de piece
        self.port_collide()  # verify si le personnage ne rentre pas dans porte

        if self.nb_depacement == 0:
            self.monster.iadeplacemnt()
            self.nb_depacement += 1
        else:
            if self.nb_depacement == 25:
                self.nb_depacement = 0
            else:  # inteligence artificielle des ennemie
                for monster in self.all_monster:
                    if monster.fonction == 0:
                        x = 0
                        if monster.mouv == 2:

                            for i in range(len(self.blocktab)):
                                if not self.blocktab[i][4][5] == 4:
                                    if (self.blocktab[i][4][5] == 0 or self.blocktab[i][4][
                                        5] == 3) and monster.rect.x + 2 + monster.rect.width >= self.blocktab[i][
                                        0] and not monster.rect.x + monster.rect.width >= self.blocktab[i][
                                        0] + 10 and monster.rect.y + monster.rect.height - 1 > self.blocktab[i][
                                        1] and monster.rect.y < self.blocktab[i][1] + self.blocktab[i][3] - 1:
                                        x = 1
                                        ii = i
                            if x == 0:
                                monster.rect.x += monster.mouv
                                self.monster.modify_apparence()

                        if monster.mouv == -2:
                            for i in range(len(self.blocktab)):
                                if not self.blocktab[i][4][5] == 4:
                                    if (self.blocktab[i][4][5] == 0 or self.blocktab[i][4][
                                        5] == 3) and monster.rect.x - 2 <= self.blocktab[i][0] + self.blocktab[i][
                                        2] and not monster.rect.x <= self.blocktab[i][0] + self.blocktab[i][
                                        2] - 10 and monster.rect.y + monster.rect.height - 1 > self.blocktab[i][
                                        1] and monster.rect.y < self.blocktab[i][1] + self.blocktab[i][3] - 1:
                                        x = 1
                                        ii = i
                            if x == 0:
                                monster.rect.x += monster.mouv
                                self.monster.modify_apparence()

                self.nb_depacement += 1

        for monster in self.all_monster:  # verify si les monstre ne sont pas en colision avec des blocks
            self.monster.verify(monster)

        self.player.draw_vie(screen)  # dessine les coeur de vie du player

        for i in range(len(self.objecttab)):  # annime les object telle que les pieces
            if self.objecttab[i][2] == 1:
                screen.blit(self.object.animation_index[self.objecttab[i][3]],
                            (self.objecttab[i][0], self.objecttab[i][1]))
                if self.objecttab[i][3] < len(self.object.animation_index) - 1:
                    self.objecttab[i][3] += 1
                else:
                    self.objecttab[i][2] = 2
                    self.objecttab[i][0] = 10000
                    self.objecttab[i][1] = 10000

        for coin in self.all_object:  # modify l'image des piece
            coin.image = self.object.coinframe[self.object.coinindex]
        if self.object.coinindex < len(self.object.coinframe) - 1:
            self.object.coinindex += 1
        else:
            self.object.coinindex = 0

        if self.transiton == True:  # transition quand le personnage rentre dans un portail ou quand il est mort
            if self.transitontab[1] == 0:
                if self.transitontab[0] > self.avancementT + 3:
                    self.avancementx(3)
                    self.transitontab[3] += 3
                    self.player.rect.x += 3
                else:
                    self.avancementx(self.transitontab[0] - self.avancementT)
                    self.transiton = False
                    if self.transitontab[4] == 0:
                        self.player.rect.y = self.transitontab[2][1] + 20
                    else:
                        self.player.rect.y = self.transitontab[2][1] - 64
                    self.player.rect.x = self.transitontab[2][0] + self.transitontab[3] + 20
            if self.transitontab[1] == 1:

                if -self.transitontab[0] < self.avancementT - 3:
                    self.avancementx(-3)
                    self.transitontab[3] -= 3
                    self.player.rect.x -= 3
                else:
                    self.avancementx(-self.transitontab[0] - self.avancementT)
                    self.transiton = False
                    if self.transitontab[4] == 0:
                        self.player.rect.y = self.transitontab[2][1] + 20
                    else:
                        self.player.rect.y = self.transitontab[2][1] - 64
                    self.player.rect.x = self.transitontab[2][0] + self.transitontab[3] + 20

        for i in range(len(self.blocktab)):  # synchronisation
            self.block_list[i][0] = self.blocktab[i][0]
            self.block_list[i][1] = self.blocktab[i][1]
            self.block_list[i][2] = self.blocktab[i][2]
            self.block_list[i][3] = self.blocktab[i][3]
            self.block_list[i][5] = self.blocktab[i][4]
        self.sort()

        fichier_level = open('fichier/level.txt', mode='r+')  # ouverture d'un fichier
        self.level = int(fichier_level.readline())
        fichier_level.close()
        x = 24

        if self.player.rect.y > 704:  # mort du personnage si il sort de l'ecran
            self.audio.chan0.play(self.audio.waa)
            if not self.editor == True and not self.player.health == 0:
                self.player.health -= 1
            for i in range(len(self.blocktab)):
                if self.blocktab[i][4][5] == 3:
                    self.i = i
                    self.player.vie = True
            if self.blocktab[self.i][0] < 0:
                self.transiton = True
                self.player.rect.x = self.avancementT
                self.player.rect.y = -1000 - 64
                self.transitontab = [self.avancementT - self.blocktab[self.i][0] + self.spawn_distance - 63, 0,
                                     [self.blocktab[self.i][0], self.blocktab[self.i][1]], 0, 1]
            elif self.blocktab[self.i][0] >= 1088:
                self.transiton = True
                self.player.rect.x = self.avancementT
                self.player.rect.y = -1000 - 64
                self.transitontab = [self.blocktab[self.i][0] - 1088 + self.blocktab[self.i][2], 1,
                                     [self.blocktab[self.i][0], self.blocktab[self.i][1]], 0, 1]
            else:
                self.player.rect.x = self.blocktab[self.i][0] + 10
                self.player.rect.y = self.blocktab[self.i][1] - 64

                self.avancementO = screen.get_width() + 100
                print("yo")

        if self.player.vie == False:  # annimation de la mort du player
            if x - 8 <= self.x < x:
                self.player.surface = self.player.deathframe[x - self.x]
                self.player.rect.y = 575 - 16
                self.player.rect.x = 300
                self.x += 1
            elif self.x == x:
                self.player.vie = True
                self.x = 0
                self.player.surface = self.player.frame[0]

            elif self.x <= 8:
                self.player.surface = self.player.deathframe[self.x]
                self.x += 1
            else:
                self.x += 1

        if self.player.health == 0:
            pass

        self.verify_block()  # change l'image des block

        for object in self.all_object:
            object.check()
        self.all_deco_block.draw(screen)  # dessine tout les objects
        # update
        self.player.check_colision(sauter)  # dessine tout les objects
        self.all_monster.draw(screen)  # dessine tout les objects
        self.dessine_player(screen)  # dessine tout les objects
        self.all_object.draw(screen)  # dessine tout les objects
        self.all_magic.draw(screen)  # dessine tout les objects

        # le mouvement sol

        if self.pressed.get(pygame.K_RIGHT) and not self.pressed.get(
                pygame.K_LEFT) and self.transiton == False:  # fait bouger les block , le background et le peronnage

            if self.avancementT - self.avancementP >= self.taille and self.avancementO == 0:
                if self.player.mouvAlert == False:
                    self.avancement = -self.avancementP

                    self.nbv -= 1
                    self.player.velocity_right = 1
                    self.player.velocity_left = 1
                    self.avancementx(-self.avancementP)
                    self.verify_mouvO = False
            else:
                self.player.velocity_right = 5
                self.player.velocity_left = 5
                self.verify_mouvO = True

            if self.player.right2 == True and self.player.rect.x + self.player.rect.width < screen.get_width():
                self.player.move_right()
            if self.player.right2 == True:
                if self.player.index < 5:
                    self.player.index += 1
                else:
                    self.player.index = 0



        elif self.pressed.get(pygame.K_LEFT) and not self.pressed.get(
                pygame.K_RIGHT) and self.transiton == False:  # fait bouger les block , le background et le peronnage

            if self.avancementT + (self.avancementP) <= 0 and self.avancementO == 0:
                if self.player.mouvAlert == False:
                    self.avancement = self.avancementP

                    self.avancementx(self.avancementP)
                    self.player.velocity_right = 1
                    self.player.velocity_left = 1
                    self.verify_mouvO1 = False
            else:
                self.player.velocity_right = 5
                self.player.velocity_left = 5
                self.verify_mouvO1 = True

                self.nbv += 1
            if self.player.left2 == True and self.player.rect.x > 0:
                self.player.move_left()
            if self.player.left2 == True:
                if self.player.index < 5:
                    self.player.index += 1
                else:
                    self.player.index = 0

        else:
            self.avancement = 0

        self.gogol = 0
        self.nbechelleII = [self.nbechelleII[0], 0, self.nbechelleII[2], self.nbechelleII[3], self.nbechelleII[4]]
        self.block.coucou = 0
        for i in range(len(self.blocktab)):
            if self.blocktab[i][4][5] == 2:
                rect = pygame.Rect(self.blocktab[i][0], self.blocktab[i][1], self.blocktab[i][2], self.blocktab[i][3])

                if rect.x < self.player.rect.x + self.player.rect.width and rect.x + rect.width > self.player.rect.x and rect.y == self.player.rect.y + self.player.rect.height - 1 and rect.y + rect.height > self.player.rect.y and \
                        self.nbechelleII[0] == 0:
                    if self.pressed.get(pygame.K_DOWN):
                        self.player.rect.y += 3
                        self.nbechelleII[3] = 10
                        self.nbechelleII[2] = 2
                        self.nbechelleII[0] = 0

                if rect.x < self.player.rect.x + self.player.rect.width and rect.x + rect.width > self.player.rect.x and rect.y + 1 < self.player.rect.y + self.player.rect.height and rect.y + rect.height > self.player.rect.y:
                    self.gogol += 1
                    self.block.coucou = 1
                    self.nbechelleII[1] = [rect.x, rect.y, rect.width, rect.height]
                    if self.nbechelleII[4] == 0:
                        self.nbechelleII[4] = self.player.rect.y




                else:
                    self.alert = False

        if self.gogol > 0:
            self.alert = True
        if self.block.coucou == 0:
            self.mmmm = 0
        if self.mmmm == 1 and self.pressed.get(pygame.K_UP):
            self.mmmm = 0
            self.player.rect.y -= 2
            self.nbechelleII[2] = 2
            self.nbechelleII[0] = 0
            self.nbechelleII[3] = 10

        if self.block.coucou == 1 and (self.pressed.get(pygame.K_UP) or self.nbechelleII[3] == 10) and self.nbechelleII[
            0] == 0:
            self.nbechelleII[0] = 1
            self.nbechelleII[3] = 0
            self.player.rect.x = self.nbechelleII[1][0] + 12


        elif self.nbechelleII[0] == 1 and (self.pressed.get(pygame.K_RIGHT) or self.pressed.get(pygame.K_LEFT)) and (
                self.player.rect.y == self.nbechelleII[4] or self.block.coucou == 0 or self.mmmm == 1):

            self.nbechelleII[0] = 0
            self.nbechelleII[2] = 0
            self.nbechelleII[4] = 0

        if self.nbechelleII[0] == 1:
            self.avancementP = 0
            self.alert = True
            self.mouv = False

            if self.pressed.get(pygame.K_UP):
                self.player.rect.y -= 4
                if self.player.climb_index < len(self.player.climbframe) - 1:
                    self.player.climb_index += 1
                else:
                    self.player.climb_index = 0

            if self.pressed.get(pygame.K_DOWN):
                self.block.coucou = 0
                for i in range(len(self.blocktab)):
                    if self.blocktab[i][0] <= self.player.rect.x and self.blocktab[i][
                        0] + self.player.rect.width > self.player.rect.x and self.blocktab[i][
                        1] + self.player.rect.width >= self.player.rect.y and self.blocktab[i][
                        1] <= self.player.rect.y + self.player.rect.height + 4 and self.blocktab[i][4][5] != 2:
                        self.INt = i
                        self.block.coucou += 1
                if self.block.coucou == 0:
                    self.player.rect.y += 4
                    if self.player.climb_index < len(self.player.climbframe) - 1:
                        self.player.climb_index += 1
                    else:
                        self.player.climb_index = 0
                    self.mmmm = 0
                else:
                    self.player.rect.y += self.blocktab[self.INt][1] - (
                            self.player.rect.y + self.player.rect.height) + 1
                    self.mmmm = 1

            self.player.surface = self.player.climbframe[self.player.climb_index]
        else:
            self.avancementP = 4

        if self.nbechelleII[0] == 0 and self.nbechelleII[2] == 0:
            self.mouv = True
        self.colision_portal()

    def colision_portal(self):  # colision avec le portail

        self.portal = [self.portal[0], 0, self.portal[2]]
        self.coucou = 0
        self.xxx = 0
        for i in range(len(self.blocktab)):
            self.portal[1] += 1
            if self.blocktab[i][4][8][0] == 5:

                rect = pygame.Rect(self.blocktab[i][0], self.blocktab[i][1], self.blocktab[i][2], self.blocktab[i][3])
                if rect.x < self.player.rect.x + self.player.rect.width and rect.x + rect.width > self.player.rect.x and rect.y + 1 < self.player.rect.y + self.player.rect.height and rect.y + rect.height > self.player.rect.y:
                    self.xxx = i
                    self.coucou = 1
                else:
                    self.alert1 = False

        if self.coucou == 1:
            self.alert1 = True
        if self.coucou == 1 and self.pressed.get((pygame.K_UP)) and self.xy == 0:
            self.xy = 1
            if self.portal_sound == 'vrai':
                self.audio.chan0.play(self.audio.son_in)
            else:
                self.audio.chan0.play(self.audio.son_portail)
            for i in range(len(self.blocktab)):
                if self.blocktab[self.xxx][4][8][1] == 1:
                    if self.blocktab[i][4][8][1] == 2 and self.blocktab[self.xxx][4][8][2] == self.blocktab[i][4][8][2]:
                        self.xxxx = i
                else:
                    if self.blocktab[i][4][8][1] == 1 and self.blocktab[self.xxx][4][8][2] == self.blocktab[i][4][8][2]:
                        self.xxxx = i
            if self.blocktab[self.xxxx][0] < 0:
                self.transiton = True
                self.player.rect.x = self.avancementT
                self.player.rect.y = -1000 - 64
                self.transitontab = [self.avancementT - self.blocktab[self.xxxx][0], 0,
                                     [self.blocktab[self.xxxx][0], self.blocktab[self.xxxx][1]], 0, 0]
            elif self.blocktab[self.xxxx][0] + self.blocktab[self.xxxx][2] >= 1080 + 8:

                self.transiton = True
                self.player.rect.x = self.avancementT
                self.player.rect.y = -1000 - 64
                self.transitontab = [
                    (self.blocktab[self.xxxx][0] - 1088) + (-self.avancementT) + self.blocktab[self.xxxx][2], 1,
                    [self.blocktab[self.xxxx][0], self.blocktab[self.xxxx][1]], 0, 0]

            else:
                self.player.rect.x = self.blocktab[self.xxxx][0] + 20
                self.player.rect.y = self.blocktab[self.xxxx][1]
            self.avancementO = 0

        if self.xy == 1 and self.pressed2.get(pygame.K_UP):
            self.xy = 0

        self.mouv_eau()
        if self.pressed.get(pygame.K_UP) and self.pressed.get(pygame.K_o) and self.pressed.get(pygame.K_b):
            self.coin = 999

    def verify_spawn_boule(self):
        if self.pressed.get(pygame.K_d) and self.boul_feu == 0:
            self.spawn_boule_de_feu('droite', 90)
            self.spawn_boule_de_feu('droite', 70)
            self.spawn_boule_de_feu('droite', 50)
            self.spawn_boule_de_feu('droite', 30)
            self.spawn_boule_de_feu('droite', 10)
            self.spawn_boule_de_feu('droite', -10)
            self.spawn_boule_de_feu('gauche', 90)
            self.spawn_boule_de_feu('gauche', 70)
            self.spawn_boule_de_feu('gauche', 50)
            self.spawn_boule_de_feu('gauche', 30)
            self.spawn_boule_de_feu('gauche', 10)
            self.spawn_boule_de_feu('gauche', 0)

            self.boul_feu = 1
        if self.pressed.get(pygame.K_q) and self.boul_feu1 == 0:
            self.spawn_boule_de_feu('gauche', 0)
            self.boul_feu1 = 1
        if self.pressed.get(pygame.K_q) == False:
            self.boul_feu1 = 0
        if self.pressed.get(pygame.K_d) == False:
            self.boul_feu = 0

    def port_collide(self):
        x = 0
        for i in range(len(self.decotab)):
            if self.decotab[i][5][5] == 10 and self.decotab[i][6] == 10:
                rect = pygame.Rect(self.decotab[i][0], self.decotab[i][1], self.decotab[i][2], self.decotab[i][3])
                if rect.x < self.player.rect.x + self.player.rect.width and rect.x + rect.width > self.player.rect.x and rect.y + 1 < self.player.rect.y + self.player.rect.height and rect.y + rect.height > self.player.rect.y:
                    x += 1
                    int = i

        if x == 0:
            self.alert2 = False
        else:
            if self.pressed.get(pygame.K_UP):
                rect = pygame.Rect(self.decotab[int][0], self.decotab[int][1], self.decotab[int][2],
                                   self.decotab[int][3])
                for i in self.all_deco_block:
                    if rect.x == i.rect.x and rect.y == i.rect.y:
                        i.image = pygame.transform.scale(pygame.image.load('assets/porte/dor2.png'),
                                                         (i.rect.width, i.rect.height))
                        self.playing = False
            print(self.alert2)
            self.alert2 = True

    def update_level1(self, screen):
        self.piege.toucher()
        self.piege.rotate()
        screen.blit(flat.image2, flat.rect2)
        screen.blit(flat.image, flat.rect)
        self.all_block.draw(screen)

    def update_level2(self, screen):
        screen.blit(flat.image2, flat.rect2)
        screen.blit(flat.image, flat.rect)
        self.all_block.draw(screen)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def over(self, screen):
        self.image_game_over = pygame.image.load('assets/GameOver.png')
        screen.blit(self.image_game_over, (200, 200))
        print('game_over')
        self.move = False
        self.alert = True
