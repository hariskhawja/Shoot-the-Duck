import pygame
import sceneControl
import colours
import sceneControl
from itertools import repeat

pygame.init()
pygame.display.set_caption("Shoot the Duck")

orgScreen = pygame.display.set_mode((1200, 500))
screen = orgScreen.copy()
screenRect = screen.get_rect()
offset = repeat((0, 0))

def shake():
    s = -1
    for i in range(0, 3):
        for j in range(0, 20, 5):
            yield(j*s, j*s)
        for j in range(20, 0, 5):
            yield (j*s, j*s)
        
        s *= -1
    
    while True:
        yield (0, 0)

pygame.mouse.set_visible(False)

font = pygame.font.SysFont("Arial", 25)

FPS = 120
fpsClock = pygame.time.Clock()

quitVar = True

ducks = []

timer = 3100
score = 0

cursorColour = [255, 255, 255]
cursorColourDelay = 0

gameStage = 0

while quitVar:
    orgScreen.fill([0, 0, 0])
    screen.fill([0, 0, 0])

    if gameStage == 0: startButton = sceneControl.gameStart(screen, font)

    elif gameStage == 1: ducks, timer, score, gameStage = sceneControl.gameMain(screen, font, ducks, timer, score, gameStage)
    
    else: restartButton, quitButton = sceneControl.gameOver(screen, font, score)

    if cursorColourDelay <= 0: cursorColour = [255, 255, 255]

    else: cursorColourDelay -= 1

    sceneControl.cursorDraw(screen, cursorColour)

    orgScreen.blit(screen, next(offset))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            cursorColour = [255, 0, 0]
            cursorColourDelay = 10
            offset = shake()
            position = pygame.mouse.get_pos()

            if gameStage == 0 and startButton.collidepoint(pygame.mouse.get_pos()): gameStage = 1
            
            if gameStage == 2 and restartButton.collidepoint(pygame.mouse.get_pos()): 
                gameStage = 1
                timer = 3100
                score = 0

            if gameStage == 2 and quitButton.collidepoint(pygame.mouse.get_pos()): quitVar = False

            for duck in ducks:
                if (duck.direct == -1 and (position[0] >= duck.x - 9 and position[0] <= duck.x + 50) and (position[1] <= duck.y + 40 and position[1] >= duck.y - 9)) or (duck.direct == 1 and (position[0] <= duck.x + 9 and position[0] >= duck.x - 50) and (position[1] <= duck.y + 40 and position[1] >= duck.y - 9)):
                    score += colours.colourPoints(duck.colour)
                    ducks.remove(duck)

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()