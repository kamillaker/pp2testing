'''
Snake
Extend example project from lecture and add the following functionality:

Checking for border (wall) collision and whether the snake is leaving the playing area
Generate random position for food, so that it does not fall on a wall or a snake
Add levels. For example, when the snake receives 3-4 foods or depending on score 
Increase speed when the user passes to the next level
Add counter to score and level
Comment your code
'''
#imports
import pygame as pg
import random
import time

#initializing
pg.init()

#screen sets
width = 800
height= 600
screen = pg.display.set_mode((width, height))

clock = pg.time.Clock()
snake_speed = 10
score = 0
score_level = 0
level = 1

#for checking is our snake eat food
snake_pos = [100,60]

#snake body parts(by default the starting  4 blocks) 
snake_body = [
    [100,60], 
    [80,60],
    [60,60],
    [40,60],
]

#for checking if snake eat
food_eaten = False

#food's pos
food_pos = [random.randint(2,width//20)*20 ,random.randint(2,height//20)*20 ]

# current direction for checking to (by default to right)
direction = 'RIGHT'
#changing direction 
change_to = direction


def game_over():
    font = pg.font.Font(r".\resources\BebasNeue-Regular.ttf", 50)
    game_over_surface = font.render("Game Over", True, (0, 255, 0))
    screen.fill('red')
    score_surface = font.render("SCORES:"+str(score), True, (0, 255, 0))
    screen.blit(score_surface, score_surface.get_rect(center = (width//2+100,height//2+100)) )
    screen.blit(game_over_surface, game_over_surface.get_rect(center= (width//2,height//2)) )
    pg.display.flip()
    time.sleep(2)
    pg.quit()
    quit()

def score_to_screen():
    font = pg.font.Font(r".\resources\BebasNeue-Regular.ttf", 20)
    score_surface = font.render("SCORES:"+str(score), True, (0, 255, 0))
    screen.blit(score_surface, score_surface.get_rect(center = (150,10)) )

def level_to_screen():
    font = pg.font.Font(r".\resources\BebasNeue-Regular.ttf", 20)
    level_surface = font.render("level:"+str(level), True, (0, 255, 0))
    screen.blit(level_surface, level_surface.get_rect(center= (50,10)) )


done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                change_to = "RIGHT"
            if event.key == pg.K_LEFT:
                change_to = "LEFT"
            if event.key == pg.K_UP:
                change_to = "UP"
            if event.key == pg.K_DOWN:
                change_to = "DOWN"
    
    # CHECKING  TO NOT GO ON ITSELF
    if change_to=="RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    if change_to=="LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to=="UP" and direction != "DOWN":
        direction = "UP"
    if change_to=="DOWN" and direction != "UP":
        direction = "DOWN"

    if direction == "RIGHT":
        snake_pos[0] += 20
    if direction == "LEFT":
        snake_pos[0] -= 20
    if direction == "UP":
        snake_pos[1] -= 20
    if direction == "DOWN":
        snake_pos[1] += 20

    snake_body.insert(0, list(snake_pos) )
    if snake_pos[0]==food_pos[0] and snake_pos[1]==food_pos[1]:
        score += 10
        score_level+=10
        food_eaten = True
        if score_level > 50 :
            level+=1
            score_level =0 
            snake_speed +=1
    else:
        snake_body.pop()
    
    if food_eaten:
        cant_choose = False 
        food_pos =  [random.randint(2,width//20-1)*20 ,random.randint(2,height//20-1)*20 ]
        for i in snake_body:
                if i==food_pos:
                    cant_choose = True
                    break
        while cant_choose:
            cant_choose = False
            food_pos =  [random.randint(2,width//20-1)*20 ,random.randint(2,height//20-1)*20 ]
            for i in snake_body:
                if i==food_pos:
                    cant_choose = True
                    break

    for i in snake_body:
        if food_eaten :
            food_pos =  [random.randint(2,width//20-1)*20 ,random.randint(2,height//20-1)*20 ]
        if i==food_pos:
            food_pos =  [random.randint(2,width//20-1)*20 ,random.randint(2,height//20-1)*20 ]

        
    
    food_eaten= False
    screen.fill('black')
    pg.draw.line(screen ,(0,255,0), (0,20), (800, 20) )

    pg.draw.rect(screen, 'red',(snake_body[0][0],snake_body[0][1], 20,20))
    for pos in snake_body[1:]:
        pg.draw.rect(screen, 'yellow',(pos[0],pos[1], 20,20))

    pg.draw.rect(screen, 'white', (food_pos[0], food_pos[1], 20, 20))

    # Touching corners
    if snake_pos[0]>width-20 or snake_pos[0]<0 or snake_pos[1]<20 or snake_pos[1]>height-20 :
        game_over()
    
    # Touching own body
    for part in snake_body[1:]:
        if snake_pos == part:
            game_over()
    
    score_to_screen()
    level_to_screen()

    pg.display.update()
    clock.tick(snake_speed)
