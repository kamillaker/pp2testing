#imports
import pygame
import random
import sys
import psycopg2
import time

# Database connection setup
def connect_database():
    try:
        conn = psycopg2.connect(host="localhost", database="PhoneBook", user="postgres", password="59500")
        initialize_database(conn)
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

#creating database if it doesnt exist and task username as key, so they dont repeat
def initialize_database(conn):
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(255) PRIMARY KEY,
            userlevel INT NOT NULL DEFAULT 1,
            score INT NOT NULL DEFAULT 0
        );
    ''')
    conn.commit()

# Pygame initialization
pygame.init()
window_x, window_y = 720, 480
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Snake')
fps = pygame.time.Clock()

# Game variables
snake_speed = 15
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
fruit_position = [random.randrange(5, (window_x//12)) * 10, random.randrange(5, (window_y//12)) * 10]
fruit_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0
level = 1
paused = False
walls = []

# Game states
GAME_STATE_INIT = 'initializing'
GAME_STATE_PLAYING = 'playing'
GAME_STATE_PAUSED = 'paused'
game_state = GAME_STATE_INIT

# Colors
black, white, red, green = pygame.Color(0, 0, 0), pygame.Color(255, 255, 255), pygame.Color(255, 0, 0), pygame.Color(0, 255, 0)

# Input box for username
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = white
        self.text = text
        self.font = pygame.font.Font(None, 32)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = red if self.active else white
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                    self.handle_login()
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        if game_state == GAME_STATE_INIT:
            screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
            pygame.draw.rect(screen, self.color, self.rect, 2)

    #if user exists put his stats
    def handle_login(self):
        global username, level, score, game_state
        username = self.text
        self.text = ''
        user_data = check_user(conn, username)
        if user_data:
            level, score = user_data
        else:
            insert_new_user(conn, username)
        game_state = GAME_STATE_PLAYING  # Transition to playing state

#checking in database for user
def check_user(conn, username):
    cur = conn.cursor()
    cur.execute("SELECT userlevel, score FROM users WHERE username = %s;", (username,))
    return cur.fetchone()

#entering new user to database
def insert_new_user(conn, username):
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username) VALUES (%s) ON CONFLICT DO NOTHING;", (username,))
    conn.commit()

#saving current data
def save_game_state(conn, username, level, score):
    cur = conn.cursor()
    cur.execute("UPDATE users SET userlevel = %s, score = %s WHERE username = %s;", (level, score, username))
    conn.commit()

#gameover condition
def check_wall_collisions(snake_position):
    for wall in walls:
        if wall[0] <= snake_position[0] < wall[0] + wall[2] and wall[1] <= snake_position[1] < wall[1] + wall[3]:
            return True
    return False

#obstacles for each level
def update_level_settings():
    global snake_speed, walls
    if level == 1:
        snake_speed = 10
        walls = []
    elif level == 2:
        snake_speed = 12
        walls = [(200, 150, 10, 100), (500, 150, 10, 100)]  # Example walls
    elif level == 3:
        snake_speed = 15
        walls = [(200, 150, 10, 100), (500, 150, 10, 100), (300, 300, 200, 10)]

#drawing walls
def draw_walls():
    for wall in walls:
        pygame.draw.rect(game_window, pygame.Color(139, 69, 19), pygame.Rect(wall))

#call to update level settings when the level changes
if score >= 100 and level == 1:
    level = 2
    update_level_settings()
elif score >= 200 and level == 2:
    level = 3
    update_level_settings()



#level and score blitting
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    level_surface = score_font.render('Level : ' + str(level), True, color)
    level_rect = level_surface.get_rect()
    level_rect.topright = (window_x - 10, 0)
    game_window.blit(level_surface, level_rect)
    score_rect = score_surface.get_rect() 
    game_window.blit(score_surface, score_rect)


#code after gameover
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()


#if hitted the wall then gameover
if check_wall_collisions(snake_position):
    game_over()

#main loop
input_box = InputBox(240, 180, 240, 32)
conn = connect_database()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if game_state == GAME_STATE_INIT:
            input_box.handle_event(event)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
                #save data when paused
                if paused:
                    save_game_state(conn, username, level, score)
                game_state = GAME_STATE_PAUSED if paused else GAME_STATE_PLAYING
            
            if game_state == GAME_STATE_PLAYING and not paused:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

    #first ccreen
    if game_state == GAME_STATE_INIT:
        game_window.fill(black)
        input_box.draw(game_window)

    #game
    elif game_state == GAME_STATE_PLAYING and not paused:
        game_window.fill(black)
        
        # Change direction based on user input
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        elif change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        elif change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        elif change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        
        # Move the snake
        if direction == 'UP':
            snake_position[1] -= 10
        elif direction == 'DOWN':
            snake_position[1] += 10
        elif direction == 'LEFT':
            snake_position[0] -= 10
        elif direction == 'RIGHT':
            snake_position[0] += 10
        
        #growing
        snake_body.insert(0, list(snake_position))
        if (fruit_position[0] <= snake_position[0] < fruit_position[0] + 30) and (fruit_position[1] <= snake_position[1] < fruit_position[1] + 30):
            score += 30
            fruit_spawn = False
        else:
            snake_body.pop()
        
        #respawn fruit
        if not fruit_spawn:
            fruit_position = [random.randrange(5, (window_x // 12)) * 10, random.randrange(5, (window_y // 12)) * 10]
            fruit_spawn = True

        #draw walls and check for collisions
        draw_walls()
        if check_wall_collisions(snake_position):
            game_over()

        #drawing snake
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 30, 30))
        
        #hitting wall
        if snake_position[0] < 0 or snake_position[0] > window_x - 10 or snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()
        
        #hitting itself
        for block in snake_body[1:]:
            if snake_position == block:
                game_over()

        # Level progression and speed adjustment
        if score > 100 * level:
            level += 1
            update_level_settings()

    #pause menu
    elif game_state == GAME_STATE_PAUSED:
        pause_font = pygame.font.SysFont('times new roman', 48)
        pause_surf = pause_font.render('Paused', True, white)
        pause_rect = pause_surf.get_rect(center=(window_x/2, window_y/2))
        game_window.blit(pause_surf, pause_rect)

    show_score(white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(snake_speed)