import pygame

pygame.init()
s_w = 500
s_h = 500
screen = pygame.display.set_mode((s_w,s_h))

rad = 25
diameter = rad * 2

x = s_w // 2
y = s_h // 2

s = 20

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= s
            if event.key == pygame.K_RIGHT:
                x += s
            if event.key == pygame.K_DOWN:
                y += s
            if event.key == pygame.K_UP:
                y -= s
                
    # Adjust position if circle is going out of bounds
    if x - rad < 0:
        x = rad
    elif x + rad > s_w:
        x = s_w - rad
    if y - rad < 0:
        y = rad
    elif y + rad > s_h:
        y = s_h - rad
    
    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, [255, 0, 0], (x, y), rad)
    
    pygame.display.update()

pygame.quit()