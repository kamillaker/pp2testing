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

# New event to increase speed
INC_SPEED = pg.USEREVENT+1
pg.time.set_timer(INC_SPEED ,1000)

# New event to rotate in 0.1 seconds coin
INC_COIN_ID = pg.USEREVENT+2
pg.time.set_timer(INC_COIN_ID,100)

# Variables needed
SPEED = 5
SCORES = 0
coin_id = 1
x = rd.randint(1,350)
y = rd.randint(80,500)

#image loader
_image_library = {}
def get_img(path):
    global _image_library
    image = _image_library.get(path)
    if image == None :
        canonicalized_path = path.replace("\\", os.sep).replace("/", os.sep)  
        image = pg.transform.scale(pg.image.load(canonicalized_path) , (50,50))
        _image_library[canonicalized_path] = image
    return image

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r"./resources/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (width//2 , height-80 )

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

# Setting up Sprites
P1 = Player()
E1 = Enemy()

# creating groups
enemies = pg.sprite.Group()
all_sprites = pg.sprite.Group()
enemies.add(E1)
all_sprites.add(P1,E1)

# Game Loop
done = False 
while not done :
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == INC_SPEED:
            SPEED += 1
        if event.type == INC_COIN_ID:
            coin_id += 1

    # Updating graphics of scores 
    scores = font.render("Scores:"+str(SCORES), True, 'black')

    screen.blit(bg, (0,0))
    screen.blit(scores, (250,10))

    # Coins 
    if coin_id == 7:
        coin_id = 1
    coin = get_img(f".\\resources\\coin{coin_id}"+".png")
    screen.blit(coin , (x , y))
    if P1.rect.colliderect((x,y, 50,50)):
        x = rd.randint(1,350)
        y = rd.randint(90,500)
        SCORES += 1
    
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

        # sprite from the group will no longer be drawn to the screen
        for entity in all_sprites:
            entity.kill()

        time.sleep(2) #for showing red screen
        pg.quit()
        sys.exit()
        
    clock.tick(FPS)
    pg.display.flip()