import pygame
class Monster(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        #variable
        self.game = game
        self.health = 3
        self.max_health = 3
        self.mouv = 0
        self.sauter = False
        self.tomber = False
        self.X = 0
        self.fonction = 0
        #importation image
        self.image1 = pygame.image.load('assets/goblin/Goblin1.png')
        self.image2 = pygame.image.load('assets/goblin/Goblin2.png')
        self.image3 = pygame.image.load('assets/goblin/Goblin3.png')
        self.image4 = pygame.image.load('assets/goblin/Goblin4.png')
        self.image5 = pygame.image.load('assets/goblin/Goblin5.png')
        self.imager1 = pygame.image.load('assets/goblin/Goblinr1.png')
        self.imager2 = pygame.image.load('assets/goblin/Goblinr2.png')
        self.imager3 = pygame.image.load('assets/goblin/Goblinr3.png')
        self.imager4 = pygame.image.load('assets/goblin/Goblinr4.png')
        self.imager5 = pygame.image.load('assets/goblin/Goblinr5.png')

        #tableau utiliser pour l'annimation
        self.index = 0
        self.frameimage = [self.image1,self.image1,self.image2,self.image2,self.image3,self.image3,self.image4,self.image4,self.image5,self.image5]
        self.frameimager = [self.imager1, self.imager1, self.imager2, self.imager2, self.imager3, self.imager3, self.imager4,self.imager4, self.imager5, self.imager5]
        self.image = self.frameimage[self.index]
        self.rect = self.image.get_rect()


    def iadeplacemnt(self):#ia du monstre
        for monster in self.game.all_monster:
            print(monster.fonction)

            x = 0
            if self.game.player.rect.x > monster.rect.x:
                for i in range(len(self.game.blocktab)):
                    if not self.game.blocktab[i][4][5] == 4:
                        if (self.game.blocktab[i][4][5] == 0 or self.game.blocktab[i][4][5] == 3) and monster.rect.x + 2 + monster.rect.width >= self.game.blocktab[i][0] and not monster.rect.x+monster.rect.width >= self.game.blocktab[i][0]+10 and monster.rect.y+monster.rect.height > self.game.blocktab[i][1] and monster.rect.y < self.game.blocktab[i][1] + self.game.blocktab[i][3]-1:
                            x = 1
                            ii=i
                if x==0:
                    monster.mouv = 2
                    monster.rect.x += 2








            elif self.game.player.rect.x < monster.rect.x:
                x=0
                ii=0
                for i in range(len(self.game.blocktab)):
                    if not self.game.blocktab[i][4][5] == 4:
                        if (self.game.blocktab[i][4][5] == 0 or self.game.blocktab[i][4][5] == 3) and monster.rect.x - 2 <=self.game.blocktab[i][0] + self.game.blocktab[i][2] and not monster.rect.x <= self.game.blocktab[i][0] + self.game.blocktab[i][2] - 10 and monster.rect.y + monster.rect.height - 1 > self.game.blocktab[i][1] and monster.rect.y < self.game.blocktab[i][1] + self.game.blocktab[i][3] - 1:
                            x = 1
                            ii = i


                if x==0:
                    monster.mouv = -2
                    monster.rect.x -= 2







            else:
                monster.mouv = 0


    def modify_apparence(self):#change l'image des monstre
        for i in self.game.all_monster:
            if i.mouv<0:
                i.image = i.frameimage[i.index]
                if i.index < len(i.frameimage) - 1:
                    i.index += 1
                else:
                    i.index = 0
            elif i.mouv>0:
                i.image = i.frameimager[i.index]
                if i.index < len(i.frameimage) - 1:
                    i.index += 1
                else:
                    i.index = 0
            else:
                pass


    def tombere(self,block):#graviter du monstre
        for i in range(len(self.game.tab)):
            if len(self.game.tab)>0 and not self.game.blocktab[i][4][5] == 4 and not self.game.blocktab[i][4][8][0] == 3:
                if block.rect.y - block.X + block.rect.height >= self.game.blocktab[i][1] and not block.rect.y > self.game.blocktab[i][1] and \
                        self.game.blocktab[i][0] < block.rect.x + block.rect.width and block.rect.x < self.game.blocktab[i][0] + \
                        self.game.blocktab[i][2]:
                    block.X = block.rect.y + block.rect.height - self.game.blocktab[i][1] - 1
                    block.rect.y -= block.X
                    return False

        block.rect.y -= block.X
        return True



    def verify(self,block):#verifie la colison avec des block
        if block.sauter == False and block.tomber == False:
            x = 0
            for i in range(len(self.game.blocktab)):
                if self.game.blocktab[i][4][8][0] == 0:
                    if block.rect.colliderect(self.game.blocktab[i][0], self.game.blocktab[i][1], self.game.blocktab[i][2],self.game.blocktab[i][3]):
                        x += 1
            if x == 0:
                block.tomber = True
                block.X = 0
                print("yo")
                block.X -= 3
                block.tomber = self.tombere(block)

        if block.tomber == True:
            block.X -= 3
            block.tomber = self.tombere(block)




