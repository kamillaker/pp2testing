#Imports
import pygame as pg
import random as rd
import sys
import time
import os

# Frame per second
clock = pg.time.Clock()
FPS = 60

#initialzing
pg.init()

# Screen setting
height = 600
width = 400
screen = pg.display.set_mode((width,height))
bg = pg.image.load(r"./resources/AnimatedStreet.png")
screen.fill((255,255,255))

# Setting up Font
font = pg.font.Font(r"./resources/BebasNeue-Regular.ttf" , 50)

# Variables needed
SPEED = 5
SCORES = 0


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r"./resources/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (width//2 , height-80)

    def move(self):
        pressed = pg.key.get_pressed()
        if pressed[pg.K_UP] and self.rect.top>0  :
            self.rect.move_ip(0,-5)
        if pressed[pg.K_DOWN] and self.rect.bottom<height :
            self.rect.move_ip(0,5)
        if pressed[pg.K_LEFT] and self.rect.left>0:
            self.rect.move_ip(-5,0)
        if pressed[pg.K_RIGHT] and self.rect.right < width :
            self.rect.move_ip(5,0)

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r"./resources/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (rd.randint(self.rect[2]//2, width - self.rect[2]//2) , 80 )

    def move(self):
        if self.rect.bottom < height :
            self.rect.move_ip(0,SPEED)
        else:
            self.rect.center = (rd.randint(self.rect[2]//2, width - self.rect[2]//2) , 35 )

class Coin_1(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r"./resources/coin1.png")
        self.image = pg.transform.scale(self.image , (40,40))
        self.rect = self.image.get_rect()
        self.rect.center = (rd.randint(40, width - 40) , 0)

    def move(self):
        if self.rect.bottom < height :
            self.rect.move_ip(0,SPEED)
        else:
            self.rect.center = (rd.randint(40, width - 40) , 0)

        

class Coin_5(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r"./resources/coin5.png")
        self.image = pg.transform.scale(self.image , (40,40))
        self.rect = self.image.get_rect()
        self.rect.center = (rd.randint(40, width - 40) ,0)

    def move(self):
        if self.rect.bottom < height :
            self.rect.move_ip(0,SPEED)
        else:
            self.rect.center = (rd.randint(40, width - 40) , 0)

class Sandyq(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r"./resources/sandyq.png")
        self.image = pg.transform.scale(self.image , (40,40))
        self.rect = self.image.get_rect()
        self.rect.center = (rd.randint(40, width - 40) , 0)

    def move(self):
        if self.rect.bottom < height :
            self.rect.move_ip(0,SPEED)
        else:
            self.rect.center = (rd.randint(40, width - 40) , 0)

# Setting up Sprites
C1 = Coin_1()
C5 = Coin_5()
S = Sandyq()
P1 = Player()
E1 = Enemy()

# creating groups
coins1 = pg.sprite.Group()
coins5 = pg.sprite.Group()
coins50 = pg.sprite.Group()
enemies = pg.sprite.Group()
all_sprites = pg.sprite.Group()
enemies.add(E1)
all_sprites.add(P1,E1,C1,C5,S)
coins1.add(C1)
coins5.add(C5)
coins50.add(S)


# Game Loop
done = False 
while not done :
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
       
    # Updating graphics of scores 
    scores = font.render("Scores:"+str(SCORES), True, 'black')

    screen.blit(bg, (0,0))
    screen.blit(scores, (100,10))
    
    # Check for collision with coins1
    coin1_collide = pg.sprite.spritecollide(P1,coins1,True)
    for coin in coin1_collide:
        SCORES+=1
        new_coin1 = Coin_1()
        coins1.add(new_coin1)
        all_sprites.add(new_coin1)
        new_coin1.rect.top = 0
        new_coin1.rect.center = (rd.randint(40, width - 40), 0)
        if SCORES%10==0:  #adding more new coins and increasing speed 
            SPEED+=1
            new_coin5 = Coin_5()
            coins5.add(new_coin5)
            all_sprites.add(new_coin5)
        if SCORES%50==0: #adding new coins  and increasing speed 
            SPEED+=1
            new_coin50 = Sandyq()
            coins50.add(new_coin50)
            all_sprites.add(new_coin50)
    
    # Check for collision with coins5
    coin5_collide = pg.sprite.spritecollide(P1,coins5,True)
    for coin in coin5_collide:
        SCORES+=5
        coin.kill()
    # Check for collision with coins50
    coin50_collide = pg.sprite.spritecollide(P1,coins50,True)
    for coin in coin50_collide:
        SCORES+=50
        coin.kill()

    # Move and blit to screen
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    # when collide Player to enemy
    if pg.sprite.spritecollideany(P1, enemies):
        pg.mixer.Sound(r"./resources/crash.wav").play()
        time.sleep(1) # to listen until the end of sound

        screen.fill((255,0,0))
        screen.blit(font.render("Game Over", True, 'black'), (120,260))
        screen.blit(scores, (180,320))
        pg.display.flip()

       

        time.sleep(2) #for showing red screen
        pg.quit()
        sys.exit()
        
    clock.tick(FPS)
    pg.display.flip()