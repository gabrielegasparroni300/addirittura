# importa ed inizializza la libreria pygame
import pygame

pygame.init()

# variabili

SCREEN_WIDTH = pygame.display.get_desktop_sizes()[0][0]
SCREEN_HEIGHT = pygame.display.get_desktop_sizes()[0][1]

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

half_WIDTH = SCREEN_WIDTH // 2
half_HEIGHT = SCREEN_HEIGHT // 2

# fonts
Titlefont = pygame.font.SysFont('Impact', 70)
buttonFont = pygame.font.SysFont('Arial', 40)

# testi
textEsci = buttonFont.render('Esci' , True , "white")
textTitolo = Titlefont.render("Giochi", True, "red")
textButton1 = buttonFont.render("Jumper",True,"black")
textButton2 = buttonFont.render("Space something",True,"black")
textButton3 = buttonFont.render("Space wars",True,"black")
textButton4 = buttonFont.render("God protect me",True,"black")
textButton5 = buttonFont.render("Space invaders",True,"black")
textButton6 = buttonFont.render("Money catcher",True,"black")
textButton7 = buttonFont.render("Slot",True,"black")
textButton8 = buttonFont.render("Fuffy bird",True,"black")
textButton9 = buttonFont.render("SuperSpace",True,"black")
textButton10 = buttonFont.render("MotoRUN",True,"black")
textButton11 = buttonFont.render("PACMAN",True,"black")
textButton12 = buttonFont.render("Pong",True,"black")

# pulsanti
buttonEsci = pygame.Rect(half_WIDTH + 500, half_HEIGHT - 400, 100, 50)
buttonGioco1 = pygame.Rect(254, 368, 150, 100)
buttonGioco2 = pygame.Rect(254, 568, 250, 100)
buttonGioco3 = pygame.Rect(254, 768, 175, 100)
buttonGioco4 = pygame.Rect(658, 368, 225, 100)
buttonGioco5 = pygame.Rect(658, 568, 225, 100)
buttonGioco6 = pygame.Rect(658, 768, 225, 100)
buttonGioco7 = pygame.Rect(1062, 368, 150, 100)
buttonGioco8 = pygame.Rect(1062, 568, 150, 100)
buttonGioco9 = pygame.Rect(1062, 768, 200, 100)
buttonGioco10 = pygame.Rect(1466, 368, 175, 100)
buttonGioco11 = pygame.Rect(1466, 568, 175, 100)
buttonGioco12 = pygame.Rect(1466, 768, 150, 100)

# lo screen (con titolo)
pygame.display.set_caption("Schermata iniziale")


running = True

while running:
    # posizione del mouse
    mPos = pygame.mouse.get_pos()
    # serve a gestire la X di chiusura in alto
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # quando clicchi SOPRA il pulsante... FAI QUALCOSA!!!
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if buttonEsci.collidepoint(mPos):
                running = False

    # colora lo schermo
    screen.fill("oldlace")
    
    buttonColor = "red"
    buttonColorEsci = "red"
    if buttonEsci.collidepoint(mPos):
        buttonColorEsci = "crimson"
    rectEsci = pygame.draw.rect(screen,buttonColorEsci,buttonEsci)
    rectGioco1 = pygame.draw.rect(screen,buttonColor,buttonGioco1)
    rectGioco2 = pygame.draw.rect(screen,buttonColor,buttonGioco2)
    rectGioco3 = pygame.draw.rect(screen,buttonColor,buttonGioco3)
    rectGioco3 = pygame.draw.rect(screen,buttonColor,buttonGioco4)
    rectGioco3 = pygame.draw.rect(screen,buttonColor,buttonGioco5)
    rectGioco3 = pygame.draw.rect(screen,buttonColor,buttonGioco6)
    rectGioco3 = pygame.draw.rect(screen,buttonColor,buttonGioco7)
    rectGioco3 = pygame.draw.rect(screen,buttonColor,buttonGioco8)
    rectGioco3 = pygame.draw.rect(screen,buttonColor,buttonGioco9)
    rectGioco3 = pygame.draw.rect(screen,buttonColor,buttonGioco10)
    rectGioco3 = pygame.draw.rect(screen,buttonColor,buttonGioco11)
    rectGioco3 = pygame.draw.rect(screen,buttonColor,buttonGioco12)
    
    screen.blit(textTitolo, (half_WIDTH - 100,100))
    screen.blit(textEsci,(half_WIDTH + 500, half_HEIGHT - 400) )
    screen.blit(textButton1,(254,385))
    screen.blit(textButton2,(254,585))
    screen.blit(textButton3,(254,785))
    screen.blit(textButton4,(658,385))
    screen.blit(textButton5,(658,585))
    screen.blit(textButton6,(658,785))
    screen.blit(textButton7,(1062,385))
    screen.blit(textButton8,(1062,585))
    screen.blit(textButton9,(1062,785))
    screen.blit(textButton10,(1466,385))
    screen.blit(textButton11,(1466,585))
    screen.blit(textButton12,(1466,785))
    
    # aggiorna il contenuto dello schermo
    pygame.display.flip()

# Chiude pygame
pygame.quit()
