 # Fuffy bird

# 
import pygame
import random
import time
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

pygame.mixer.init()
music_path = os.path.join(os.path.dirname(__file__), "chief-keef-love-sosa.mp3")
pygame.mixer.music.load(music_path)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# lo screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fuffy bird")


ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY,2000)

enemies = []


imgSfondo_path = os.path.join(os.path.dirname(__file__), 'sfondo.jpg')
imgSfondo = pygame.image.load(imgSfondo_path)
imgSfondo = pygame.transform.scale(imgSfondo, (SCREEN_WIDTH, SCREEN_HEIGHT))


imgFuffy_path = os.path.join(os.path.dirname(__file__), 'fuffysosa.png')
imgFuffy = pygame.image.load(imgFuffy_path)
imgFuffy = pygame.transform.scale(imgFuffy,(35,35))

imgPerso_path = os.path.join(os.path.dirname(__file__), 'PERSO.png')
imgPerso = pygame.image.load(imgPerso_path)
imgPerso = pygame.transform.scale(imgPerso, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT // 2

w = 35
h = 35

speed = 0.5


#scritte
Titolo = pygame.font.SysFont('Rockwell Extra Bold',70)
scrittenorm = pygame.font.SysFont('Rockwell Extra Bold',30)

game_end = Titolo.render('FUFFY BIRD',True,'red')
close_tip = scrittenorm.render('Clicca spazio per giocare',True,'red')

# facile...
running = True
scritta = True
#



while running:
    # serve a gestire la X di chiusura in alto ed esc per uscire dal gioco
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            scritta = False
        if event.type == ADD_ENEMY:
            posx1 = SCREEN_WIDTH - 40
            posy1 = 0 #SCREEN_HEIGHT - 250
            w1 = 40
            h1 = random.randint(50,250)
            enemies.append((posx1,posy1,w1,h1))
            
            posx2 = SCREEN_WIDTH - 40
            posy2 = h1 + 100
            w2 = 40
            h2 = SCREEN_HEIGHT - posy2
            enemies.append((posx2,posy2,w2,h2))
      
            
    
    
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_UP] and y > 0: 
        y -= 0.3
    if not scritta and not keys[pygame.K_UP]:
        y += 0.2

    if scritta:
        screen.blit(imgSfondo,(0,0))
        screen.blit(game_end,(280,230))
        screen.blit(close_tip,(300,300))
        
        # Update display content
        pygame.display.flip()
        continue
        

    screen.blit(imgSfondo,(0,0))
    player = screen.blit(imgFuffy,(x,y))#pygame.draw.rect(screen, "red", (x, y, w, h))
    
   # in questo caso i nemici sono fermi: sono ostacoli
    for i in range(len(enemies)):
        (posx,posy,wq,hq) = enemies[i]
        en = pygame.draw.rect(screen, "forest green", (posx, posy, wq, hq))
        
        posx -= 0.2
        enemies[i] = (posx,posy,wq ,hq)
        

        # se questo rettangolo "collide" con il punto (x,y) ove si trova il giocatore...
        if player.colliderect(en):
            screen.blit(imgPerso,(0,0))            
            pygame.display.flip()
            time.sleep(5)
            running = False

            
            
    if y >= SCREEN_HEIGHT:
        screen.blit(imgPerso,(0,0))        
        pygame.display.flip()
        time.sleep(5) 

               
        running = False
        
    # Update display content
    pygame.display.flip()

# Chiude pygame
pygame.quit()

