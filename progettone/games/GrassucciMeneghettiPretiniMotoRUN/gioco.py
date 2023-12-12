# IMPORTAZIONE PYGAME E RANDOM
import pygame
import random

#INIZIO PYGAME
pygame.init()

#dimensioni dello schermo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#suono
pygame.mixer.init() 
pygame.mixer.music.load("Honda CR 500 Sound Check Braaap!!!-0-16.9.mp3") 
pygame.mixer.music.set_volume(0.5) 
pygame.mixer.music.play(loops = -1)

# impostazione sfondo
imgSfondo = pygame.image.load("terreno3.png")
screen = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH,SCREEN_HEIGHT))

#titolo 
Titolo = pygame.font.SysFont("Rockwell Extra Bold", 100)
scrittaGioco = pygame.font.SysFont("Rockwell Extra Bold", 50)

# SCRITTE INIZIALI
game_end = Titolo.render("MOTO RUN", True, "black")
close_tip = scrittaGioco.render("clicca spazio per giocare", True, "black")

# TITOLO GIOCO
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
pygame.display.set_caption("MOTO RUN")

#AGGIUNTA IMMAGINE GIOCATORE
imgMoto = pygame.image.load("motoUfficiale.png")
imgMoto = pygame.transform.scale(imgMoto,(100, 100))

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
pygame.time.set_timer(add_moneta, 800)


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
        
        #-------------------------------------------------------------------------------------
    # COMPARSA NEMICI
    # creo una lista per creare quattro corsie
    listaCorsie = [25,175,325,475]
    
    contaAlberi = 0
    contaTrattori = 0
    contaMonete = 0
    
    # COMPARSA ALBERI  
    if event.type == ADD_albero:
        contaAlberi += 1
        albero_x = SCREEN_WIDTH - 25
        corsiaAlbero = random.randint(0,3)
        albero_y = listaCorsie[corsiaAlbero]
        enemiesAlberi.append((albero_x,albero_y))
    
    # COMPARSA TRATTORI
    if event.type == add_trattore:
        contaTrattori += 1
        trattore_x = SCREEN_WIDTH - 20
        while True:
            if contaTrattori == contaAlberi:
                corsiaTrattore = random.randint(0,3)
                if corsiaTrattore != corsiaAlbero:
                    break
            
        trattore_y = listaCorsie[corsiaTrattore]
        enemiesTrattori.append((trattore_x,trattore_y))
    
    # COMPARSA MONETE
    if event.type == add_moneta:
        contaMonete += 1
        moneta_x = SCREEN_WIDTH - 20
        while True:
            corsiaMoneta = random.randint(0,3)
            if corsiaMoneta != corsiaAlbero and corsiaMoneta != corsiaTrattore:
                break
        moneta_y = listaCorsie[corsiaMoneta]
        enemiesMoneta.append((moneta_x,moneta_y))
      
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
        posx,posy = enemiesAlberi[i]
        en = screen.blit(imgAlbero,(posx,posy))
        enemiesAlberi[i] = (posx - 5, posy)
        # SE IL GIOCATORE SI SCONTRA CON UN ALBERO RUNNING DIVENTA FALSE
        # E IL GIOCO FINISCE
        if player.colliderect(en):
            print("HAI PERSO SCEMOOO!")
            running = False
    
    # APPARIZIONE TRATTORI
    for i in range(len(enemiesTrattori)):
        posizionex,posizioney = enemiesTrattori[i]
        Trattore = screen.blit(imgTrattore,(posizionex,posizioney))
        enemiesTrattori[i] = (posizionex - 5, posizioney)
        # SE IL GIOCATORE SI SCONTRA CON UN TRATTORE RUNNING DIVENTA FALSE
        # E IL GIOCO FINISCE
        if player.colliderect(Trattore):
            print("HAI PERSO SCEMOOO!")
            running = False
    # SE IL GIOCATORE COLPISCE LE MONETE LA VELOCITA' AUMENTA DI 1 E LA MONETA SCOMPARE
    for i in range(len(enemiesMoneta)):
        posizionex,posizioney = enemiesMoneta[i]
        Moneta = screen.blit(imgMoneta,(posizionex,posizioney))
        enemiesMoneta[i] = (posizionex - 5, posizioney)
        if player.colliderect(Moneta):
            speed += 1
            enemiesMoneta.pop(i)
            break
    
    print(speed)

    # AGGIORNA IL CODICE
    pygame.display.flip()

# CHIUDE PYGAME
pygame.quit()
