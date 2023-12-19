# Filippo Zamponi   Tommaso Zamponi
# 2 BS
# Gioco con python

import pygame, random , time

pygame.init()

pygame.mixer.init() 
pygame.mixer.music.load("musica.mp3") 
pygame.mixer.music.set_volume(0.3) 
pygame.mixer.music.play()

#grandezza schermo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#titolo schermo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("Pong")

#font dei due palyer
player1_font = pygame.font.SysFont('Impact', 30)
player2_font = pygame.font.SysFont('Impact', 30)

#
player1Sfondo = player1_font.render("PLAYER 1", True, "blue","black")
player2Sfondo = player2_font.render("PLAYER 2", True, "red","black")




#sfondo
imgSfondo = pygame.image.load("N.jpeg") 
imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH,SCREEN_HEIGHT))

    

# posizione iniziale giocatore 1 
x1 = SCREEN_WIDTH // 11
y1 = SCREEN_HEIGHT // 2

# posizione iniziale giocatore 2 
x2 = SCREEN_WIDTH * 9 // 10
y2 = SCREEN_HEIGHT // 2


#dimensioni rettangoli
w = 10
h = 40

# velocità di spostamento rettangolo
speed = 3

#velocità spostamento palla
speed_palla = 3

#direzioni casuali palla
direction_x = [1, -1]
direction_y = [1, -1]

x_ball = random.choice(direction_x)
y_ball = random.choice(direction_y)

#posizione pallina
x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT // 2

# il nome del vincitore
winner = ""

running = True

#per spostare i due giocatori 
while running: 
    pygame.time.delay(10) 

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    
    #tasti per lo spostamento 
    keys = pygame.key.get_pressed() 
    
    if keys[pygame.K_w] and y1 > 24: 
        y1 -= speed 
    if keys[pygame.K_s] and y1 < 580 - h: 
        y1 += speed
        
    if keys[pygame.K_UP] and y2 > 24: 
        y2 -= speed 
    if keys[pygame.K_DOWN] and y2 < 580 - h: 
        y2 += speed 

  
    #lo schermo e invece di screen.fill("white") utilizzo un altro sfondo 
    screen.blit(imgSfondo,(0,0) )

    # linea bianca dal punto... al punto ... di spessore ...
    # l è il "rettangolo" che contiene la linea disegnata 
    pygame.draw.line(screen, "white", (60, 20), (740, 20), 4)

    # linea bianca dal punto... al punto ... di spessore ...
    # l è il "rettangolo" che contiene la linea disegnata 
    pygame.draw.line(screen, "white", (60, 580), (740, 580), 4)

    # linea bianca dal punto... al punto ... di spessore ...
    # l è il "rettangolo" che contiene la linea disegnata 
    pygame.draw.line(screen, "white", (60, 20), (60, 580), 4)

    # linea bianca dal punto... al punto ... di spessore ...
    # l è il "rettangolo" che contiene la linea disegnata 
    pygame.draw.line(screen, "white", (740, 20), (740, 580), 4)

    # linea bianca dal punto... al punto ... di spessore ...
    # l è il "rettangolo" che contiene la linea disegnata 
    linea_tratteggiata = pygame.draw.line(screen, "white", (400, 20), (400, 580), 4)

    #i due giocatori 
    player1 = pygame.draw.rect(screen, "white", (x1, y1, w, h))
    player2 = pygame.draw.rect(screen, "white", (x2, y2, w, h))
    
    
    #disegno la pallina
    pallina = pygame.draw.circle(screen, "white", (x,y), 10)
    
    
    
    # collisioni e rimbalzi tra pallina e campo di gioco
    if y >= SCREEN_HEIGHT - 20 :
        y_ball *= -1
    
    if y <= 20:
        y_ball *= -1
        
    if player1.colliderect(pallina):
        x_ball *= -1
    
    if player2.colliderect(pallina):
        x_ball *= -1
            
    
    if x <= 60:
        winner = "P2"
        running = False 
        
    if x >= SCREEN_WIDTH - 60:
        winner = "P1"        
        running = False
      
    screen.blit(player1Sfondo, (170,5))
    screen.blit(player2Sfondo, (530,5))
    
    pygame.display.flip()
    
    # cambio di direzione della pallina nella collisione 
    x += speed_palla * x_ball
    y += speed_palla * y_ball

# il ciclo inizia se P1 o P2 hanno vinto
if winner == "P1":
    img_win = pygame.image.load("P1.png")
    print("p1 win")       
else:
    img_win = pygame.image.load("P2.png") 
    print("p2 win")
    
screen.blit(img_win,(150, 100 ) )       
pygame.display.flip()  
time.sleep(2.0)






pygame.quit()