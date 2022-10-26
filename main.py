import pygame
import random

from Game import Main
from Enemy import ShadowEnemy

from tkinter import simpledialog

pygame.init()

WIDTH = 1200
HEIGHT = 650


screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Harry Potter Game")

icon = pygame.image.load("img/potter-icon.png")
pygame.display.set_icon(icon)

magic_voice = pygame.mixer.Sound("media/expecto-patronum.mp3")
bg_music = pygame.mixer.Sound("media/bg-music-hp.wav")
space_voice = pygame.mixer.Sound("media/media_success_click.wav")


bg_music.play(0,-1)
magic_voice.set_volume(0.2)

fps = 60
clock = pygame.time.Clock()
    
class Player(pygame.sprite.Sprite and ShadowEnemy):
    def __init__(self,x,y,group_of_enemy):
        super().__init__(0,0)
        self.group_of_enemy = group_of_enemy
        self.score = 0
        self.lives = 3
        self.font_score = pygame.font.Font("fonts/Harry.ttf",54)
        self.font_header = pygame.font.Font("fonts/Harry.ttf",65)
        self.font_time = pygame.font.Font("fonts/Harry.ttf",40)
        self.lose_font = pygame.font.Font("fonts/Harry.ttf",65)
        self.font_lives = pygame.font.Font("fonts/Harry.ttf",30)
        self.image = pygame.image.load("img/potter-icon.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.round_time = 0
        self.slow_time = 0
        self.name = simpledialog.askstring("Game","What is your name ? ")


    def update(self):

        self.slow_time += 1
    
        if(self.slow_time == fps):
            self.round_time += 1
            self.slow_time = 0


        self.time_text()
        self.move()
        self.collision()
        self.header_line()
        self.header_text()
        self.defeat()
        self.Win()


    def time_text(self):
        self.text_time = self.font_time.render(f"time : {self.round_time}",True,(255,255,0))
        screen.blit(self.text_time,(1010,15))
        
    def header_text(self):
        self.text_header = self.font_header.render("Harry Potter Game",True,(255,255,0))
        screen.blit(self.text_header,(420,15))
        
    def header_line(self):
        pygame.draw.line(screen,(255, 255, 0),(0,85),(1200,85))

    def move(self):
        keys = pygame.key.get_pressed()

        self.speed = 18

        if(keys[pygame.K_UP] and self.rect.top > 85):
            self.rect.y -= self.speed
        
        if(keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT):
            self.rect.y += self.speed
        
        if(keys[pygame.K_LEFT] and self.rect.left > 0):
            self.rect.x -= self.speed

        if(keys[pygame.K_RIGHT] and self.rect.right < WIDTH):
            self.rect.x += self.speed    

    def collision(self):
        if pygame.sprite.spritecollide(self,self.group_of_enemy,True):
            enemy_shadow = ShadowEnemy(random.randint(30,1100),random.randint(175,500))
            EnemyShadow_group.remove(enemy_shadow)
            EnemyShadow_group.add(enemy_shadow)
            self.score += 1
            magic_voice.play()

        self.text_score = self.font_score.render(f"score : {self.score}",True,(255,255,0))
        screen.blit(self.text_score,(30,30))

    def defeat(self):
        self.lose_text = self.lose_font.render("Prohal jsi stistkni mezernik a hraj znovu",True,(255,255,0))

        if self.round_time >= 20 and self.score < 20:
            screen.blit(self.lose_text,(WIDTH//2 - 340,HEIGHT//2 - 40))
            self.speed = 0
            self.speed_enemy = 0
        
        self.keys = pygame.key.get_pressed()

        if(self.keys[pygame.K_SPACE]):
            self.score = 0
            self.text_victory = ""
            self.round_time = 0
            self.slow_time = 0
            self.speed = 10
            self.speed_enemy = 10
            space_voice.play()

    def Win(self):

        self.p = 20

        if self.score >= 20:
            self.winner_font = pygame.font.Font("fonts/Harry.ttf",43)
            self.text_victory = "Zvitezil jsi Stitskni mezernik a hraj znovu"
            self.text_win = self.winner_font.render(self.text_victory,True,(255,255,0))
            screen.blit(self.text_win,(WIDTH//2 - 240,HEIGHT//2 -40))

            self.list_winner:list = []

            with open("winner_list.txt","w") as file:
                self.list_winner.append(self.name)
                
                for self.username in self.list_winner:
                    file.write(f"Winner is : {self.username} \n")

            keys = pygame.key.get_pressed()

            if(keys[pygame.K_SPACE]):
                self.score = 0
                self.text_victory = ""
                self.round_time = 0
                self.slow_time = 0
                space_voice.play()

         
run = True

bg_group = pygame.sprite.Group()
bg_image = Main(WIDTH//2,HEIGHT//2)
bg_group.add(bg_image)

EnemyShadow_group = pygame.sprite.Group()
enemy_shadow = ShadowEnemy(490,360)
EnemyShadow_group.add(enemy_shadow)

players_group = pygame.sprite.Group()
player = Player(250,350,EnemyShadow_group)
players_group.add(player)

while run:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False

    screen.fill((0,0,0))
    
    bg_group.draw(screen)
    players_group.draw(screen)
    EnemyShadow_group.draw(screen)
    
    players_group.update()
    EnemyShadow_group.update()
    players_group.draw(screen)


    pygame.display.update()
    clock.tick(fps)

pygame.quit()