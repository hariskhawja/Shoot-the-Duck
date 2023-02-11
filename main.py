import pygame
import duckControl
import sceneControl
import colours
import sceneControl

pygame.init()
pygame.display.set_caption("Shoot the Duck")
screen = pygame.display.set_mode((1200, 500))

pygame.mouse.set_visible(False)

font = pygame.font.SysFont("Arial", 25)

FPS = 120
fpsClock = pygame.time.Clock()

quitVar = True

ducks = []

timer = 31000
score = 0

gameStage = 0

while quitVar:
    screen.fill([0, 0, 0])

    sceneControl.cursorDraw(screen)

    if gameStage == 0: startButton = sceneControl.gameStart(screen, font)

    elif gameStage == 1: ducks, timer, score, gameStage = sceneControl.gameMain(screen, font, ducks, timer, score, gameStage)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()

            if gameStage == 0 and startButton.collidepoint(pygame.mouse.get_pos()): gameStage = 1
            
            for duck in ducks:
                if duck.direct == -1:
                    if (position[0] >= duck.x - 9 and position[0] <= duck.x + 50) and (position[1] <= duck.y + 40 and position[1] >= duck.y - 9):
                        score += colours.colourPoints(duck.colour)
                        ducks.remove(duck)

                else:
                    if (position[0] <= duck.x + 9 and position[0] >= duck.x - 50) and (position[1] <= duck.y + 40 and position[1] >= duck.y - 9):
                        score += colours.colourPoints(duck.colour)
                        ducks.remove(duck)

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()