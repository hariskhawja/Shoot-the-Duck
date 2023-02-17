import pygame
import duckControl

def textDisplay(surface, font, text, coordinates):
    text = font.render(text, True, [255, 255, 255])
    textRect = text.get_rect(center = coordinates)
    surface.blit(text, textRect)

def cursorDraw(surface, cursorColour):
    posX, posY = pygame.mouse.get_pos()

    pygame.draw.circle(surface, cursorColour, (posX, posY), 5, width = 1)
    pygame.draw.circle(surface, cursorColour, (posX, posY), 10, width = 1)
    pygame.draw.rect(surface, cursorColour, (posX + 3, posY, 12, 1))
    pygame.draw.rect(surface, cursorColour, (posX - 15, posY, 12, 1))
    pygame.draw.rect(surface, cursorColour, (posX, posY - 15, 1, 12))
    pygame.draw.rect(surface, cursorColour, (posX, posY + 3, 1, 12))

def gameStart(surface, font):
    textDisplay(surface, font, "WELCOME TO SHOOT THE DUCK", (600, 200))

    startButton = pygame.draw.rect(surface, (255, 255, 255), (550, 275, 100, 50), width=1)
    textDisplay(surface, font, "START", (600, 300))

    return startButton

def gameMain(surface, font, ducks, timer, score, gameStage):
    pygame.draw.rect(surface, [255, 255, 255], (0, 425, 1200, 1))

    textDisplay(surface, font, "TIME: " + str(int(timer / 100)), (500, 450))
    textDisplay(surface, font, "SCORE: " + str(score), (700, 450))

    for duck in ducks:
        if duck.direct == 1 and duck.x > 1300: ducks.remove(duck)

        elif duck.direct == -1 and duck.x < -100: ducks.remove(duck)

        elif duck.y < -100: ducks.remove(duck)
        
        else: duck.duckDraw(surface)

    if timer > 0: 
        if timer % 50 == 0: ducks.append(duckControl.Duck())
        timer -= 1

    elif len(ducks) == 0: gameStage = 2
    
    return ducks, timer, score, gameStage

def gameOver(surface, font, score):
    textDisplay(surface, font, "GAME OVER", (600, 175))
    textDisplay(surface, font, "FINAL SCORE: " + str(score), (600, 250))

    restartButton = pygame.draw.rect(surface, (255, 255, 255), (425, 325, 150, 50), width=1)
    textDisplay(surface, font, "RESTART", (500, 350))

    quitButton = pygame.draw.rect(surface, (255, 255, 255), (625, 325, 150, 50), width=1)
    textDisplay(surface, font, "QUIT", (700, 350))

    return restartButton, quitButton