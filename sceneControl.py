import pygame
import duckControl

def cursorDraw(surface):
    posX, posY = pygame.mouse.get_pos()

    pygame.draw.circle(surface, [255, 255, 255], (posX, posY), 5, width = 1)
    pygame.draw.circle(surface, [255, 255, 255], (posX, posY), 10, width = 1)
    pygame.draw.rect(surface, [255, 255, 255], (posX + 3, posY, 12, 1))
    pygame.draw.rect(surface, [255, 255, 255], (posX - 15, posY, 12, 1))
    pygame.draw.rect(surface, [255, 255, 255], (posX, posY - 15, 1, 12))
    pygame.draw.rect(surface, [255, 255, 255], (posX, posY + 3, 1, 12))

def gameStart(surface, font):
    startButton = pygame.draw.rect(surface, (255, 255, 255), (550, 250, 100, 50), width=1)
    startText = font.render("START", True, (255, 255, 255))
    startRect = startText.get_rect(center = (600, 275))
    surface.blit(startText, startRect)

    return startButton

def gameMain(surface, font, ducks, timer, score, gameStage):
    pygame.draw.rect(surface, [255, 255, 255], (0, 425, 1200, 1))

    timerText = font.render("TIME: " + str(int(timer / 100)), True, [255, 255, 255])
    timerRect = timerText.get_rect(center = (500, 450))
    surface.blit(timerText, timerRect)

    scoreText = font.render("SCORE: " + str(score), True, [255, 255, 255])
    scoreRect = scoreText.get_rect(center = (700, 450))
    surface.blit(scoreText, scoreRect)

    for duck in ducks:
        if duck.direct == 1 and duck.x > 1300: ducks.remove(duck)

        elif duck.direct == -1 and duck.x < -100: ducks.remove(duck)
        
        else: duck.duckDraw(surface)

    if timer > 0: 
        if timer % 50 == 0: ducks.append(duckControl.Duck())
        timer -= 1
    
    else: gameStage = 2
    
    return ducks, timer, score, gameStage

def gameOver(surface):
    pass