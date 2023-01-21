import pygame
import duckControl
import sceneControl
import colours
# import generationControl
# from generationControl import ducks

pygame.init()
pygame.display.set_caption("Shoot the Duck")
screen = pygame.display.set_mode((1200, 500))

pygame.mouse.set_visible(False)

font = pygame.font.SysFont("Arial", 25)

FPS = 120
fpsClock = pygame.time.Clock()

quitVar = True

ducks = []

timer = 10000
score = 0

while quitVar:
    screen.fill([0, 0, 0])
    timerText = font.render("Time: " + str(int(timer / 100)), True, [255, 255, 255])
    timerRect = timerText.get_rect(center = (120, 90))
    screen.blit(timerText, timerRect)

    scoreText = font.render("Score: " + str(score), True, [255, 255, 255])
    scoreRect = scoreText.get_rect(center = (120, 190))
    screen.blit(scoreText, scoreRect)


    for duck in ducks:
        if duck.direct == 1 and duck.x > 1300: ducks.remove(duck)

        elif duck.direct == -1 and duck.x < -100: ducks.remove(duck)
        
        else: duck.duckDraw(screen)

    sceneControl.cursorDraw(screen)
    sceneControl.terrainDraw(screen)

    if not timer <= 0: 
        if timer % 50 == 0: ducks.append(duckControl.Duck())
        timer -= 1

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            
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