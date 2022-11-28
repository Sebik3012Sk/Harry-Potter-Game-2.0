import pygame

WIDTH = 1200
HEIGHT = 650

pygame.init()

class Main(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos):
        super().__init__()
        self.image = pygame.image.load("img/bg-dementors.png")
        self.scaleImg = pygame.transform.scale(self.image,(WIDTH,HEIGHT))
        self.rect = self.scaleImg.get_rect()
        self.rect.center = (x_pos,y_pos)
        