import pygame
class Magic(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        #variable
        self.game = game
        self.magic = 0
        self.frame = []
        self.index = 0
        self.rect = 0
        self.angle = 0
        self.direction = 'droite'
    def check_collision(self):
        #voit si une boule de feu rentre en collision avec un block
        for magic in self.game.all_magic:
            if magic.magic==1:
                for block in self.game.all_blockx:
                    if block.rect.colliderect(magic.rect):
                        magic.remove()
    def remove(self):
        #supprime une boule de feu
        self.game.all_magic.remove(self)

