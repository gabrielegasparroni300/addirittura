# IMPORTAZIONE PYGAME E RANDOM
#manca solo da aggiungere il timer
import pygame
import random

#INIZIO PYGAME
pygame.init()

#DIMENSIONE SCHERMO
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#AGGIUNTA SUONO IN LOOP
pygame.mixer.init() 
pygame.mixer.music.load("Honda CR 500 Sound Check Braaap!!!-0-16.9.mp3") 
pygame.mixer.music.set_volume(0.5) 
pygame.mixer.music.play(loops = -1)

# AGGIUNTA TERRENO SULLO SFONDO
imgSfondo = pygame.image.load("terreno.png")
screen = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH,SCREEN_HEIGHT))

#FONT SCRITTE INIZIALI
Titolo = pygame.font.SysFont("Rockwell Extra Bold", 100)
scrittaGioco = pygame.font.SysFont("Rockwell Extra Bold", 50)

# SCRITTE INIZIALI
game_end = Titolo.render("MOTO RUN", True, "black")
close_tip = scrittaGioco.render("clicca spazio per giocare", True, "black")

# TITOLO GIOCO
screen = pygame.display.set_mode( (800, 600) )
pygame.display.set_caption("MOTO RUN")

#AGGIUNTA IMMAGINE GIOCATORE
imgMoto = pygame.image.load("motoUfficiale.png")
imgMoto = pygame.transform.scale(imgMoto,(70, 70))

# AGGIUNTA IMMAGINI ENEMIES
imgAlbero = pygame.image.load("alberoUfficiale.png")
imgAlbero = pygame.transform.scale(imgAlbero,(70, 70))

imgTrattore = pygame.image.load("trattoreUfficiale.png")
imgTrattore = pygame.transform.scale(imgTrattore,(70,70))

imgMoneta = pygame.image.load("moneta.png")
imgMoneta = pygame.transform.scale(imgMoneta,(70,70))

# TEMPO DI AGGIUNTA ENEMIES
ADD_albero = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_albero, 800)

add_trattore = pygame.USEREVENT + 1
pygame.time.set_timer(add_trattore, 800)

add_moneta = pygame.USEREVENT + 1
pygame.time.set_timer(add_moneta, 1000)


# ELENCO NEMICI
enemiesAlberi = []
enemiesTrattori = []
enemiesMoneta = []

# POSIZIONE INIZIALE GIOCATORE
x = 225
y = 500

# DIMENSIONI GIOCATORE
w = 40
h = 20

# VELOCITA' GIOCATORE
speed = 7
superspeed = 14


# DEFINISCO RUNNING E SCRITTA COME "TRUE"
running = True
scritta = True
pausa = True
while running:
    pygame.time.delay(15)
    # GESTIONE X DI CHIUSURA
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # GESTIONE Q (QUIT) PER CHIUDERE IL GIOCO
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
                
        # SE PREMI SPAZIO IL GIOCO COMINCIA 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            scritta = False
            pausa = False
            
        if pausa:
            continue
        
        # COMPARSA ALBERI  
        if event.type == ADD_albero:
                posx_alberi = SCREEN_WIDTH - 20
                posy_alberi = random.randint(0, SCREEN_HEIGHT - 75)
                enemiesAlberi.append( (posx_alberi,posy_alberi) )
        
        # COMPARSA TRATTORI
        if event.type == add_trattore:
                posx_trattori = SCREEN_WIDTH - 20
                while True:
                    posy_trattori = random.randint(0, SCREEN_HEIGHT - 100)
                    if posy_trattori > posy_alberi + 75 or posy_trattori < posy_alberi - 75:
                        break
                
                enemiesTrattori.append( (posx_trattori,posy_trattori) )
        
        # COMPARSA MONETE
        if event.type == add_moneta:
                posx_monete = SCREEN_WIDTH - 20
                posy_monete = random.randint(0, SCREEN_HEIGHT - 100)
                while True:
                    posy_monete = random.randint(0, SCREEN_HEIGHT - 100)
                    if (posy_monete > posy_alberi + 75 or posy_monete < posy_alberi - 75) and (posy_monete > posy_trattori + 75 or posy_monete < posy_trattori - 75):
                        break
                enemiesMoneta.append( (posx_monete,posy_monete) )
      
       # PREMI "P" per mettere in pausa (o uscire dalla pausa)
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
         #   if paused:
          #      paused = False
           #     pygame.mixer.music.play(loops = -1)
            #    if paused:
             #       paused = True
              #      pygame.mixer.music.pause(loops = -1)
                
    # MOVIMENTO GIOCATORE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0: 
        x -= speed 
    if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - w: 
        x += speed 
    if keys[pygame.K_UP] and y > 0: 
        y -= speed 
    if keys[pygame.K_DOWN] and y < SCREEN_HEIGHT - h: 
        y += speed
    
    # scritta INIZIALE!!!
    if scritta:
        screen.blit(imgSfondo,(0,0))
        screen.blit(game_end,(190, 150))
        screen.blit(close_tip,(190,220))
        
        pygame.display.flip()
        continue 

    # AGGIUNTA DIMENSIONI IMMAGINE SFONDO
    screen.blit(imgSfondo,(0,0) )
    
    # DEFINISCO IL GIOCATORE
    player = screen.blit(imgMoto,(x,y))
    
    # APPARIZIONE ALBERI
    for i in range(len(enemiesAlberi)):
        posx_alberi,posy_alberi = enemiesAlberi[i]
        en = screen.blit(imgAlbero,(posx_alberi,posy_alberi))
        enemiesAlberi[i] = (posx_alberi - 5, posy_alberi)
        # SE IL GIOCATORE SI SCONTRA CON UN ALBERO RUNNING DIVENTA FALSE
        # E IL GIOCO FINISCE
        if player.colliderect(en):
            print("HAI PERSO SCEMOOO!")
            running = False
    
    # APPARIZIONE TRATTORI
    for i in range(len(enemiesTrattori)):
        posx_trattori,posy_trattori = enemiesTrattori[i]
        Trattore = screen.blit(imgTrattore,(posx_trattori,posy_trattori))
        enemiesTrattori[i] = (posx_trattori - 5, posy_trattori)
        # SE IL GIOCATORE SI SCONTRA CON UN TRATTORE RUNNING DIVENTA FALSE
        # E IL GIOCO FINISCE
        if player.colliderect(Trattore):
            print("HAI PERSO SCEMOOO!")
            running = False
    # SE IL GIOCATORE COLPISCE LE MONETE LA VELOCITA' AUMENTA DI 1 E LA MONETA SCOMPARE
    for i in range(len(enemiesMoneta)):
        posx_monete,posy_monete = enemiesMoneta[i]
        Moneta = screen.blit(imgMoneta,(posx_monete,posy_monete))
        enemiesMoneta[i] = (posx_monete - 5, posy_monete)
        if player.colliderect(Moneta):
            speed += 1
            enemiesMoneta.pop(i)
            break
    

    # AGGIORNA IL CODICE
    pygame.display.flip()

# CHIUDE PYGAME
pygame.quit()


