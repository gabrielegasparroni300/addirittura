#Nicolò Draghetti
#2 BS
#Slot Machine

# importa ed inizializza la libreria pygame
import pygame

pygame.init()


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 612

# lo screen
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
pygame.display.set_caption("Slot Machine")

# facile...
running = True

while running:
    # serve a gestire la X di chiusura in alto
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # colora lo schermo di verde
    screen.fill("black")
    
    #importa l'immagine della slot machine
    imgSfondo = pygame.image.load("slot.jpg")
    screen.blit(imgSfondo,(0,0))
    
     # rettangolo BIANCO che va dal punto (180,260) alto 118, largo 170
    # r è il rettangolo che contiene il rettangolo disegnato
    r = pygame.draw.rect(screen, "white", (180, 260, 62, 90))
    
    # rettangolo BIANCO che va dal punto (276,260) alto 118, largo 170
    # r è il rettangolo che contiene il rettangolo disegnato
    r = pygame.draw.rect(screen, "white", (276, 260, 62, 90))
    
    # rettangolo BIANCO che va dal punto (372,260) alto 118, largo 170
    # r è il rettangolo che contiene il rettangolo disegnato
    r = pygame.draw.rect(screen, "white", (372, 260, 62, 90))
    
    # Update display content
    pygame.display.flip()

    # DENTRO il FOR che gestisce gli eventi...
    # Se l'evento è la pressione di un tasto...
    # ... e il tasto è il tasto ESC.. esc(i)!
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = False


# Chiude pygame
pygame.quit()
