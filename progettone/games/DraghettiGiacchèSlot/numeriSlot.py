import pygame
import random
import time

pygame.init()

#variabili schermo

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 612


#variabili gioco
numero1 = ""
conta = 0
tentativo = 0
vittoria = 0
soldi = 20
start = 0
fine = 0
paused = False

#screen set
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Slot Machine")

#font
Numberfont = pygame.font.SysFont('Impact', 70)
Normalfont = pygame.font.SysFont('Impact', 30)
Creditfont = pygame.font.SysFont('Impact', 50)
Titlefont = pygame.font.SysFont('Impact', 100)
vincita = ""

#scritte fisse
credito = Normalfont.render("CREDITO:", True , "yellow")
# avvertenze = pygame.image.load("black2.jpg")
avvertenze = pygame.image.load("Avvertenze_nuovo.png")
Fine = pygame.image.load("Finale.jpg")
vittoria999 = pygame.image.load("Schermata_di_vincita.png")
istruzioniSpazio = Normalfont.render('_Space_ : Gioca' , True , 'yellow')
istruzioniEsc = Normalfont.render('_Escape_ : Cash Out' , True , 'yellow')
# attenzione = Normalfont.render('Attenzione\nIl Gioco Può Creare\nDipendenza' , True , "yellow")



#running e pausa
running = True
paused = False


#immagini e audio
imgSfondo = pygame.image.load("slot.jpg")


pygame.mixer.init() 
pygame.mixer.music.load("gamemusic-6082.mp3") 
pygame.mixer.music.set_volume(0.7) 
pygame.mixer.music.play(loops = -1)


#inizio
while running:
    
    #start
    if start == 0:
        screen.blit(avvertenze, (0,0))
#         screen.blit(attenzione, (0,0))
        pygame.display.flip()
        pygame.mixer.music.pause()
        time.sleep(4)
        pygame.mixer.music.play(loops = -1)

        start += 1
    
    credito7 = Titlefont.render(f"{str(soldi)} crediti" , True , "yellow")

    #eventi se schiaccio tasti
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if soldi != 0:
                screen.blit(vittoria999, (0,0))
                screen.blit(credito7, (245,450))
                pygame.display.flip()
                time.sleep(4)
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            running = True
            conta = 0
            tentativo = 0
    
    


    
#     if start == 0:
#         screen.blit(avvertenze, (0,0))
#         time.sleep(5)
#         start += 1
    
    #soldi
    if soldi == 0:
        if fine == 0:
            time.sleep(0.7)
            fine += 1
        
        pygame.mixer.music.pause()
        screen.blit(Fine , (0,0))
        pygame.display.flip()
        
#         FineGioco = Titlefont.render("Hai Finito Il Credito" , True , "red" , "white")
#         screen.blit(FineGioco, (SCREEN_WIDTH/2 , SCREEN_HEIGHT/2+100))
        continue
    
    
    
    #numeri casuali
    if conta != 20:
        numero1 = random.randint(1,6)
        colonna1 = Numberfont.render(str(numero1), True, "red" )
        
        numero2 = random.randint(1,6)
        colonna2 = Numberfont.render(str(numero2), True, "red" )
        
        numero3 = random.randint(1,6)
        colonna3 = Numberfont.render(str(numero3), True, "red" )
        
        conta += 1

        
        time.sleep(0.1)

    
    #vittoria/sconfitta
    if conta == 20 and tentativo == 0:
        if int(numero1) == int(numero2) and int(numero2) == (numero3):
            soldi += 10 * int(numero1)
            vittoria += 1
        #elif int(numero1) != int(numero2) or int(numero2) != (numero3):
        else:
            soldi -= 1
            vittoria = 0
            
    ContaSoldi = Creditfont.render(str(soldi), True , "yellow")

        
    
    
    

    
    
    #scritta vittoria/sconfitta
    if conta == 20:
        tentativo = 1
        if int(numero1) == int(numero2) and int(numero2) == (numero3):
            vincita = "HAI VINTO"
            

        else:
            vincita = "HAI PERSO"

    VincitaScritta = Numberfont.render(vincita, True, "red")
    
    

    #blits        
    screen.fill("black")
    screen.blit(imgSfondo, (0,0))
    r = pygame.draw.rect(screen, "white", (180, 260, 62, 90))
    
    # rettangolo BIANCO che va dal punto (276,260) alto 62, largo 90
    # r è il rettangolo che contiene il rettangolo disegnato
    r = pygame.draw.rect(screen, "white", (276, 260, 62, 90))
    
    # rettangolo BIANCO che va dal punto (372,260) alto 62, largo 90
    # r è il rettangolo che contiene il rettangolo disegnato
    r = pygame.draw.rect(screen, "white", (372, 260, 62, 90))
    
    screen.blit(colonna1, (192,260))
    screen.blit(colonna2, (288,260))
    screen.blit(colonna3, (384,260))
    screen.blit(credito, (620,100))
    screen.blit(ContaSoldi, (800 , 85))
    screen.blit(istruzioniSpazio , (620 , 500))
    screen.blit(istruzioniEsc , (620 , 550))
    
    
    
    
    
    if conta == 20:
        screen.blit(VincitaScritta,(170,500))
    
    
    
    
    
    
    pygame.display.flip()

    

pygame.quit()
