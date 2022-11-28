import pygame
import random
import time

pygame.init()

WIDTH = 1200
HEIGHT = 650



class ShadowEnemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("img/mozkomor.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.x = random.choice([-1,1])
        self.y = random.choice([-1,1])
        self.speed_enemy = 6
        

    def update(self):

        self.rect.x += self.x * self.speed_enemy
        self.rect.y += self.y * self.speed_enemy

        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.x= -1 * self.x
            time.sleep(0.001)
        
        if self.rect.top < 100 or self.rect.bottom > HEIGHT - 100:
            self.y = -1 * self.y