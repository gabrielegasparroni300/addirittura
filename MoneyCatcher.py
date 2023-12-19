#Gruppo Bruschi Frontalini  

#importo la libreria
import pygame
import random
import time
#importo funzione
import score


#inizio pygame
pygame.init()

pygame.mixer.music.load("retro-wave-style-track-59892.mp3") 
pygame.mixer.music.set_volume(0.3) 
pygame.mixer.music.play()

#--------------------------------------------------------
#SUONI
#suono moneta
MONETA_SOUND = pygame.mixer.Sound("monetina.mp3")
pygame.mixer.Sound.set_volume(MONETA_SOUND , 0.5)

GRUZZOLETTO_SOUND = pygame.mixer.Sound("bonusuono.mp3")
pygame.mixer.Sound.set_volume(GRUZZOLETTO_SOUND , 0.5)
#-----------------------------------------------------------
#DIMENSIONE E TITOLO DELLO SCHERMO

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Money Catcher")

#----------------------------------------------------------------------------------------
# FONT DELLE SCRITTE
#oggetto_testo = oggetto_font.render(stringa, True, colore, sfondo (opzionale) )

#Score font
Scorefont = pygame.font.SysFont('Impact', 30)

#Score point
score_point = Scorefont.render("0", True, "white")

#Hanger font
Hangerfont = pygame.font.SysFont('Impact', 70)

#Hanger
hanger_text = Hangerfont.render("AWESOME", True, "mediumorchid")

#Game font
GameEndfont = pygame.font.SysFont('Impact', 70)

#Game
game_end = GameEndfont.render("GAME OVER", True, "blueviolet")

#scritta punti
Scrittafont = pygame.font.SysFont('Impact', 20)

moneta_text = Scrittafont.render("Moneta : +1", True, "gold")
gruzzoletto_text = Scrittafont.render("Gruzzoletto : +5", True, "green")
alieno_text = Scrittafont.render("Alieno : morte", True, "white")

#----------------------------------------------------------------------------------------------------------
#EVENTI 
#crea un nuovo (tipo di) evento (da gestire nel for degli eventi sotto)
#che verrà scatenato ogni TOT ms

#Evento monete
ADD_MONEY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_MONEY, 499)

# l'elenco delle monete
money = []

#---------------------------------------------------------------------------------
#lista gruzzoletti 
hanger = []

#--------------------------------------------------------------------------------------------------------
# Evento nemici
ADD_ENEMY = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_ENEMY, 1587)

# l'elenco dei nemici
enemies = []

#-----------------------------------------------------------------
#IMMAGINI SFONDO, NAVICELLA, MONETE, ALIENI,GRUZZOLETTO
imgSfondo = pygame.image.load("spaziosfondo.jpg") 
imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH,SCREEN_HEIGHT))
imgNavicella = pygame.image.load("razzo.png") 
imgNavicella = pygame.transform.scale(imgNavicella,(100,120))
imgMoneta = pygame.image.load("Moneta.png") 
imgMoneta = pygame.transform.scale(imgMoneta,(40,40))
imgAlieno = pygame.image.load("alienogiusto.png")
imgAlieno = pygame.transform.scale(imgAlieno,(60,70)) 
imgGruzzoletto = pygame.image.load("gruzzoletto.png")
imgGruzzoletto = pygame.transform.scale(imgGruzzoletto, (90, 90))

x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT // 2

widthNavicella = 100
aggiungiBottino = False
speed = 8

speedMoney= 5
speedHanger = 5
speedEnemies = 5

running = True
devistoppare = False
scrittainiziale = True
contaScore = 0

    
while running: #eseguito solo se running è ancora True
    
    pygame.time.delay(10)
    
    #considera tutti gli eventi che accadono e che pygame intercetta 
    for event in pygame.event.get():
                
        # serve a gestire la X di chiusura in alto
        if event.type == pygame.QUIT:
            running = False
        
        #se l'evento è un tasto premuto
        if event.type == pygame.KEYDOWN:
            
            #e il tasto è ESC
            if event.key == pygame.K_ESCAPE:
                running = False
                
        #se l'evento è aggiungere una moneta       
        if event.type == ADD_MONEY:
            
            #si creano le posizioni della moneta e le si aggiungono alla lista dellle monete
            posx = random.randint(0,SCREEN_WIDTH-100)
            posy = random.randint(0,200)
            money.append((posx,posy))
                
        #se l'evento è aggiungere un nemico
        if event.type == ADD_ENEMY:
            
            #si creano le posizioni del nemico e le si aggiungono alla lista dei nemici
            posxEnemies = random.randint(0,SCREEN_WIDTH-100)
            posyEnemies = random.randint(0,200)
            enemies.append( (posxEnemies,posyEnemies) )
        
        #se l'evento è aggiungere gruzzoletto
        if contaScore%20 == 0 and contaScore != 0:
            aggiungiBottino = True
            
        if aggiungiBottino == True:
            #si creano le posizioni della moneta e le si aggiungono alla lista dellle monete
            posxHanger = random.randint(0,SCREEN_WIDTH-100)
            posyHanger = random.randint(0,200)
            hanger.append((posxHanger,posyHanger))
            aggiungiBottino = False
            contaScore += 1
            
    # per il movimento della navicella
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and x > 0: 
        x -= speed 
    if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - 100: 
        x += speed
    
        
    #imposto lo sfondo e scritte
    screen.blit(imgSfondo,(0,0))
    screen.blit(score_point, (550,0))
    screen.blit(moneta_text, (0,0))
    screen.blit(gruzzoletto_text, (0,20))
    screen.blit(alieno_text, (0,40))
    
    player = screen.blit(imgNavicella,(x,525))
    
    #per la presenza di monete
    for n in range (len(money)):
        posx, posy = money[n]

        # Money è la moneta
        MONEY = screen.blit(imgMoneta,(posx,posy))
        
        #metto la velocità alla moneta
        posy += speedMoney
            
        money[n] = (posx,posy)
        # se questa moneta "collide" con il punto (x,y) ove si trova il giocatore...
        if player.colliderect(MONEY):
            
            #aumento punteggio
            contaScore += 1
            score_point = Scorefont.render(score.score(contaScore), True, "white")
            
            #elimino dalla lista
            money.pop(n)
            
            #suono monete
            pygame.mixer.Sound.play(MONETA_SOUND)
            break
    
    #per la presenza dei gruzzoletti
    for c in range(len(hanger)):
        posxHanger, posyHanger = hanger[c]

        # Hanger sono più monete
        HANGER = screen.blit(imgGruzzoletto,(posxHanger,posyHanger))
        
        #metto velocità al gruzzoletto
        posyHanger += speedHanger
            
        hanger[c] = (posxHanger,posyHanger)
        
        # se queste monete "collidono" con il punto (x,y) ove si trova il giocatore...
        if player.colliderect(HANGER):
            
            #suono bonus
            pygame.mixer.Sound.play(GRUZZOLETTO_SOUND)
           
            #aumento punteggio
            contaScore += 4
            score_point= Scorefont.render(score.score(contaScore), True, "white")
            
            #elimino dalla lista
            hanger.pop(c)
            
            #aggiunta scritta
            screen.blit(hanger_text, (150,0))
            break   
    
    # per la presenza di alieni
    for i in range (len(enemies)):
        posxEnemies, posyEnemies = enemies[i]

        # Alien è l'alieno
        Alien = screen.blit(imgAlieno, (posxEnemies,posyEnemies)) 
        
        #metto velocità aggli alieni
        posyEnemies += speedEnemies
        
        enemies[i] = (posxEnemies,posyEnemies)
        # se questo alieno "collide" con il punto (x,y) ove si trova il giocatore...
        
        if player.colliderect(Alien):
            
            #suono morte
            pygame.mixer.music.load("mortesuono.mp3") 
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
            
            #scritta alla fine e velocità
            screen.blit(game_end, (150,300))
            devistoppare = True
            speedEnemies = 0
            speedMoney = 0
           
            #il gioco si ferma
            running = False
            
    #per aggiornare pygame
    pygame.display.flip()
    
    if devistoppare:
        
        # qui stoppi
        time.sleep(2)
        devistoppare = False
        
#fine pygame
pygame.quit()