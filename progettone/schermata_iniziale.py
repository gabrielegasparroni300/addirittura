# importa ed inizializza la libreria pygame
import pygame
from pathlib import Path
import os
import subprocess

pygame.init()

# Immagini anteprima giochi
imgAntJumper = pygame.image.load("anteprimaJumper.png")
imgAntJumper = pygame.transform.scale(imgAntJumper,(250,100))
imgAntSpaceSomething = pygame.image.load("anteprimaSpaceSomething.png")
imgAntSpaceSomething = pygame.transform.scale(imgAntSpaceSomething,(250,100))
imgAntSpaceWars = pygame.image.load("anteprimaSpaceWars.png")
imgAntSpaceWars = pygame.transform.scale(imgAntSpaceWars,(250,100))
imgAntGodProtectMe = pygame.image.load("anteprimaGodProtectMe.png")
imgAntGodProtectMe = pygame.transform.scale(imgAntGodProtectMe,(250,100))
imgAntSpaceInvaders = pygame.image.load("anteprimaSpaceInvaders.png")
imgAntSpaceInvaders = pygame.transform.scale(imgAntSpaceInvaders,(250,100))
imgAntMoneyCatcher = pygame.image.load("anteprimaMoneyCatcher.png")
imgAntMoneyCatcher = pygame.transform.scale(imgAntMoneyCatcher,(250,100))
imgAntSlot = pygame.image.load("anteprimaSlot.png")
imgAntSlot = pygame.transform.scale(imgAntSlot,(250,100))
imgAntFuffyBird = pygame.image.load("anteprimaFuffyBird.png")
imgAntFuffyBird = pygame.transform.scale(imgAntFuffyBird,(250,100))
imgAntSuperSpace = pygame.image.load("anteprimaSuperSpace.png")
imgAntSuperSpace = pygame.transform.scale(imgAntSuperSpace,(250,100))
imgAntMotoRUN = pygame.image.load("anteprimaMotoRUN.png")
imgAntMotoRUN = pygame.transform.scale(imgAntMotoRUN,(250,100))
imgAntPACMAN = pygame.image.load("anteprimaPACMAN.png")
imgAntPACMAN = pygame.transform.scale(imgAntPACMAN,(250,100))
imgAntPong = pygame.image.load("anteprimaPong.png")
imgAntPong = pygame.transform.scale(imgAntPong,(250,100))

# Path Istruzioni

istruzioni = Path.cwd() / "istruzioni"

istrJumper = istruzioni / "istruzioni_Jumper.txt"
istrFuffyBird = istruzioni / "istruzioni_FuffyBird.txt"
istrGodProtectMe = istruzioni / "istruzioni_GodProtectMe.txt"
istrMoneyCatcher = istruzioni / "istruzioni_MoneyCatcher.txt"
istrMotoRun = istruzioni / "istruzioni_MotoRun.txt"
istrPacman = istruzioni / "istruzioni_Pacman.txt"
istrPong = istruzioni / "istruzioni_Pong.txt"
istrSlot = istruzioni / "istruzioni_Slot.txt"
istrSnake = istruzioni / "istruzioni_Snake.txt"
istrSpaceInvaders = istruzioni / "istruzioni_SpaceInvaders.txt"
istrSpaceWars = istruzioni / "istruzioni_SpaceWars.txt"
istrSpaceSomething = istruzioni / "istruzioni_SpaceSomething.txt"
istrSuperSpace = istruzioni / "istruzioni_SuperSpace.txt"

# Path Giochi
giochi = Path.cwd() / "games"

pathJumper = giochi / "Jumper" / "__init__.py"
pathFuffyBird = giochi / "FuffyBird" / "__init__.py"
pathGodProtectMe = giochi / "GodProtectMe" / "__init__.py"
pathJumper = giochi / "Jumper" / "__init__.py"
pathMoneyCatcher = giochi / "MoneyCatcher" / "__init__.py"
pathMotoRun = giochi / "MotoRun" / "__init__.py"
pathPacman = giochi / "Pacman" / "__init__.py"
pathPong = giochi / "Pong" / "__init__.py"
pathSlot = giochi / "Slot" / "__init__.py"
pathSpaceInvaders = giochi / "SpaceInvaders" / "__init__.py"
pathSpaceSomething = giochi / "SpaceSomething" / "__init__.py"
pathSpaceWars = giochi / "SpaceWars" / "__init__.py"
pathSuperSpace = giochi / "SuperSpace" / "__init__.py"

# variabili

SCREEN_WIDTH = pygame.display.get_desktop_sizes()[0][0]
SCREEN_HEIGHT = pygame.display.get_desktop_sizes()[0][1]

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

half_WIDTH = SCREEN_WIDTH // 2
half_HEIGHT = SCREEN_HEIGHT // 2

# fonts

imgTITOLO = pygame.image.load("GIOCHI.png")
imgTITOLO = pygame.transform.scale(imgTITOLO,(446,120))

# Titlefont = pygame.font.SysFont('Impact', 70)
buttonFont = pygame.font.SysFont('Arial', 40)

# testi
textEsci = buttonFont.render('Esci' , True , "white")
# textTitolo = Titlefont.render("Giochi", True, "red")
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
buttonGioco1 = pygame.Rect(225, 368, 250, 100)
buttonGioco2 = pygame.Rect(225, 568, 250, 100)
buttonGioco3 = pygame.Rect(225, 768, 250, 100)
buttonGioco4 = pygame.Rect(632, 368, 250, 100)
buttonGioco5 = pygame.Rect(632, 568, 250, 100)
buttonGioco6 = pygame.Rect(632, 768, 250, 100)
buttonGioco7 = pygame.Rect(1039, 368, 250, 100)
buttonGioco8 = pygame.Rect(1039, 568, 250, 100)
buttonGioco9 = pygame.Rect(1039, 768, 250, 100)
buttonGioco10 = pygame.Rect(1446, 368, 250, 100)
buttonGioco11 = pygame.Rect(1446, 568, 250, 100)
buttonGioco12 = pygame.Rect(1446, 768, 250, 100)

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
        # Jumper
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonGioco1.collidepoint(mPos):
                subprocess.run(["python", pathJumper])
                
        # Space Something
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonGioco2.collidepoint(mPos):
                subprocess.run(["python", pathSpaceSomething])

        # Space wars
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonGioco3.collidepoint(mPos):
                subprocess.run(["python", pathSpaceWars])
                
        # God protect me
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonGioco4.collidepoint(mPos):
                subprocess.run(["python", pathGodProtectMe])
                
        # Space invaders
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonGioco5.collidepoint(mPos):
                subprocess.run(["python", pathSpaceInvaders])
                
        # Money catcher
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonGioco6.collidepoint(mPos):
                subprocess.run(["python", pathMoneyCatcher])
                
        # Slot
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonGioco7.collidepoint(mPos):
                subprocess.run(["python", pathSlot])
                
        # Fuffy bird
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonGioco8.collidepoint(mPos):
                subprocess.run(["python", pathFuffyBird])
                
        # SuperSpace
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonGioco9.collidepoint(mPos):
                subprocess.run(["python", pathSuperSpace])
                
        # MotoRUN
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonGioco10.collidepoint(mPos):
                subprocess.run(["python", pathMotoRun])
                
        # PACMAN
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonGioco11.collidepoint(mPos):
                subprocess.run(["python", pathPacman])
                
        # Pong
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonGioco12.collidepoint(mPos):
                subprocess.run(["python", pathPong])
                
        

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
    
    # screen.blit(textTitolo, (half_WIDTH - 100,100))
    screen.blit(imgTITOLO,(half_WIDTH - 223,100))
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
    
    if buttonGioco1.collidepoint(mPos):
        screen.blit(imgAntJumper,(225,368))
    if buttonGioco2.collidepoint(mPos):
        screen.blit(imgAntSpaceSomething,(225,568))
    if buttonGioco3.collidepoint(mPos):
        screen.blit(imgAntSpaceWars,(225,768))
    if buttonGioco4.collidepoint(mPos):
        screen.blit(imgAntGodProtectMe,(632,368))
    if buttonGioco5.collidepoint(mPos):
        screen.blit(imgAntSpaceInvaders,(632,568))
    if buttonGioco6.collidepoint(mPos):
        screen.blit(imgAntMoneyCatcher,(632,768))
    if buttonGioco7.collidepoint(mPos):
        screen.blit(imgAntSlot,(1039,368))
    if buttonGioco8.collidepoint(mPos):
        screen.blit(imgAntFuffyBird,(1039,568))
    if buttonGioco9.collidepoint(mPos):
        screen.blit(imgAntSuperSpace,(1039,768))
    if buttonGioco10.collidepoint(mPos):
        screen.blit(imgAntMotoRUN,(1446,368))
    if buttonGioco11.collidepoint(mPos):
        screen.blit(imgAntPACMAN,(1446,568))
    if buttonGioco12.collidepoint(mPos):
        screen.blit(imgAntPong,(1446,768))
    
    
    
    
    # aggiorna il contenuto dello schermo
    pygame.display.flip()

# Chiude pygame
pygame.quit()
