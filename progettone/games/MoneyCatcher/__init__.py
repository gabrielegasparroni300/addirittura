#Gruppo Bruschi Frontalini  

#importo la libreria
import pygame
import random
import time
import os
#importo funzione
import score

os.environ['SDL_VIDEO_CENTERED'] = '1'

#inizio pygame
pygame.init() 

#--------------------------------------------------------
#SUONI
#suono moneta
pygame.mixer.init() 

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
imgSfondo_path = os.path.join(os.path.dirname(__file__), "spaziosfondo.jpg")
imgSfondo = pygame.image.load(imgSfondo_path) 
imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH,SCREEN_HEIGHT))
imgNavicella_path = os.path.join(os.path.dirname(__file__), "razzo.png")
imgNavicella = pygame.image.load(imgNavicella_path) 
imgNavicella = pygame.transform.scale(imgNavicella,(80,100))
imgMoneta_path = os.path.join(os.path.dirname(__file__), "Moneta.png")
imgMoneta = pygame.image.load(imgMoneta_path)
imgMoneta = pygame.transform.scale(imgMoneta,(40,40))
imgAlieno_path = os.path.join(os.path.dirname(__file__), "alienogiusto.png")
imgAlieno = pygame.image.load(imgAlieno_path)
imgAlieno = pygame.transform.scale(imgAlieno,(60,70))
imgGruzzoletto_path = os.path.join(os.path.dirname(__file__), "gruzzoletto.png")
imgGruzzoletto = pygame.image.load(imgGruzzoletto_path)
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
            musicMonetina_path = os.path.join(os.path.dirname(__file__), "monetina.mp3")
            pygame.mixer.music.load(musicMonetina_path) 
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
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
            musicBonusuono_path = os.path.join(os.path.dirname(__file__), "bonusuono.mp3")
            pygame.mixer.music.load(musicBonusuono_path) 
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
           
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
            musicMortesuono_path = os.path.join(os.path.dirname(__file__), "mortesuono.mp3")
            pygame.mixer.music.load(musicMortesuono_path)
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
