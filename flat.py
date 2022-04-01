import pygame
class Flat:
    def __init__(self):
        super().__init__()
        self.moving = 4
        self.image = pygame.image.load('assets/background/Terrain.png')
        self.image2 = pygame.image.load("assets/Idle.png")
        self.rect = self.image.get_rect()
        self.image2 = pygame.transform.scale(self.image2, (64, 64))
        self.rect2 = self.image2.get_rect()
        self.rect2.x = 1000
        self.rect2.y = 1000
        self.rect.x = 1000
        self.rect.y = 1000





