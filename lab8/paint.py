"""Extend example project from https://nerdparadise.com/programming/pygame/part6 and add the following functionality:

Draw rectangle
Draw circle
Eraser
Color selection

"""

import pygame as pg

pg.init()

height = 600
width = 800

screen = pg.display.set_mode((width,height))
base_layer = pg.Surface((width,height))
base_layer.fill('white')
screen.fill((255,255,255))

LMBpressed = False

thickness = 2
currX = 0
currY = 0
prevX = 0
prevY = 0

drawLine = False
drawCircle = False
drawRect = False
eraser = False

colorRED = (255,0,0)
colorWHITE = (255,255,255)
colorBLACK = (0, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0,0,255)
colorYELLOW = (255,255,0)
drawing_color = colorBLACK

class Botton():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    # function draws rect on given surface
    def draw(self , win):
        pg.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pg.draw.rect(win, colorBLACK, (self.x, self.y, self.width, self.height), 2)
    
    # checking 
    def clicked (self, pos):
        x , y = pos
        if not(x >= self.x and x <= self.x+self.width):
            return False
        if not(y >= self.y and y <= self.y+self.height):
            return False
        return True

botton_len = 20
bottons = [
    Botton(710, 10, botton_len, botton_len, colorRED),
    Botton(740, 10, botton_len, botton_len, colorBLACK),
    Botton(770, 10, botton_len, botton_len, colorBLUE),
    Botton(710, 40, botton_len, botton_len, colorGREEN),
    Botton(740, 40, botton_len, botton_len, colorWHITE),
    Botton(770, 40, botton_len, botton_len, colorYELLOW)
]

#drawing menu
for botton in bottons:
    botton.draw(screen)
    botton.draw(base_layer)

#dividing line the menu and  surface to draw
pg.draw.line(screen, colorBLACK, (0,70), (800,70))
pg.draw.line(base_layer, colorBLACK, (0,70), (800,70))

# for finding circle's center
def coor_circle_center(currX, currY, prevX, prevY):
    maxX = max(prevX, currX)
    maxY = max(prevY, currY)
    minX = min(prevX, currX)
    minY = min(prevY, currY)
    return tuple((((maxX - minX)/2)+minX , ((maxY- minY)/2)+minY )), (maxX - minX)/2

done = False 
while not done :
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN: 
            if event.key == pg.K_EQUALS:
                thickness += 1
            if event.key == pg.K_MINUS:
                thickness -= 1
            if event.key == pg.K_r:
                drawRect = True
                drawCircle = False
                drawLine = False
                eraser = False
            elif event.key == pg.K_c:
                drawCircle = True
                drawRect = False 
                drawLine = False
                eraser = False        
            elif event.key == pg.K_l:
                drawLine = True
                drawCircle = False
                drawRect = False 
                eraser = False
            elif event.key == pg.K_e:
                eraser = True
                drawCircle = False
                drawRect = False 
                drawLine = False
        
        # to not to save every drawing , when mouse moving
        if LMBpressed:
            screen.blit(base_layer, (0,0))

        #checking if sth was chosen from menu
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and event.pos[1]<70: 
            for botton in bottons:
                if botton.clicked(event.pos):
                    drawing_color = botton.color # changing color to botton's color

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and event.pos[1]>70:
            print("lmb pressed")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
            # to draw dot when we just press and release in the beginning
            if drawLine :
                currX = event.pos[0]
                currY = event.pos[1]

        if event.type == pg.MOUSEMOTION and event.pos[1]>70:
            if LMBpressed :
                #  changing current position to mouse's pos  
                currX = event.pos[0]
                currY = event.pos[1]

                if drawRect:
                    pg.draw.rect(screen, drawing_color, (min(prevX, currX), min(prevY, currY), abs(currX-prevX), abs(currY-prevY) ), thickness)
                if drawCircle:
                    tup,  rad = coor_circle_center(currX, currY, prevX, prevY)
                    pg.draw.circle(screen, drawing_color, tup, rad, thickness)
                if drawLine:
                    pg.draw.line(screen, drawing_color, (prevX,prevY), (currX,currY) , thickness )
                if eraser:
                    pg.draw.rect(screen , colorWHITE, (currX,currY, thickness,thickness))
                    base_layer.blit(screen, (0,0))

        
        if event.type == pg.MOUSEBUTTONUP and event.button == 1 and event.pos[1] >70:
            print("lmb is released")
            LMBpressed = False
            if not drawLine: # last pos for figures , etc
                currX = event.pos[0]
                currY = event.pos[1]
            if drawRect:
                pg.draw.rect(screen, drawing_color, (min(prevX, currX), min(prevY, currY), abs(currX-prevX), abs(currY-prevY) ), thickness)
            if drawCircle:
                tup,  rad = coor_circle_center(currX, currY, prevX, prevY)
                pg.draw.circle(screen, drawing_color, tup, rad, thickness)

            # saving after drawing
            base_layer.blit(screen, (0,0))

    if drawLine:
        prevX = currX
        prevY = currY
        #to save every (line) mousemotion 
        base_layer.blit(screen, (0,0))
    
    pg.display.flip()
