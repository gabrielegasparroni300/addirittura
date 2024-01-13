import pygame, random, time

pygame.init()

timer = 0

# def stopwatch(message=None):
#     global timer
#     if not message:
#         timer = pygame.time.get_ticks()
#         print(timer)
#         return
#     now = pygame.time.get_ticks()
#     runtime = (now - timer) / 1000.0 + 0.001
#     print(f"{message} {runtime} seconds\t{(1.0 / runtime):.2f}fps")
#     timer = now

pygame.mixer.init() 
pygame.mixer.music.load("sound.mp3") 
pygame.mixer.music.set_volume(0.5) 
pygame.mixer.music.play()

pygame.time.get_ticks()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("super-space!")

Titlefont = pygame.font.SysFont('Impact', 70)
Normalfont = pygame.font.SysFont('Impact', 30)

game_end = Titlefont.render("Hai Perso!", True, "white")
close1_tip = Normalfont.render("Click ESC to exit", True, "blue","cyan")
close2_tip=Normalfont.render("Click Right to continue the game", True, "blue","cyan")



ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY,400)

enemies=[]


imgSfondo = pygame.image.load("space.png") 
imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH,SCREEN_HEIGHT))

imgspaceship = pygame.image.load("spaceship.png") 
imgspaceship = pygame.transform.scale(imgspaceship,(70,70))

x = 0
y = SCREEN_HEIGHT // 2

width = 30
height = 30

speed = 6
 
imgMeteorite=pygame.image.load("meteorite.png") 
imgMeteorite = pygame.transform.scale(imgMeteorite,(100,40))

haiperso = False
pausa = False
continua=False
speed=7

running = True

while running: 
    pygame.time.delay(10)
    
    if haiperso == False :
        timer = pygame.time.get_ticks()
    time_game=Normalfont.render(str(timer),True,"white","black")
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if haiperso == True:
                pygame.mixer.music.play()
                running = True
                haiperso = False
                
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pausa = not pausa
        
            # da fare (ricomincia il gioco)
            
        if event.type == ADD_ENEMY:
            posx = SCREEN_WIDTH - 50 
            posy = random.randint(0,SCREEN_HEIGHT - 50)
            enemies.append( (posx,posy) )
        
        
    if pausa:
        continue
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and x > 0: 
        x -= speed 
    if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - width: 
        x += speed
        if haiperso == True:
            pygame.mixer.music.play()
            running = False
            haiperso = False
    if keys[pygame.K_UP] and y > 0: 
        y -= speed 
    if keys[pygame.K_DOWN] and y < SCREEN_HEIGHT - height: 
        y += speed 
    
    screen.blit(imgSfondo,(0,0) )
    screen.blit(time_game,(500,20) )
 
    player=screen.blit(imgspaceship,(x,y))
    for i in range(len(enemies)):
        posx,posy = enemies[i]
        nemico  = screen.blit(imgMeteorite,(posx,posy))
        if player.colliderect(nemico):
            pygame.mixer.music.pause()
            screen.blit(game_end, (100,100))
            screen.blit(close1_tip, (100,300))
            screen.blit(close2_tip, (350,300))
            #screen.blit(time_game, (500,20))
#             haiperso = True
            running = False
            break
        posx -= 5
        enemies[i] = posx,posy
        
        
    pygame.display.flip()

# 
pygame.quit()