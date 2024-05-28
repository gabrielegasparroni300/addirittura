import pygame, random, MovementModule, os

#God Protect Me

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

#Soundtrack

pygame.mixer.init()
music_path = os.path.join(os.path.dirname(__file__), "soundtrack.mp3")
pygame.mixer.music.load(music_path) 
pygame.mixer.music.set_volume(0.85) 
pygame.mixer.music.play(loops = -1)



#Screen setup

SCREEN_WIDTH = pygame.display.get_desktop_sizes()[0][0]
SCREEN_HEIGHT = pygame.display.get_desktop_sizes()[0][1]

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT ) )
pygame.display.set_caption("God Protect Me")

background_path = os.path.join(os.path.dirname(__file__), "background.jpg")
background_image = pygame.image.load(background_path)
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

#Main menu setup

Titlefont = pygame.font.SysFont('Impact', 70)
Normalfont = pygame.font.SysFont('Impact', 30)

Highscore = pygame.font.SysFont('Arial', 60)
Gameend1 = pygame.font.SysFont('Impact', 60)
Gameend2 = pygame.font.SysFont('Impact', 50)

score = 0
top_left = ((SCREEN_WIDTH * 100) / 1920, (SCREEN_HEIGHT * 100) / 1080)
top_right = ((SCREEN_WIDTH * 1300) / 1920, (SCREEN_HEIGHT * 125) / 1080)

title = Titlefont.render('God Protect Me', True,"#ffd700")
click_to_play = Normalfont.render('Click "SPACE" to play', True, "#ffd700")
game_over = Gameend1.render('Game Over', True, "#ff0000")
click_exit = Gameend2.render('Click "ESC" to exit', True, "black")


#Player's base information

base_width = (SCREEN_WIDTH * 300) / 1920
base_height = (SCREEN_WIDTH * 300) / 1920

base_x = SCREEN_WIDTH // 2 - base_width // 2
base_y = SCREEN_HEIGHT // 2 - base_height // 2

base_path = os.path.join(os.path.dirname(__file__), "playerBase.png")
base_image = pygame.image.load(base_path)
base_image = pygame.transform.scale(base_image, (base_width, base_height))

hp = 1500
health_bar = (SCREEN_WIDTH * 500) / 1920

pygame.mouse.set_visible(False)

#Player Info
spawn_point_x = SCREEN_WIDTH // 2
spawn_point_y = SCREEN_HEIGHT // 2

player_pos_list = []

player_speed = (SCREEN_WIDTH * 8) / 1920

player_attack_radius = (SCREEN_WIDTH * 200) / 1920

player_width = player_attack_radius // 2
player_height = player_attack_radius // 2

player_path = os.path.join(os.path.dirname(__file__), "personaggio.png")
player_image = pygame.image.load(player_path)
player_image = pygame.transform.scale(player_image, (player_width, player_height))

w = player_attack_radius
h = player_attack_radius

surf = pygame.Surface((w, h), pygame.SRCALPHA)
alpha_surface = pygame.Surface(surf.get_size(), pygame.SRCALPHA)
player_attack_area = pygame.draw.circle(surf, "red", (w // 2,h // 2), w // 2)
alpha_surface.fill((255, 255, 255, 80))
surf.blit(alpha_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)


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

enemy_path = os.path.join(os.path.dirname(__file__), "bomba.png")
enemy_image = pygame.image.load(enemy_path)
enemy_image = pygame.transform.scale(enemy_image, ((SCREEN_WIDTH * 58) / 1920, (SCREEN_HEIGHT * 56) / 1080))

dead_enemy_path = os.path.join(os.path.dirname(__file__), "fulmine.png")
dead_enemy_image = pygame.image.load(dead_enemy_path)
dead_enemy_image = pygame.transform.scale(dead_enemy_image, ((SCREEN_WIDTH * 70) / 1920, (SCREEN_HEIGHT * 100) / 1080))

#Level generation

running = True

while running:
    
    pygame.time.delay(10)

    player_score = Highscore.render(f"Score: {score}", True, "#ffd700")
    
    screen.blit(background_image, (0,0))
    
    castle = screen.blit(base_image, (base_x, base_y))
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        
        #Adding random positions for the enemies far enough from the player's base to a list
        
        if event.type == ADD_ENEMY and hp > 0:
            
            for times in range(random.randint(30, 50)):
                enemy_position_x = random.randint(-25, SCREEN_WIDTH + 25)
                enemy_position_y = random.randint(-25, SCREEN_HEIGHT + 25)
            
                if MovementModule.is_on_screen(enemy_position_x, enemy_position_y, SCREEN_WIDTH, SCREEN_HEIGHT) == False:
                    enemy_list.append((enemy_position_x, enemy_position_y, 45, 60))
    
    #Moving the player
    spawn_point_x = MovementModule.move_player_1(spawn_point_x, spawn_point_y, player_speed) [0]
    spawn_point_y = MovementModule.move_player_1(spawn_point_x, spawn_point_y, player_speed) [1]
    
    #Using the positions from the list to spawn the enemies
    
    for i in range(len(enemy_list)):
        (x,y) = (enemy_list[i][0], enemy_list[i][1])
        
        enemy_speed = random.randint((SCREEN_WIDTH * 3) // 1920, (SCREEN_HEIGHT * 7) // 1920)
        
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
        
    #Checking if an enemy is close enough to the player to be killed
        
        if MovementModule.is_in_range(spawn_point_x, spawn_point_y, x, y, player_attack_radius) == True:
            dead_enemy = enemy_list.pop(i)
            dead_enemy_list.append(dead_enemy)
            for x in range(180):
                dead = screen.blit(dead_enemy_image, (dead_enemy))
            score += random.randint(100, 250)
            break

    for stat in range(len(static_enemy_list)):
        if MovementModule.is_in_range(spawn_point_x, spawn_point_y, static_enemy_list[stat][0], static_enemy_list[stat][1], player_attack_radius) == True:
            dead_enemy = static_enemy_list.pop(stat)
            dead_enemy_list.append(dead_enemy)
            for x in range(180):
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
        game_end = screen.blit(game_over, (SCREEN_WIDTH // 2 - (SCREEN_WIDTH * 130) / 1920, SCREEN_HEIGHT // 2))
        click_esc = screen.blit(click_exit, (SCREEN_WIDTH // 2 - (SCREEN_WIDTH * 130) / 1920, SCREEN_HEIGHT // 2 + 80))
        player_speed = 0
        static_enemy_list.clear()
        enemy_list.clear()
    
    circle = screen.blit(surf,(spawn_point_x - (player_width / 2), spawn_point_y - (player_height / 2)))
    
    player = screen.blit(player_image, (spawn_point_x, spawn_point_y))
    
    #Adding all of the UI elements
    
    score_text = screen.blit(player_score, top_left)
    
    castle_damage_taken = pygame.draw.rect(screen, "#400101", (top_right[0], top_right[1], (SCREEN_WIDTH * 500) / 1920, (SCREEN_HEIGHT * 20) / 1080))
    
    castle_health_left = pygame.draw.rect(screen, "#e61919", (top_right[0], top_right[1], health_bar, (SCREEN_HEIGHT * 20) / 1080))

    #Updating and closing the game

    pygame.display.update()

pygame.quit()
