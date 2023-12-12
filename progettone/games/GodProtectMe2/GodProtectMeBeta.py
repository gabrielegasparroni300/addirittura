import pygame, random

#God Protect Me

pygame.init()

#Soundtrack

pygame.mixer.init()
pygame.mixer.music.load("soundtrack.mp3") 
pygame.mixer.music.set_volume(0.85) 
pygame.mixer.music.play(loops = -1)

#Screen setup

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT ) )
pygame.display.set_caption("God Protect Me")

background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

#Main menu setup

Titlefont = pygame.font.SysFont('Impact', 70)
Normalfont = pygame.font.SysFont('Impact', 30)

Highscore = pygame.font.SysFont('Arial', 60)
Gameend1 = pygame.font.SysFont('Impact', 60)
Gameend2 = pygame.font.SysFont('Impact', 50)

score = 0
top_left = (100, 100)
top_right = (1300, 150)

title = Titlefont.render('God Protect Me', True,"#ffd700")
click_to_play = Normalfont.render('Click "SPACE" to play', True, "#ffd700")
game_over = Gameend1.render('Game Over', True, "#ff0000")
click_exit = Gameend2.render('Click "ESC" to exit', True, "black")


#Player's base information

base_width = 300
base_height = 300

base_x = SCREEN_WIDTH // 2 - base_width // 2
base_y = SCREEN_HEIGHT // 2 - base_height // 2

base_image = pygame.image.load("playerBase.png")
base_image = pygame.transform.scale(base_image, (base_width, base_height))

hp = 1500
health_bar = 500

mouse_icon = pygame.image.load("cursor.png")
mouse_icon = pygame.transform.scale(mouse_icon, (40,40))
pygame.mouse.set_visible(False)

#Enemy's information

ADD_ENEMY = pygame.USEREVENT + 1
timer = 950
pygame.time.set_timer(ADD_ENEMY, timer)

dmg = 1.5

enemy_list = []
static_enemy_list = []
dead_enemy_list = []

target_x = SCREEN_WIDTH // 2
target_y = SCREEN_HEIGHT // 2

enemy_image = pygame.image.load("enemy.png")
enemy_image = pygame.transform.scale(enemy_image, (58, 56))

dead_enemy_image = pygame.image.load("deadEnemy.png")
dead_enemy_image = pygame.transform.scale(dead_enemy_image, (58, 56))

#Level generation

running = True

while running:
    
    pygame.time.delay(10)
    
    mouse_pos = pygame.mouse.get_pos()
    mouse_icon_rect = mouse_icon.get_rect(topleft = (mouse_pos[0], mouse_pos[1]))
    

    player_score = Highscore.render(f"Score: {score}", True, "#ffd700")
    
    screen.blit(background_image, (0,0))
    
    castle = screen.blit(base_image, (base_x, base_y))
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        
        #Adding random positions for the enemies far enough from the player's base to a list
        
        if event.type == ADD_ENEMY:
            
            enemy_position_x1 = random.randint(-25, SCREEN_WIDTH + 25)
            enemy_position_y1 = random.randint(-25, 0)
            
            enemy_position_x2 = random.randint(-25, 0)
            enemy_position_y2 = random.randint(-25, SCREEN_HEIGHT + 25)
            
            enemy_position_x3 = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 25)
            enemy_position_y3 = random.randint(-25, SCREEN_HEIGHT + 25)

            enemy_position_x4 = random.randint(-25, SCREEN_WIDTH + 25)
            enemy_position_y4 = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT + 25)
            
            enemy_list.append((enemy_position_x1, enemy_position_y1, 45, 60))
            
            enemy_list.append((enemy_position_x2, enemy_position_y2, 45, 60))
            
            enemy_list.append((enemy_position_x3, enemy_position_y3, 45, 60))
            
            enemy_list.append((enemy_position_x4, enemy_position_y4, 45, 60))
    
    #Using the positions from the list to spawn the enemies
    
    for i in range(len(enemy_list)):
        enemy_rect = pygame.Rect(enemy_list[i][0], enemy_list[i][1], enemy_list[i][-2], enemy_list[i][-1])
        (x,y) = (enemy_list[i][0], enemy_list[i][1])
        
        enemy_speed = random.randint(3, 8)
        
        if hp <= 0:
            enemy_speed = 0
            dmg = 0
        
        en = screen.blit(enemy_image, enemy_list[i])
        
        if x > target_x:
            x -= enemy_speed
        if x < target_x:
            x += enemy_speed
        if y > target_y:
            y -= enemy_speed
        if y < target_y:
            y += enemy_speed
                
        if en.colliderect(castle):
             enemy_list.pop(i)
             static_enemy_list.append((x,y))
             break
            
        enemy_list.pop(i)
        enemy_list.insert(i, (x,y))
        
    #Checking for collisions between an enemy and the cursor
        
        if pygame.mouse.get_pressed()[0] and mouse_icon_rect.colliderect(enemy_rect):
            dead_enemy = enemy_list.pop(i)
            dead_enemy_list.append(dead_enemy)
            dead = screen.blit(dead_enemy_image, (dead_enemy))
            score += random.randint(100, 250)
            break

    for stat in range(len(static_enemy_list)):
        if pygame.mouse.get_pressed()[0] and mouse_icon_rect.colliderect(enemy_rect):
            dead_enemy = static_enemy_list.pop(stat)
            dead_enemy_list.append(dead_enemy)
            dead = screen.blit(dead_enemy_image, (dead_enemy))
            score += random.randint(100, 250)
            break
        
        for (x,y) in dead_enemy_list:
            x,y = 0,0
            enemy_speed -= enemy_speed
            
    #Stopping the enemies that hit the player's base and dealing damage to the player himself
    
    for o in range(len(static_enemy_list)):
        (static_x, static_y) = static_enemy_list[o]
        static_en = screen.blit(enemy_image, static_enemy_list[o])
        hp -= dmg
        if hp == 0:
            break
        health_bar -= (health_bar * dmg) / hp
        
    #Stoppping the game when the player loses all the health points
    
    if hp <= 0:
        game_end = screen.blit(game_over, (SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2))
        click_esc = screen.blit(click_exit, (SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 + 80))

    #Adding all of the HUD elements
    
    score_text = screen.blit(player_score, top_left)
    
    castle_damage_taken = pygame.draw.rect(screen, "#400101", (top_right[0], top_right[1], 500, 20))
    
    castle_health_left = pygame.draw.rect(screen, "#e61919", (top_right[0], top_right[1], health_bar, 20))
    
    Title = screen.blit(title, (SCREEN_WIDTH // 2 -250, 50))
    
    new_cursor = screen.blit(mouse_icon, mouse_pos)

    #Updating and closing the game

    pygame.display.update()

pygame.quit()
