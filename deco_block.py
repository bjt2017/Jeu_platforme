import pygame

class Deco_block(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        #variable
        self.game = game
        self.image = pygame.image.load("assets/Idle.png")
        self.rect = self.image.get_rect()
    def remove(self):#suppresion du sprite
        self.game.all_deco_block.remove(self)