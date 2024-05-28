#Mingo Aurora e Tittarelli Silvia
#Classe 2BS
# Primo programma: PacMan

# importa ed inizializza la libreria pygame
import pygame
import random
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

#parte dove si programma la musica
pygame.mixer.init()
music_path = os.path.join(os.path.dirname(__file__), "PacManSong.mp3")
pygame.mixer.music.load(music_path)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

#posizione iniziale
wPacMan = 42 #larghezza PacMan
hPacMan = 42 #altezza PacMan
xPacMan = 0 #x iniziale PacMan
yPacMan = 750 #y iniziale PacMan
speed = 5 #velocità
speed_ghost = 3



#dimensioni dello schermo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# lo screen
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
pygame.display.set_caption("PacMan tarocco")

#inserimento immagine di Pac Man
imgPacMan_path = os.path.join(os.path.dirname(__file__), "PacMan2.png")
imgPacMan = pygame.image.load(imgPacMan_path)
imgPacManUpDw_path = os.path.join(os.path.dirname(__file__), "PacMan.png")
imgPacManUpDw = pygame.image.load(imgPacManUpDw_path)

#ridimensionamento immagini di PacMan per tutte le direzioni
imgPacManDx = pygame.transform.scale(imgPacMan,(42,42))
imgPacManSx = pygame.transform.flip(imgPacManDx,True,False)
imgPacManUp = pygame.transform.scale(imgPacManUpDw,(42,42))
imgPacManDw = pygame.transform.flip(imgPacManUp,False, True)

#lista immagini create
listaImmagini = [imgPacManDx,imgPacManSx,imgPacManUp,imgPacManDw]
direction = 0

punteggio = 0

# Definizione dei font se vinci
ScrittaGrande = pygame.font.SysFont('Impact', 170)

#font dei punti e dell'uscita
punti = pygame.font.SysFont('Impact', 30)

#definizione delle scritte che compaiono nel gioco
vittoria = ScrittaGrande.render("VICTORY!", True, "gold")
sconfitta = ScrittaGrande.render("GAME OVER", True, "red")
contaPunti = punti.render(("points:0"), True, "white")
uscita = punti.render("Premi ESC per uscire",True,"white")
#
#------------------------------------------------------------------------
#immagine fantasmino ridimensioni
fantasmino1_path = os.path.join(os.path.dirname(__file__), "fantasmino.png")
fantasmino1 = pygame.image.load(fantasmino1_path)
fantasmino2_path = os.path.join(os.path.dirname(__file__), "fantasmino_azzurro.png")
fantasmino2 = pygame.image.load(fantasmino2_path)
fantasmino3_path = os.path.join(os.path.dirname(__file__), "fantasmino_arancione.png")
fantasmino3 = pygame.image.load(fantasmino3_path)

imgFantasma1 = pygame.transform.scale(fantasmino1,(50,50))
imgFantasma2 = pygame.transform.scale(fantasmino2,(50,50))
imgFantasma3 = pygame.transform.scale(fantasmino3,(50,50))


#direzioni che seguirà il fantasmino
lista_direzioni = ["destra","sinistra","sopra","sotto"]

#coordinate fantasma 1
x_fantasma1 = 750
y_fantasma1 = 750

#coordinate fantasma 2
x_fantasma2 = 750
y_fantasma2 = 0

#coordinate fantasma 3
x_fantasma3 = 375
y_fantasma3 = 375


#dimensioni generali fantasmi
w_fantasma = 50
h_fantasma = 50

lista_fantasmi = [(750,750),(750,0),(375,375)]
lista_cambi = [(750,750),(750,375),(750,0),(375,0),(375,375),(375,750),(0,0),(0,375),(0,750)]

#direzioni iniziali dei fantasmini
direzione1 = random.choice(lista_direzioni)
direzione2 = random.choice(lista_direzioni)
direzione3 = random.choice(lista_direzioni)

#--------------------------------------------------------------------------------------------ù
#settore monete

#lista delle monete inizialmente vuota
lista_monete = []

#linea 1 x
for x in range(20,780,50):
    money = (x,20)
    lista_monete.append(money)
    
#linea 2 x
for x in range(70,760,50):
    money = (x,395)
    lista_monete.append(money)
    
#linea 3 x
for x in range(20,780,50):
    money = (x,770)
    lista_monete.append(money)

#linea 1 y
for y in range(70,780,50):
    money = (20,y)
    lista_monete.append(money)
    
#linea 2 y
for y in range(70,760,50):
    money = (395,y)
    lista_monete.append(money)

#linea 3 y
for y in range(70,780,50):
    money = (770,y)
    lista_monete.append(money)

#-------------------------------------------------------------------------
#mappa
posizioni = [(50,425),(50,50),(425,50),(425,425)]

                
#condizioni iniziali
running = True
paused = False

#------------------------------------------------------------------------------------------------
#cosa accade mentre si è in gioco
while running:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        # serve a gestire la X di chiusura in alto 
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        
        #blocco per stoppare la musica
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            if paused:
                paused = False
                pygame.mixer.music.play()
            else:
                paused = True
                pygame.mixer.music.pause()

    if paused:
        continue
    
    keys = pygame.key.get_pressed()
    
    #movimenti del PacMan
    if keys[pygame.K_LEFT] and xPacMan > 0: 
        xPacMan -= speed
        direction = 1
        
    if keys[pygame.K_RIGHT] and xPacMan < SCREEN_WIDTH - wPacMan: 
        xPacMan += speed
        direction = 0
            
    if keys[pygame.K_UP] and yPacMan > 0: 
        yPacMan -= speed
        
        direction = 2
            
    if keys[pygame.K_DOWN] and yPacMan < SCREEN_HEIGHT - hPacMan:
        yPacMan += speed
        
        direction = 3
    
    #---------------------------------------------------------------------------------
    #movimenti fantasma 1
    if  direzione1 == "sinistra" and x_fantasma1 > 0: 
        x_fantasma1 -= speed_ghost
        
        
    if direzione1 == "destra" and x_fantasma1 < SCREEN_WIDTH - w_fantasma: 
        x_fantasma1 += speed_ghost
        
        
    if direzione1 == "sopra" and y_fantasma1 > 0: 
        y_fantasma1 -= speed_ghost
        
        
    if direzione1 == "sotto" and y_fantasma1 < SCREEN_HEIGHT - h_fantasma:
        y_fantasma1 += speed_ghost
        
    #----------------------------------------------------------------------------------------------------------
    #movimenti fantasma 2
    if  direzione2 == "sinistra" and x_fantasma2 > 0: 
        x_fantasma2 -= speed_ghost
        
        
    if direzione2 == "destra" and x_fantasma2 < SCREEN_WIDTH - w_fantasma: 
        x_fantasma2 += speed_ghost
        
        
    if direzione2 == "sopra" and y_fantasma2 > 0: 
        y_fantasma2 -= speed_ghost
        
        
    if direzione2 == "sotto" and y_fantasma2 < SCREEN_HEIGHT - h_fantasma:
        y_fantasma2 += speed_ghost
    
    #----------------------------------------------------------------------------------------------------
    #movimenti fantasma 3
    if  direzione3 == "sinistra" and x_fantasma3 > 0: 
        x_fantasma3 -= speed_ghost
        
        
    if direzione3 == "destra" and x_fantasma3 < SCREEN_WIDTH - w_fantasma: 
        x_fantasma3 += speed_ghost
        
        
    if direzione3 == "sopra" and y_fantasma3 > 0: 
        y_fantasma3 -= speed_ghost
        
        
    if direzione3 == "sotto" and y_fantasma3 < SCREEN_HEIGHT - h_fantasma:
        y_fantasma3 += speed_ghost
        
    #-------------------------------------------------------------------------------------------------

    screen.fill("black")
    screen.blit(contaPunti,(450,450))
    
    #aggiunge titti i personaggi allo screen
    player = screen.blit(listaImmagini[direction],(xPacMan,yPacMan))
    
    
    for posx,posy in posizioni:
        
        limite_sinistra = pygame.draw.rect(screen,"blue",(posx,posy,325,325),15)#,border_radius = 10)
        limite_destra = pygame.draw.rect(screen, "blue",(posx+325,posy,1,325))
        limite_alto = pygame.draw.rect(screen, "blue",(posx,posy-1,325,1))
        limite_basso = pygame.draw.rect(screen, "blue",(posx,posy+325,325,1))
        
            
        if player.colliderect(limite_sinistra):
            xPacMan -= speed
            
        if player.colliderect(limite_destra):
            xPacMan += speed
        
        if player.colliderect(limite_alto):
            yPacMan -= speed
            xPacMan += speed
        
        if player.colliderect(limite_basso):
            yPacMan += speed
    
    #------------------------------------------------------------------------------------------------
    #fantasmi
    disegno_fantasma1 = screen.blit(imgFantasma1,(x_fantasma1,y_fantasma1))
    disegno_fantasma2 = screen.blit(imgFantasma2,(x_fantasma2,y_fantasma2))
    disegno_fantasma3 = screen.blit(imgFantasma3,(x_fantasma3,y_fantasma3))
    
    #caso fantasma 1
    if x_fantasma1 < 0 or x_fantasma1 > SCREEN_WIDTH - w_fantasma:
        direzione1 = random.choice(lista_direzioni)
        print(x_fantasma1, y_fantasma1)
        
    if y_fantasma1 < 0 or y_fantasma1 > SCREEN_WIDTH - h_fantasma:
        direzione1 = random.choice(lista_direzioni)
        print(x_fantasma1, y_fantasma1)
        
    for x_cambi,y_cambi in lista_cambi:
        if (x_fantasma1,y_fantasma1) == (x_cambi,y_cambi):
            direzione1 = random.choice(lista_direzioni)
            
    #caso fantasma 2
    if x_fantasma2 < 0 or x_fantasma2 > SCREEN_WIDTH - w_fantasma:
        direzione2 = random.choice(lista_direzioni)
        print(x_fantasma2, y_fantasma2)
        
    if y_fantasma2 < 0 or y_fantasma2 > SCREEN_WIDTH - h_fantasma:
        direzione2 = random.choice(lista_direzioni)
        print(x_fantasma1, y_fantasma1)
        
    for x_cambi,y_cambi in lista_cambi:
        if (x_fantasma2,y_fantasma2) == (x_cambi,y_cambi):
            direzione2 = random.choice(lista_direzioni)
            
    #caso fantasma 3
    if x_fantasma3 < 0 or x_fantasma3 > SCREEN_WIDTH - w_fantasma:
        direzione3 = random.choice(lista_direzioni)
        print(x_fantasma3, y_fantasma3)
        
    if y_fantasma3 < 0 or y_fantasma3 > SCREEN_WIDTH - h_fantasma:
        direzione3 = random.choice(lista_direzioni)
        print(x_fantasma3, y_fantasma3)
        
    for x_cambi,y_cambi in lista_cambi:
        if (x_fantasma3,y_fantasma3) == (x_cambi,y_cambi):
            direzione3 = random.choice(lista_direzioni)
    
    #collisione fantasma
    if player.colliderect(disegno_fantasma1) or player.colliderect(disegno_fantasma2) or player.colliderect(disegno_fantasma3):
        screen.blit(sconfitta,(20,260))
        screen.blit(uscita,(30,450))
        speed = 0
        speed_ghost = 0
        
        
#-----------------------------------------------------------------------------------------------
#disegno e conteggio delle monete
    for x,y in lista_monete:
        money = pygame.draw.rect(screen,"orange",(x,y,10,10))
        
        if player.colliderect(money):
            
            punteggio += 1
            contaPunti = punti.render(("points:"+str(punteggio)), True, "white")
            screen.blit(contaPunti,(450,450))
            
            
            lista_monete.remove((x,y))
    
    #vittoria
    if punteggio == 90:
        screen.blit(vittoria,(90,280))
        screen.blit(uscita,(80,450))
        speed = 0
        speed_ghost = 0

    # aggiorna quello che vedi sullo schermo
    pygame.display.flip()
    
# Chiude pygame
pygame.quit()
