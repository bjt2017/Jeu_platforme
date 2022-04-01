import pygame

from block import Block
from flat import Flat

fichier = open('fichier/verify.txt', mode='r+')
nb = int(fichier.readline())
fichier2 = open('fichier/left.txt', mode='r+')
left = int(fichier2.readline())
fichier3 = open('fichier/right.txt', mode='r+')
right = int(fichier3.readline())


if nb == 2:
    verify = True
else:
    verify = False
if right == 1:
    right2 = True
else:
    right2 = False
if left == 1:
    left2 = True
else:
    left2 = False
class Player(pygame.sprite.Sprite):#creation de la class player
    def __init__(self,game):#intitialisation de cette classe
        super().__init__()

        self.vie = True#variable de la class player
        self.health = 4#variable de la class player
        self.max_health = 4#variable de la class player
        self.block = Block(game)#variable de la class player
        self.flat = Flat()#variable de la class player
        self.game = game#variable de la class player

        self.Y = 30
        if self.game.skin == 1:
            #right
            self.image = pygame.image.load("assets/player_pink/droite/Pink1.png")#import des image du player
            self.image2 = pygame.image.load("assets/player_pink/droite/Pink2.png")#import des image du player
            self.image3 = pygame.image.load("assets/player_pink/droite/Pink3.png")#import des image du player
            self.image4 = pygame.image.load("assets/player_pink/droite/Pink4.png")#import des image du player
            self.image5 = pygame.image.load("assets/player_pink/droite/Pink5.png")#import des image du player
            self.image6 = pygame.image.load("assets/player_pink/droite/Pink6.png")#import des image du player

            #left
            self.image7 = pygame.image.load("assets/player_pink/gauche/Pink1.png")#import des image du player
            self.image8 = pygame.image.load("assets/player_pink/gauche/Pink2.png")#import des image du player
            self.image9 = pygame.image.load("assets/player_pink/gauche/Pink3.png")#import des image du player
            self.image10 = pygame.image.load("assets/player_pink/gauche/Pink4.png")#import des image du player
            self.image11 = pygame.image.load("assets/player_pink/gauche/Pink5.png")#import des image du player
            self.image12 = pygame.image.load("assets/player_pink/gauche/Pink6.png")#import des image du player

            self.climb1 = pygame.image.load("assets/player_pink/climb/Climb1.png")#import des image du player
            self.climb2 = pygame.image.load("assets/player_pink/climb/Climb2.png")#import des image du player
            self.climb3 = pygame.image.load("assets/player_pink/climb/Climb3.png")#import des image du player
            self.climb4 = pygame.image.load("assets/player_pink/climb/Climb4.png")#import des image du player



        if self.game.skin == 2:
            self.image = pygame.transform.scale(pygame.image.load("assets/white_player/droite/White1.png"),(40,54))#import des image du player
            self.image2 = pygame.transform.scale(pygame.image.load("assets/white_player/droite/White2.png"),(40,54))#import des image du player
            self.image3 = pygame.transform.scale(pygame.image.load("assets/white_player/droite/White3.png"),(40,54))#import des image du player
            self.image4 = pygame.transform.scale(pygame.image.load("assets/white_player/droite/White4.png"),(40,54))#import des image du player
            self.image5 = pygame.transform.scale(pygame.image.load("assets/white_player/droite/White5.png"),(40,54))#import des image du player
            self.image6 = pygame.transform.scale(pygame.image.load("assets/white_player/droite/White6.png"),(40,54))#import des image du player

            # left
            self.image7 = pygame.image.load("assets/white_player/gauche/White1.png")#import des image du player
            self.image8 = pygame.image.load("assets/white_player/gauche/White2.png")#import des image du player
            self.image9 = pygame.image.load("assets/white_player/gauche/White3.png")#import des image du player
            self.image10 = pygame.image.load("assets/white_player/gauche/White4.png")#import des image du player
            self.image11 = pygame.image.load("assets/white_player/gauche/White5.png")#import des image du player
            self.image12 = pygame.image.load("assets/white_player/gauche/White6.png")#import des image du player

            self.climb1 = pygame.image.load("assets/white_player/climb/white1.png")#import des image du player
            self.climb2 = pygame.image.load("assets/white_player/climb/white2.png")#import des image du player
            self.climb3 = pygame.image.load("assets/white_player/climb/white3.png")#import des image du player
            self.climb4 = pygame.image.load("assets/white_player/climb/white4.png")#import des image du player



        if self.game.skin == 3:
            self.image = pygame.image.load("assets/blue_player/droite/blue1.png")#import des image du player
            self.image2 = pygame.image.load("assets/blue_player/droite/blue2.png")#import des image du player
            self.image3 = pygame.image.load("assets/blue_player/droite/blue3.png")#import des image du player
            self.image4 = pygame.image.load("assets/blue_player/droite/blue4.png")#import des image du player
            self.image5 = pygame.image.load("assets/blue_player/droite/blue5.png")#import des image du player
            self.image6 = pygame.image.load("assets/blue_player/droite/blue6.png")#import des image du player

            # left
            self.image7 = pygame.image.load("assets/blue_player/gauche/blue1.png")#import des image du player
            self.image8 = pygame.image.load("assets/blue_player/gauche/blue2.png")#import des image du player
            self.image9 = pygame.image.load("assets/blue_player/gauche/blue3.png")#import des image du player
            self.image10 = pygame.image.load("assets/blue_player/gauche/blue4.png")#import des image du player
            self.image11 = pygame.image.load("assets/blue_player/gauche/blue5.png")#import des image du player
            self.image12 = pygame.image.load("assets/blue_player/gauche/blue6.png")#import des image du player

            self.climb1 = pygame.image.load("assets/blue_player/climb/Climb1.png")#import des image du player
            self.climb2 = pygame.image.load("assets/blue_player/climb/Climb2.png")#import des image du player
            self.climb3 = pygame.image.load("assets/blue_player/climb/Climb3.png")#import des image du player
            self.climb4 = pygame.image.load("assets/blue_player/climb/Climb4.png")#import des image du player

        self.climb_index = 0 #variable
        self.climbframe = [self.climb1, self.climb1, self.climb1, self.climb1, self.climb2, self.climb2, self.climb2,#tableau
                           self.climb2, self.climb3, self.climb3, self.climb3, self.climb3, self.climb4, self.climb4,
                           self.climb4, self.climb4]
        #self.deathimage1 = pygame.image.load("assets/death/Fall (32x32).png")
        #self.deathimage2 = pygame.image.load("assets/death/Appearing (96x96)2.png")
        #self.deathimage3 = pygame.image.load("assets/death/Appearing (96x96)3.png")
        #self.deathimage4 = pygame.image.load("assets/death/Appearing (96x96)4.png")
        #self.deathimage5 = pygame.image.load("assets/death/Appearing (96x96)5.png")
        #self.deathimage6 = pygame.image.load("assets/death/Appearing (96x96)6.png")
        #self.deathimage6 = pygame.transform.scale(self.deathimage6, (56, 56))
        #self.deathimage7 = pygame.image.load("assets/death/Appearing (96x96)7.png")
        #self.deathimage7 = pygame.transform.scale(self.deathimage7, (56, 56))
        #self.deathimage8 = pygame.image.load("assets/death/Appearing (96x96)8.png")
        #self.deathimage8 = pygame.transform.scale(self.deathimage8, (56, 56))
        #self.deathimage9 = pygame.image.load("assets/death/costume1.png")
        self.frame = [self.image, self.image2, self.image3, self.image4, self.image5, self.image6]
        self.frame2 = [self.image7, self.image8, self.image9, self.image10, self.image11, self.image12]
        #self.deathframe = [self.deathimage1, self.deathimage2, self.deathimage3, self.deathimage4, self.deathimage5,
                           #self.deathimage6, self.deathimage7, self.deathimage8, self.deathimage9]

        self.index = 1#variable
        self.surface = self.frame[self.index]#variable
        self.rect = self.image.get_rect()#variable
        self.velocity_right = 1#variable
        self.velocity_left =1#variable
        self.rect.y = -1000#variable
        self.rect.x = 1000#variable
        self.x = 0#variable
        self.mouvAlert = False#variable

    





    def move_right(self):#fonction qui fait deplacer le joueur vers la droite
        if self.vie == True and self.game.mouv == True:
            x = 0
            p = 0
            for i in range(len(self.game.blocktab)):#regarde si le personnage ne touche aucun block
                if not self.game.blocktab[i][4][5] == 4:
                    if (self.game.blocktab[i][4][5] == 0 or self.game.blocktab[i][4][5] == 3) and self.rect.x + self.velocity_right + self.rect.width >= self.game.blocktab[i][0] and not self.rect.x+self.rect.width >= self.game.blocktab[i][0]+10 and self.rect.y+self.rect.height-1 > self.game.blocktab[i][1] and self.rect.y < self.game.blocktab[i][1] + self.game.blocktab[i][3]-1:
                        x += 1
                        p = i
            if x == 0:
                self.rect.x += self.velocity_right
                self.surface = self.frame[self.index]
                self.mouvAlert = False
                if self.game.verify_mouvO == True:
                    self.game.avancementO += self.velocity_right
            else:
                self.rect.x += self.game.blocktab[p][0] - self.rect.x-self.rect.width
                self.mouvAlert = True
                if self.game.verify_mouvO == True:
                    self.game.avancementO += self.game.blocktab[p][0] - self.rect.x-self.rect.width


    def move_left(self):#fonction qui fait deplacer vers la gauche le joueur
        if self.vie == True and self.game.mouv == True:
            x = 0
            p = 0
            for i in range(len(self.game.blocktab)):#regarde si le personnage ne touche aucun block
                if not self.game.blocktab[i][4][5] ==4:
                    if (self.game.blocktab[i][4][5] == 0 or self.game.blocktab[i][4][5] == 3) and self.rect.x - self.velocity_left <= self.game.blocktab[i][0]+self.game.blocktab[i][2] and not self.rect.x <= self.game.blocktab[i][0]+self.game.blocktab[i][2]-10 and self.rect.y + self.rect.height-1 > self.game.blocktab[i][1] and self.rect.y < self.game.blocktab[i][1] + self.game.blocktab[i][3] - 1:
                        x += 1
                        p = i
            if x == 0:
                self.rect.x -= self.velocity_left
                self.surface = self.frame2[self.index]
                self.mouvAlert = False
                if self.game.verify_mouvO1 == True :
                    self.game.avancementO -= self.velocity_left
                if self.rect.x>100:
                    self.game.avancementO = 0
            else:
                self.rect.x -= self.rect.x - (self.game.blocktab[p][0]+self.game.blocktab[p][2])
                if self.game.verify_mouvO1 == True:
                    self.game.avancementO -= self.rect.x - (self.game.blocktab[p][0]+self.game.blocktab[p][2])
                if self.rect.x>100:
                    self.game.avancementO = 0
                self.mouvAlert = True


    def alert(self, sauter, tomber):#cette fonction fait que le joueur tombe
        global double_saut
        sauter = False
        tomber = True
        double_saut[0] = False
        return sauter,tomber

    def check_colision(self, sauter):






        fichier2 = open('fichier/left.txt', mode='r+')
        left = int(fichier2.readline())
        fichier3 = open('fichier/right.txt', mode='r+')
        right = int(fichier3.readline())
        fichier = open('fichier/verify.txt', mode='r+')
        nb = int(fichier.readline())
        if nb == 2:
            verify = True
        else:
            verify = False
        fichier.close()
        if right == 1:
            self.right2 = True
        else:
            self.right2 = False
        if left == 1:
            self.left2 = True
        else:
            self.left2 = False




    def sauter(self,X): #fonction qui fait que le joueur saute
        if self.vie ==True:

            x = 0

            for i in range(len(self.game.tab)):
                if (self.game.blocktab[i][4][4] == True or self.x == 0) and not self.game.blocktab[i][4][5] ==4:
                    if self.rect.y - X <= self.game.blocktab[i][1] + self.game.blocktab[i][3] and self.rect.x + self.rect.width > self.game.blocktab[i][0] and self.rect.x < self.game.blocktab[i][0] + self.game.blocktab[i][2] and self.rect.y >= self.game.blocktab[i][1] + self.game.blocktab[i][3]:
                        if self.game.blocktab[i][4][4] == True:
                            self.x += 1
                        x += 1
                        self.rect.y += (self.game.blocktab[i][1] + self.game.blocktab[i][3]) - self.rect.y
                        return False
                else:
                    if not self.game.blocktab[i][4][5] ==4:
                        if self.rect.y - X <= self.game.blocktab[i][1] + self.game.blocktab[i][3] and self.rect.x + self.rect.width > self.game.blocktab[i][0] and self.rect.x < self.game.blocktab[i][0] + self.game.blocktab[i][2] and self.rect.y >= self.game.blocktab[i][1] + self.game.blocktab[i][3]:
                            self.rect.y += self.game.blocktab[i][1] - self.rect.y-self.rect.height
                            self.x += 1
            if self.rect.y - X < 30:
                x += 1
                self.rect.y += 30 - self.rect.y
                return False



            if x == 0:
                self.rect.y -= X
            if X>0:
                return True
            else:
                return False



    def tomber(self,X):#fonction qui fait que le joueur tombe
        for i in range(len(self.game.tab)):
            if len(self.game.tab)>0 and not self.game.blocktab[i][4][5] ==4 and not self.game.blocktab[i][4][8][0] ==3:
                if self.rect.y - X + self.rect.height >= self.game.blocktab[i][1] and not self.rect.y > self.game.blocktab[i][1] and \
                        self.game.blocktab[i][0] < self.rect.x + self.rect.width and self.rect.x < self.game.blocktab[i][0] + \
                        self.game.blocktab[i][2]:
                    X = self.rect.y + self.rect.height - self.game.blocktab[i][1] - 1
                    self.rect.y -= X
                    return False
        if self.vie == True:
            if self.rect.y-X+self.rect.height > self.game.flat.rect2.y:
                X = self.rect.y+self.rect.height - self.flat.rect2.y
                self.rect.y -= X
                return False

            self.rect.y -= X
            return True

















    def _vie(self): #importation des image de coeur
        self.vie_image_none = pygame.image.load('assets/vie/heartDisplay1.png')
        self.vie_image_half = pygame.image.load('assets/vie/heartDisplay2.png')
        self.vie_image_full = pygame.image.load('assets/vie/heartDisplay3.png')

        self.vie_image_none = pygame.transform.scale(self.vie_image_none, (32, 32))
        self.vie_image_half = pygame.transform.scale(self.vie_image_half, (32, 32))
        self.vie_image_full = pygame.transform.scale(self.vie_image_full, (32, 32))

        self.vie_images = self.vie_image_full
        
        self.vie_images_pos = self.vie_images.get_rect()


        




    def draw_vie(self, screen):#desine les coeurs
        self.vie_images_pos.x = 10
        self.vie_images_pos.y = 10
        for i in range(self.health):
            self.vie_images = self.vie_image_full
            
            screen.blit(self.vie_images, (self.vie_images_pos.x, self.vie_images_pos.y))

            self.vie_images_pos.x += 32
        
        for i in range(self.max_health-self.health):
            self.vie_images = self.vie_image_none
            
            screen.blit(self.vie_images, (self.vie_images_pos.x, self.vie_images_pos.y))

            self.vie_images_pos.x += 32


        
        
        
        
        
































