import pygame#importation de pigame
class menu:
    def __init__(self,game):
        self.game = game
        self.menu_image = pygame.image.load("assets/menu/menue/menu01.png")#importation d'une image
        self.rect = self.menu_image.get_rect()
        self.rect.x = 190
        self.rect.y = 100

        self.name_image = pygame.image.load("assets/menu/menue/Logo.png")#importation d'une image
        self.namerect = self.menu_image.get_rect()
        self.namerect.x = 320
        self.namerect.y = 0




        self.playimage = pygame.image.load("assets/menu/menue/menue1.png")#importation d'une image
        self.playimage = pygame.transform.scale(self.playimage,(360,82))
        self.playimage2 = pygame.image.load("assets/menu/menue/menue2.png")#importation d'une image
        self.playimage2 = pygame.transform.scale(self.playimage2, (360, 82))
        self.playrect = self.playimage.get_rect()
        self.playrect.x = 360
        self.playrect.y = 186

        self.levelimage = pygame.image.load("assets/menu/menue/menue3.png")#importation d'une image
        self.levelimage = pygame.transform.scale(self.levelimage, (360, 82))
        self.levelimage2 = pygame.image.load("assets/menu/menue/menue4.png")#importation d'une image
        self.levelimage2 = pygame.transform.scale(self.levelimage2, (360, 82))
        self.levelrect = self.playimage.get_rect()
        self.levelrect.x = 360
        self.levelrect.y = 186+200

        self.editimage = pygame.image.load("assets/menu/menue/menue5.png")#importation d'une image
        self.editimage = pygame.transform.scale(self.editimage, (360, 82))
        self.editimage2 = pygame.image.load("assets/menu/menue/menue6.png")#importation d'une image
        self.editimage2 = pygame.transform.scale(self.editimage2, (360, 82))
        self.editrect = self.playimage.get_rect()
        self.editrect.x = 360
        self.editrect.y = 186 + 100

        self.boutiqueimage = pygame.image.load("assets/menu/menue/menue7.png")#importation d'une image
        self.boutiqueimage = pygame.transform.scale(self.boutiqueimage, (360, 82))
        self.boutiqueimage2 = pygame.image.load("assets/menu/menue/menue8.png")#importation d'une image
        self.boutiqueimage2 = pygame.transform.scale(self.boutiqueimage2, (360, 82))
        self.boutiquerect = self.playimage.get_rect()
        self.boutiquerect.x = 360
        self.boutiquerect.y = 186 + 300


        self.chiffre1 =  pygame.image.load("assets/chiffre/chiffre1.png")#importation d'une image
        self.chiffre2 = pygame.image.load("assets/chiffre/chiffre2.png")#importation d'une image
        self.chiffre3 = pygame.image.load("assets/chiffre/chiffre3.png")#importation d'une image
        self.chiffre4 = pygame.image.load("assets/chiffre/chiffre4.png")#importation d'une image
        self.chiffre5 = pygame.image.load("assets/chiffre/chiffre5.png")#importation d'une image
        self.chiffre6 = pygame.image.load("assets/chiffre/chiffre6.png")#importation d'une image
        self.chiffre7 =  pygame.image.load("assets/chiffre/chiffre7.png")#importation d'une image
        self.chiffre8 = pygame.image.load("assets/chiffre/chiffre8.png")#importation d'une image
        self.chiffre9 =  pygame.image.load("assets/chiffre/chiffre9.png")#importation d'une image
        self.chiffre0 = pygame.image.load("assets/chiffre/chiffre0.png")#importation d'une image


        self.menu = pygame.image.load("assets/menu/menu/menu1.png")#importation d'une image
        self.menu_rect = self.menu.get_rect()
        self.menu_rect.x = 300
        self.menu_rect.y = 100

        self.resume_bouton2 = pygame.image.load("assets/menu/menu/menu2.png")#importation d'une image
        self.resume_bouton1 = pygame.image.load("assets/menu/menu/menu3.png")#importation d'une image
        self.resume_rect = self.resume_bouton1.get_rect()
        self.resume_rect.x = 370
        self.resume_rect.y = 190

        self.restart_bouton2 = pygame.image.load("assets/menu/menu/menu4.png")#importation d'une image
        self.restart_bouton1 = pygame.image.load("assets/menu/menu/menu5.png")#importation d'une image
        self.restart_rect = self.resume_bouton1.get_rect()
        self.restart_rect.x = 370
        self.restart_rect.y = 280

        self.seting_bouton2 = pygame.image.load("assets/menu/menu/menu6.png")#importation d'une image
        self.seting_bouton1 = pygame.image.load("assets/menu/menu/menu7.png")#importation d'une image
        self.seting_rect = self.resume_bouton1.get_rect()
        self.seting_rect.x = 370
        self.seting_rect.y = 370

        self.quit_bouton2 = pygame.image.load("assets/menu/menu/menu8.png")#importation d'une image
        self.quit_bouton1 = pygame.image.load("assets/menu/menu/menu9.png")#importation d'une image
        self.quit_rect = self.resume_bouton1.get_rect()
        
        self.quit_rect.x = 370
        self.quit_rect.y = 460

        self.backhome = pygame.image.load("assets/menu/menue/Icons_01.png")#importation d'une image
        self.backhome2 = pygame.image.load("assets/menu/menue/Icons_02.png")#importation d'une image
        self.backhome = pygame.transform.scale2x(self.backhome)
        self.backhome2 = pygame.transform.scale2x(self.backhome2)
        self.backhomerect = self.backhome.get_rect()
        self.backhomerect.x = 250
        self.backhomerect.y = 150

        self.open =  pygame.transform.scale(pygame.image.load("assets/menu/menu/open2.png"),(150,40))#importation d'une image
        self.open_rect = self.open.get_rect()
        self.open_rect.x = 700
        self.open_rect.y = 150


        self.boutiqueimage1 = pygame.image.load("assets/menu/boutique.png")#importation d'une image
        self.boutiqueimage_rect = self.boutiqueimage1.get_rect()
        self.boutiqueimage_rect.x = 40
        self.boutiqueimage_rect.y = 40

        self.boutiqueimage56 = pygame.image.load("assets/menu/boutique56.png")#importation d'une image
        self.boutiqueimage56_rect = self.boutiqueimage1.get_rect()
        self.boutiqueimage56_rect.x = 375
        self.boutiqueimage56_rect.y = 80

        self.idem = pygame.transform.scale(pygame.image.load("assets/menu/item.png"),(126,40))#importation d'une image
        self.idem_rect = self.idem.get_rect()
        self.idem_rect.x = 150
        self.idem_rect.y = 170

        self.skin = pygame.transform.scale(pygame.image.load("assets/menu/skin.png"), (126, 40))#importation d'une image
        self.skin_rect = self.idem.get_rect()
        self.skin_rect.x = 150
        self.skin_rect.y = 400

        self.boule_feu = pygame.transform.scale2x(pygame.image.load("assets/menu/10-Fire-ball2.png"))#importation d'une image
        self.boule_feu_rect = self.boule_feu.get_rect()
        self.boule_feu_rect.x = 170
        self.boule_feu_rect.y = 240

        self.skin1 = pygame.transform.scale2x(pygame.image.load("assets/menu/Portraits2_01.png"))#importation d'une image
        self.skin1_rect = self.skin1.get_rect()
        self.skin1_rect.x = 170
        self.skin1_rect.y = 465

        self.skin2 = pygame.transform.scale2x(pygame.image.load("assets/menu/Portraits2_07.png"))#importation d'une image
        self.skin2_rect = self.skin2.get_rect()
        self.skin2_rect.x = 350
        self.skin2_rect.y = 465

        self.skin3 = pygame.transform.scale2x(pygame.image.load("assets/menu/Portraits2_13.png"))#importation d'une image
        self.skin3_rect = self.skin3.get_rect()
        self.skin3_rect.x = 530
        self.skin3_rect.y = 465

        self.button_vierge = pygame.image.load("assets/menu/button_vierge.png")#importation d'une image
        self.button_vierge_rect = [self.button_vierge.get_rect(),self.button_vierge.get_rect(),self.button_vierge.get_rect(),self.button_vierge.get_rect()]
        self.button_vierge_rect[0].x = self.skin1_rect.x-45
        self.button_vierge_rect[0].y = self.skin1_rect.y+76
        self.button_vierge_rect[1].x = self.skin2_rect.x-45
        self.button_vierge_rect[1].y = self.skin2_rect.y+76
        self.button_vierge_rect[2].x = self.skin3_rect.x-45
        self.button_vierge_rect[2].y = self.skin3_rect.y+76
        self.button_vierge_rect[3].x = self.boule_feu_rect.x - 45
        self.button_vierge_rect[3].y = self.boule_feu_rect.y + 76


        self.valide_true = pygame.transform.scale(pygame.image.load("assets/menu/valide2.png"),(39,39))#importation d'une image
        self.valide_false = pygame.transform.scale(pygame.image.load("assets/menu/valide1.png"),(12*3,12*3))#importation d'une image





        self.flecheg = pygame.image.load("assets/menu/menue/Icons_25.png")#importation d'une image
        self.fleched = pygame.image.load("assets/menu/menue/Icons_26.png")#importation d'une image
        self.flecheg = pygame.transform.scale2x(self.flecheg)
        self.fleched = pygame.transform.scale2x(self.fleched)
        self.flecheg_rect = self.flecheg.get_rect()
        self.fleched_rect = self.fleched.get_rect()
        self.flecheg_rect2 = self.flecheg.get_rect()
        self.fleched_rect2 = self.fleched.get_rect()
        self.flecheg_rect.x = 450
        self.flecheg_rect.y = 350
        self.fleched_rect.x = 300
        self.fleched_rect.y = 350
        self.flecheg_rect2.x = 400+350
        self.flecheg_rect2.y = 350
        self.fleched_rect2.x = 250+350
        self.fleched_rect2.y = 350

        self.valide1 = pygame.image.load("assets/menu/menue/valide1.png")#importation d'une image
        self.valide2 = pygame.image.load("assets/menu/menue/valide2.png")#importation d'une image
        self.validerect = self.valide1.get_rect()
        self.validerect.x = 385
        self.validerect.y = 480
        
        


        self.image_mondes = [pygame.image.load('assets/background/monde_1.png'),
                             pygame.transform.scale(pygame.image.load('assets/background/monde_1.png'), (3869, 2503)),]#importation d'une image

        #placer les coordonées de la carte
        self.image_mondes_rect = self.image_mondes[1].get_rect()
        self.image_mondes_rect.x = 0
        self.image_mondes_rect.y = 0

        # dictionaire pour le placement des niveaux des mondes
        self.place_monde = [{0:[60, 80, 'x', [None, 1, None, None]],
                             1:[341, 80, 'y', [None, None, 2, 0]],
                             2:[341, 320, 'x', [1, None, None, 3]],
                             3:[60, 320, 'y', [None, 2, 4, None]],
                             4:[60, 570, 'x', [3, 5, None, None]],
                             5:[520, 570, 'x', ['A', 6, None, 4]],
                             6:[740, 570, 'x', [None, 'n', None, 5]],
                             'n':[905, 570, 'y', [7, None, None, 6]],
                             7:[905, 380, 'x', [None, None, 'n', None]],
                             'A':[520, 460, 'y', [None, None, 5, None]]},
                            
                            {0:[0, 0, [None, 1, None, None]],
                             1:[-340, 0, [None, None, 2, 0]],
                             2:[-340, -175, [1, 3, None, None]],
                             3:[-700, -175, [None, 4, None, 2]],
                             4:[-1445, -145, [None, 'n15', None, 3]],
                             'n15':[-1900, -155, [None, 'n25', None, 4]],
                             'n25':[-2080, -190, [None, 'n35', None, 'n15']],
                             'n35':[-2260, -225, [None, 5, None, 'n25']],
                             5:[-2543, -235, [None, 'A', 6, 'n35']],
                             6:[-2543, -1040, [5, None, 7, None]],
                             7:[-2537, -1520, [6, None, None, 8]],
                             8:[-1655, -1520, [9, 7, 10, 'B']],
                             9:[-1655, -960, [None, None, 8, None]],
                             10:[-1655, -1820, [8, None, None, 11]],
                             11:[-140, -1820, [12, 10, None, None]],
                             12:[-140, -840, [None, 'ch', 11, None]],
                             'ch':[-570, -850, [None, None, None, 12]],
                             'B':[-1320, -1520, [None, 8, None, None]],
                             'A':[-2740, -235, [None, None, None, 5]]}]

        #applique les valeurs par default pour ne pas avoir de variable vide
        self.monde1_level = self.place_monde[0]
        self.image_monde1 = self.image_mondes[0]
        self.menurect = self.game.player.frame[0].get_rect()


    def position_perso(self, x, y, move, screen,direction): #cette fonction fait bouger le personnage dans le menu
        if move == True:
            if self.game.player.index < len(self.game.player.frame)-1:
                self.game.player.index += 1
                #print('u')
            else:
                self.game.player.index = 0
        else:
            self.game.player.index = 0
        #print('y')
        self.menurect.x = x
        self.menurect.y = y
        if direction=='droite':
            screen.blit(pygame.transform.scale(self.game.player.frame[self.game.player.index], (51, 84)), self.menurect)
        else:
            screen.blit(pygame.transform.scale(self.game.player.frame2[self.game.player.index], (51, 84)), self.menurect)

    def deplacer_perso_x(self, persox, persoy, xgoal, vitesse, mov_menu, screen):#cette fonction fait bouger le personnage dans le menu en x c'est a dire de droite a gauche
        direction = 'droite'
        if persox == xgoal:
            mov_menu = False
            
        if mov_menu and persox != xgoal:
            if persox < xgoal:
                direction = 'droite'
                if persox+vitesse < xgoal:
                    persox += vitesse
                    #print('go')
                else:
                    #print('ya')
                    persox += (xgoal-persox)
                    mov_menu = False
            elif persox > xgoal:
                direction = 'gauche'
                if persox-vitesse > xgoal:
                    persox -= vitesse
                else:
                    persox -= (xgoal-persox)
                    mov_menu = False

        self.position_perso(persox, persoy, mov_menu, screen, direction)
        return persox, mov_menu


    def deplacer_perso_y(self, persox, persoy, ygoal, vitesse, mov_menu, screen):#cette fonction fait bouger le personnage dans le menu dans l'ordonner
        direction = 'droite'
        if persoy == ygoal:
            mov_menu = False
            
        if mov_menu and persoy != ygoal:
            if persoy < ygoal:
                direction = 'droite'
                if persoy+vitesse < ygoal:
                    persoy += vitesse
                    #print('go')
                else:
                    #print('ya')
                    persoy += (ygoal-persoy)
                    mov_menu = False
            elif persoy > ygoal:
                direction = 'gauche'
                if persoy-vitesse > ygoal:
                    persoy -= vitesse
                else:
                    persoy -= (ygoal-persoy)
                    mov_menu = False

        self.position_perso(persox, persoy, mov_menu, screen, direction)
        return persoy, mov_menu

    def select_x_or_y(self, goooo): #pour debuger
        if goooo == 'x':
            return 0
        else:
            return 1

    def change_level(self, levelin, setlevelin, dire): #deplace le joueur en fonction de la direction
        if dire == 'aller':
            goooo = self.monde1_level[levelin][2]
            x_or_y = self.select_x_or_y(goooo)
            levelin = setlevelin
        elif dire == 'revenir':
            levelin = setlevelin
            goooo = self.monde1_level[levelin][2]
            x_or_y = self.select_x_or_y(goooo)
        else:
            goooo = self.monde1_level[levelin][2]
            x_or_y = self.select_x_or_y(goooo)
        return goooo, x_or_y, levelin, True

    def monde1_aller_revenir(self, levelin, direction): #defini la direction en fonction des niveaux (pour debuger)
        if direction == 'Up':
            if levelin in ['n']:
                return 'aller'
            elif levelin in [2, 4, 5]:
                return 'revenir'
            
        elif direction == 'Right':
            if levelin in [0, 4, 5, 6]:
                return 'aller'
            elif levelin in [3]:
                return 'revenir'
            
        elif direction == 'Down':
            if levelin in [1, 3, 'A']:
                return 'aller'
            elif levelin in [7]:
                return 'revenir'
            
        elif direction == 'Left':
            if levelin in [2]:
                return 'aller'
            elif levelin in [1, 5, 6, 'n']:
                return 'revenir'
        else:
            return 'yo'


    def deplacer_perso(self, persox, persoy, pos_goal, vitesse, mov_menu, x_y, screen): #deplace le perso dans un seul axe
        if x_y == 'x':
            pos_changex, mov_menu = self.deplacer_perso_x(persox, persoy, pos_goal, vitesse, mov_menu, screen)
            pos_changey = persoy
        elif x_y == 'y':
            pos_changey, mov_menu = self.deplacer_perso_y(persox, persoy, pos_goal, vitesse, mov_menu, screen)
            pos_changex = persox
        return pos_changex, pos_changey, mov_menu


    def deplacer_libre(self, persox, persoy, xgoal, ygoal, vitessex, vitessey, mov_menu, screen, perso=True): #deplace le perso dans les 2 axes
        direction = 'droite'
        if not perso:
            mov_menu = True
        if persox == xgoal and persoy == ygoal:
            mov_menu = False
            
        if mov_menu and persox != xgoal:
            if persox < xgoal:
                direction = 'droite'
                if persox+vitessex < xgoal:
                    persox += vitessex
                    #print('go')
                else:
                    #print('ya')
                    persox += (xgoal-persox)
            elif persox > xgoal:
                direction = 'gauche'
                if persox-vitessex > xgoal:
                    persox -= vitessex
                else:
                    persox += (xgoal-persox)
                    
        if mov_menu and persoy != ygoal:
            if persoy < ygoal:
                direction = 'droite'
                if persoy+vitessey < ygoal:
                    persoy += vitessey
                    #print('go')
                else:
                    #print('ya')
                    persoy += (ygoal-persoy)
            elif persoy > ygoal:
                direction = 'gauche'
                if persoy-vitessey > ygoal:
                    persoy -= vitessey
                else:
                    persoy += (ygoal-persoy)

        if perso:    
            self.position_perso(persox, persoy, mov_menu, screen, direction)
            
        #print(persox, persoy, xgoal, ygoal, mov_menu)
        
        return persox, persoy, mov_menu


    def deplacer_niveau(self, mondein, levelin, mov_menu, direction): #choisi de deplcaer le personnage quand il est entre deux niveaux (le 4 et le 5)
        if type(levelin) == str:
            if levelin.find('n') == 0:
                if not mov_menu:
                    levelin = self.place_monde[mondein][levelin][2][direction]
        return levelin

    def find_direction(self, mondein, levelin, direction): ##defini la direction en fonction des niveaux (pour le monde)
        if mondein == 1:
            if direction == 'Up' or direction == 0:
                if levelin in []:
                    return 'droite'
                elif levelin in []:
                    return 'gauche'
                
            elif direction == 'Right' or direction == 1:
                if levelin in [0, 2, 3, 4, 'n15', 'n25', 'n35', 5]:
                    return 'droite'
                elif levelin in []:
                    return 'gauche'
                
            elif direction == 'Down' or direction == 2:
                if levelin in []:
                    return 'droite'
                elif levelin in []:
                    return 'gauche'
                
            elif direction == 'Left' or direction == 3:
                if levelin in []:
                    return 'droite'
                elif levelin in [1, 3, 4, 'n15', 'n25', 'n35',5 , 'A', 7, 8, 10, 'ch']:
                    return 'gauche'
                
        return 'droite'
            
        
        

    def nombre(self,nombre,chiffre_max,screen,x,y,v,tran_x,trans_y,espace):#fonction qui permet d'afficher une variable a l'ecran
        while not chiffre_max==0:
            nb = 0
            nombre_chiffre = 10 ** (chiffre_max - 1)
            for i in range(10):

                if int(nombre/nombre_chiffre) == i:
                    nb = i
            screen.blit(pygame.transform.scale(pygame.image.load("assets/chiffre/chiffre"+str(nb)+".png"),(tran_x,trans_y)),(x,y))
            nombre -= nb*nombre_chiffre
            chiffre_max -= 1
            x += espace
        if v == 0:
            screen.blit(self.game.object.coinframe[self.game.object.coinindex],(x,y))
        if v == 3:
            screen.blit(self.game.object.coinframe[0], (x, y))

    def ligne_collone(self, x, y,tran_x,tran_y,fonction):
        if fonction == 0:
            for i in range(1, 100):
                if x >= (64 * (i - 1)) + (self.game.avancementI) and x < (64 * i) + (self.game.avancementI * self.game.nbv):
                    collone = i
            for i in range(1, 100):
                if y >= 64 * (i - 1) and y < 64 * i:
                    ligne = i
        elif fonction==1:
            for i in range(1, 100):
                if x >= (tran_x * (i - 1)) + (self.game.avancementI) and x < (64 * i) + (self.game.avancementI * self.game.nbv):
                    collone = i
            for i in range(1, 100):
                if y >= tran_y * (i - 1) and y < tran_y * i:
                    ligne = i

        return ligne,collone









