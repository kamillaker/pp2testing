import pygame

pygame.init()
list_music = ["mus1.mp3", "mus2.mp3", "mus3.mp3", "mus4.mp3"]


SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)


pause = False



WHITE = (255, 255, 255)
x = 25
y = 25
l = 1050 
w = 650  


clock = pygame.time.Clock()
screen = pygame.display.set_mode((l, w))
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if pause == False:
                    pygame.mixer.music.pause()
                    pause = True
                else:
                    pygame.mixer.music.unpause()
                    pause = False
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.load(list_music[0])
                pygame.mixer.music.play(0)
            if event.key == pygame.K_x:
                list_music = list_music[1:] + [list_music[0]] # move current song to the back of the list
                pygame.mixer.music.load(list_music[0])
                pygame.mixer.music.play()
            if event.key == pygame.K_z:
                list_music = [list_music[-1]] + list_music[0:-1] #move last song to the front of the list
                pygame.mixer.music.load(list_music[0])
                pygame.mixer.music.play()

        if event.type == SONG_END:
            print("song end")


    screen.fill(WHITE)

    pygame.display.flip()

    clock.tick(20)