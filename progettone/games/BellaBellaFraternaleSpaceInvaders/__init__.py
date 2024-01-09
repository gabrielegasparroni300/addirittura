# Invasori Spaziali

# di Leonardo Della Bella e Lorenzo Fraternale

import pygame, random, time

conta = 0

# inizializzazione
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("Invasori Spaziali") 

# nemici
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 10000)

enemies = []

# immagini
imgSfondo = pygame.image.load("pixelstars1.jpg")
imgSfondo = pygame.transform.scale(imgSfondo, (SCREEN_WIDTH, SCREEN_HEIGHT))
imgNave = pygame.image.load("pixelnavicella1.png") 
imgNave = pygame.transform.scale(imgNave,(100,100))
imgNemico = pygame.image.load("navicellaCattiva1.png") 
imgNemico = pygame.transform.scale(imgNemico,(85,85))


#
Titlefont = pygame.font.Font('PublicPixel-z84yD.ttf', 30)
Normalfont = pygame.font.Font('PublicPixel-z84yD.ttf', 10)

game_start = Titlefont.render('Premi "SPAZIO" per iniziare', True, "grey")

Punteggio = Titlefont.render(f'Punteggio:{conta}', True, "red")
Sconfitta = Titlefont.render(f'Hai Perso', True, "red")

#
pygame.mixer.init() 
pygame.mixer.music.load("laser.mp3") 
pygame.mixer.music.set_volume(0.5) 

#
x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT // 2 + 250

w = 10
h = 10

speedx = 5
speedy = 4

laserenem = True
attivato = False
running = True
paused = False

# posizione del proiettile
xBfriendly = 0
yBfriendly = 0
yBEnemies = 0
xBEnemies = 0
# 
bullets = []  
enemyBullets = []

while running: 
    pygame.time.delay(5)
    
    
    

   
    
#     screen.blit(imgSfondo, (0,0))
#     player = screen.blit(imgNave, (x,y))
    
    

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == ADD_ENEMY:
            posx = 10
            for n in range(10):
                posx += 100
                posy = 100
                enemies.append( (posx,posy) )

    keys = pygame.key.get_pressed()
    # movimenti
    if attivato == True:
        if keys[pygame.K_a] and x > 0 or keys[pygame.K_LEFT] and x > 0: 
            w,h = 70,70
            x -= speedx 
        if keys[pygame.K_d] and x < SCREEN_WIDTH - w-50 or keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - w-50: 
            w,h = 70,70
            x += speedx 
        if keys[pygame.K_w] and y > 600 or keys[pygame.K_UP] and y > 600: 
            w,h = 20,40
            y -= speedy 
        if keys[pygame.K_s] and y < SCREEN_HEIGHT - h-100 or keys[pygame.K_DOWN] and y < SCREEN_HEIGHT - h-100: 
            w,h = 20,40
            y += speedy
    # sparo
    if keys[pygame.K_SPACE]:
        attivato = True
        pygame.mixer.music.play()
        yBfriendly = y
        xBfriendly = x+50
        if len(bullets) < 1:
            bullets.append( (xBfriendly, yBfriendly) )
    screen.blit(imgSfondo, (0,0))
    player = screen.blit(imgNave, (x,y))
    
    
    if attivato == False:
        screen.blit(game_start, (SCREEN_WIDTH // 2 - 400,SCREEN_HEIGHT // 2))
    
    
    for i in range(len(bullets)):
        xBfriendly,yBfriendly = bullets[i]
        if xBfriendly != 0 and yBfriendly != 0:
            Bfriendly = pygame.draw.rect(screen, "green", (xBfriendly, yBfriendly, 5, 20))
            yBfriendly -= 10
            bullets[i] = xBfriendly,yBfriendly
        
        if yBfriendly <= 0:
            bullets.pop(i)
            break
        

    #
    for i in range(len(enemies)):
        posx,posy = enemies[i]
        enemy = screen.blit(imgNemico, (posx, posy))
        if enemy.colliderect(Bfriendly) == True:
            enemies.pop(i)
            conta += 1
            break
            
        if player.colliderect(enemy):
            print("HAI PERSO!")
            running = False
            
    Punteggio = Titlefont.render(f'Punteggio:{conta}', True, "red")
    screen.blit(Punteggio, (0,0))
    
    for c in range(len(enemies)):
        posx,posy = enemies[c]
        if keys[pygame.K_SPACE]:
            pygame.mixer.music.play()
            yBEnemies = posy
            xBEnemies = random.randint(100,1100)
            
            if len(enemyBullets) < 1:
                enemyBullets.append( (xBEnemies, yBEnemies) )
            
            
    for i in range(len(enemyBullets)):
        xBEnemies,yBEnemies = enemyBullets[i]
        if xBEnemies != 0 and yBEnemies != 0:
            BEnemies = pygame.draw.rect(screen, "red", (xBEnemies, yBEnemies, 5, 20))
            yBEnemies += 10
            enemyBullets[i] = xBEnemies,yBEnemies
            if player.colliderect(BEnemies) == True:
                screen.blit(Sconfitta, (0,0))
                pygame.display.flip()
                time.sleep(1)
                running = False
#             if yBEnemies >= 1000:
#                 yBEnemies = posy
        
        if yBEnemies >= 800:
            enemyBullets.pop(i)
            break
        
    
    
        
    pygame.display.flip()
    
pygame.quit()
