import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
from pygame import mixer


pygame.init()
windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Shapes!')

pygame.mixer.init()
pygame.mixer.music.load('106.mp3')
pygame.mixer.music.play(-1)

# Renamed variables to be consistent
# Moved variables out of the while loop
#aSquareX = windowWidth / 2
#aSquareY = windowHeight / 2
aSquareX = 0.0
aSquareY = 0.0
bSquareX = 0.0
bSquareY = 0.0
cSquareX = 0.0
cSquareY = 0.0
dSquareX = 0.0
dSquareY = 0.0
eSquareX = 0.0
eSquareY = 0.0
fSquareX = 0.0
fSquareY = 0.0
gSquareX = 0.0
gSquareY = 0.0
hSquareX = 0.0
hSquareY = 0.0
ASquareX = 600
ASquareY = 500
BSquareX = 600
BSquareY = 500
CSquareX = 600
CSquareY = 500
DSquareX = 600
DSquareY = 500
ESquareX = 600
ESquareY = 500
FSquareX = 600
FSquareY = 500
xSquareX = 0.0
xSquareY = 480
OSquareX = 0.0
OSquareY = 470
RSquareX = 40
RSquareY = 0.0
TSquareX = 640
TSquareY = 0.0
MSquareX = 480
MSquareY = 600




# Joined the two while loops into one
while True:
   # move to right and down
    surface.fill((200, 0, 0))
    pygame.draw.rect(surface, (255, 0, 0), (random.randint(0, windowWidth), random.randint(0, windowHeight), 10, 10))

    surface.fill((0, 0, 0))
    pygame.draw.rect(surface, (255, 228, 225),
     (aSquareX, aSquareY, 60, 60))
    aSquareX += 0.7
    aSquareY += 0.7

    pygame.draw.rect(surface, (205, 92, 92),
     (bSquareX, bSquareY, 30, 30))
    bSquareX += 0.6
    bSquareY += 0.6
    

    pygame.draw.rect(surface, (135, 205, 255),
       (cSquareX, cSquareY, 40, 40))
    cSquareX += 0.4
    cSquareY += 0.4
    #blueSquareVX += 0.1
    #blueSquareVY += 0.1


    pygame.draw.rect(surface, (0, 0, 255),
       (dSquareX, dSquareY, 50, 50))
    dSquareX += 0.2
    dSquareY += 0.2

    pygame.draw.ellipse(surface, (230, 230, 250),
       (eSquareX, eSquareY, 25, 25))
    eSquareX += 0.45
    eSquareY += 0.45

    pygame.draw.ellipse(surface, (225, 228, 225),
       (fSquareX, fSquareY, 35, 35))
    fSquareX += 0.68
    fSquareY += 0.68

    pygame.draw.ellipse(surface, (240, 255, 240),
       (gSquareX, gSquareY, 45, 45))
    gSquareX += 0.50
    gSquareY += 0.50

    pygame.draw.ellipse(surface, (255, 250, 205),
       (hSquareX, hSquareY, 55, 55))
    hSquareX += 0.26
    hSquareY += 0.26
    
    # move to left and down
    pygame.draw.rect(surface, (135,206,250),
       (ASquareX, ASquareY, 25, 25))
    ASquareX += -0.6
    ASquareY += -0.6

    pygame.draw.ellipse(surface, (248,248,255),
       (BSquareX, BSquareY, 45, 45))
    BSquareX += -0.56
    BSquareY += -0.56

    pygame.draw.rect(surface, (255,20,147),
       (CSquareX, CSquareY, 48, 48))
    CSquareX += -0.4
    CSquareY += -0.4

    pygame.draw.ellipse(surface, (255,255,0),
       (DSquareX, DSquareY, 65, 65))
    DSquareX += -0.35
    DSquareY += -0.35

    pygame.draw.rect(surface, (123,104,238),
       (ESquareX, ESquareY, 55, 55))
    ESquareX += -0.28
    ESquareY += -0.28

    pygame.draw.ellipse(surface, (255, 0, 255),
       (FSquareX, FSquareY, 55, 48))
    FSquareX += -0.2
    FSquareY += -0.2

    #111
    pygame.draw.ellipse(surface, (255, 0, 255),
       (xSquareX, xSquareY, 55, 48))
    xSquareX += 0.18
    xSquareY -= 0.18

    pygame.draw.rect(surface, (191, 239, 255),
       (OSquareX, OSquareY, 25, 25))
    OSquareX += 0.13
    OSquareY -= 0.13

    #2222from up tp down
    pygame.draw.ellipse(surface, (185, 211, 238),
       (RSquareX, RSquareY, 30, 30))
    #OSquareX += 0.13
    RSquareY += 0.28

    #from rigt upcorner to left and down
    pygame.draw.ellipse(surface, (191, 239, 255),
       (TSquareX, TSquareY, 35, 35))
    TSquareX -= 0.13
    TSquareY += 0.13

    #from down to up
    pygame.draw.ellipse(surface, (191, 239, 255),
       (MSquareX, MSquareY, 35, 35))
    #MSquareX -= 0.13
    MSquareY -= 0.33



    # Do not capitalize the .get() method for pygame.event class
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()

    # Misspelled pygame.display
    pygame.display.update()
