import pygame
class Object(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()#inisialisation
        #variable
        self.game = game
        self.image = pygame.image.load('assets/objet/Apple.png')
        self.coinimage1 = pygame.image.load('assets/objet/coin/Coin1.png')
        self.coinimage2 = pygame.image.load('assets/objet/coin/Coin2.png')
        self.coinimage3 = pygame.image.load('assets/objet/coin/Coin3.png')
        self.coinimage4 = pygame.image.load('assets/objet/coin/Coin4.png')
        self.coinimage5 = pygame.image.load('assets/objet/coin/Coin5.png')
        self.coinimage6 = pygame.image.load('assets/objet/coin/Coin6.png')
        self.coinimage7 = pygame.image.load('assets/objet/coin/Coin7.png')
        self.coinimage8 = pygame.image.load('assets/objet/coin/Coin8.png')
        self.coinframe = [self.coinimage1,self.coinimage1,self.coinimage2,self.coinimage2,self.coinimage3,self.coinimage3,self.coinimage4,self.coinimage4,self.coinimage5,self.coinimage5,self.coinimage6,self.coinimage6,self.coinimage7,self.coinimage7,self.coinimage8,self.coinimage8]
        self.coinindex = 0
        self.coin = 0





        self.rect = self.image.get_rect()
        self.animation_index = [pygame.image.load('assets/colect/Collected1.png'),pygame.image.load('assets/colect/Collected2.png'),pygame.image.load('assets/colect/Collected3.png'),pygame.image.load('assets/colect/Collected4.png'),pygame.image.load('assets/colect/Collected5.png'),pygame.image.load('assets/colect/Collected6.png')]
        self.rectA = pygame.image.load('assets/colect/Collected1.png').get_rect()
        self.boucle = 0
        self.x = True
        self.port = pygame.image.load('assets/background/porte2.png')
        self.port = pygame.transform.scale(self.port, (72,100))
    def remove(self):#supprime une piece
        self.game.all_object.remove(self)


    def check(self):#colison avec le personnage
        for player in self.game.check_collision(self, self.game.all_players):
            for i in range(len(self.game.objecttab)):
                if self.game.objecttab[i][0]==self.rect.x and self.game.objecttab[i][1]==self.rect.y and self.game.objecttab[i][2] ==0:
                    self.game.objecttab[i][2] = 1
            self.game.coin += 1
            self.game.audio.chan0.play(self.game.audio.ring)
            self.remove()


























