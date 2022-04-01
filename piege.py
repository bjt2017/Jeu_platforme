import pygame

class Piege():
    def __init__(self,game):
        self.roue_image1 = pygame.image.load('assets/piege/On 1.png')
        self.roue_image2 = pygame.image.load('assets/piege/On 2.png')
        self.roue_image3 = pygame.image.load('assets/piege/On 3.png')
        self.roue_image4 = pygame.image.load('assets/piege/On 4.png')
        self.roue_image5 = pygame.image.load('assets/piege/On 5.png')
        self.roue_image6 = pygame.image.load('assets/piege/On 6.png')
        self.roue_image7 = pygame.image.load('assets/piege/On 7.png')
        self.roue_image8 = pygame.image.load('assets/piege/On 8.png')
        self.roue_image1 = pygame.transform.scale(self.roue_image1,(57,57))
        self.roue_image2 = pygame.transform.scale(self.roue_image2, (57, 57))
        self.roue_image3 = pygame.transform.scale(self.roue_image3, (57, 57))
        self.roue_image4 = pygame.transform.scale(self.roue_image4, (57, 57))
        self.roue_image5 = pygame.transform.scale(self.roue_image5, (57, 57))
        self.roue_image6 = pygame.transform.scale(self.roue_image6, (57, 57))
        self.roue_image7 = pygame.transform.scale(self.roue_image7, (57, 57))
        self.roue_image8 = pygame.transform.scale(self.roue_image8, (57, 57))
        self.roue_rect = self.roue_image1.get_rect()
        self.roue_index = [self.roue_image1,self.roue_image2,self.roue_image3,self.roue_image4,self.roue_image5,self.roue_image6,self.roue_image7,self.roue_image8]
        self.endroi = 0
        self.roue_rect.x = 1000
        self.roue_rect.y = 1000
        self.boucle = 0
        self.angle = 0
        self.game = game
    def roue_mouv(self):

        self.boucle += 1
        if self.boucle<=62:
            self.roue_rect.x -= 2
        elif 62<self.boucle<=93:
            self.roue_rect.y += 2
        elif 93<self.boucle<=155:
            self.roue_rect.x += 2
        elif 155<self.boucle<=186:
            self.roue_rect.y -= 2
        else:
            self.boucle = 0
    def rotate(self):
        self.roue_image = self.roue_index[self.endroi]
        if self.endroi==7:
            self.endroi = 0
        else:
            self.endroi += 1
    def toucher(self):
        if self.roue_rect.colliderect(self.game.player.rect):

            self.game.player.vie = False


