import pygame
import duckControl
import sceneControl

pygame.init()
pygame.display.set_caption("Shoot the Duck")
screen = pygame.display.set_mode((1200, 500))

pygame.mouse.set_visible(False)

FPS = 120
fpsClock = pygame.time.Clock()

quitVar = True

ducks = []

ducks.append(duckControl.Duck())
ducks.append(duckControl.Duck())
ducks.append(duckControl.Duck())
ducks.append(duckControl.Duck())
ducks.append(duckControl.Duck())
ducks.append(duckControl.Duck())
ducks.append(duckControl.Duck())
ducks.append(duckControl.Duck())

timer = 5000

while quitVar:
    screen.fill([0, 0, 0])

    for duck in ducks: duck.duckDraw(screen)

    sceneControl.cursorDraw(screen)
    sceneControl.terrainDraw(screen)

    if timer <= 0: ducks = []

    else:
        if timer % 23 == 0: ducks.append(duckControl.Duck())

        timer -= 1


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            
            for duck in duck:
                if position[0] >= duck.x - duck.direct*9 and position[0] <= duck.x + duck.direct*50:

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()