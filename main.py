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

blueDuck = duckControl.Duck("blue")
greenDuck = duckControl.Duck("green")
redDuck = duckControl.Duck("red")
cyanDuck = duckControl.Duck("cyan")
purpleDuck = duckControl.Duck("purple")
yellowDuck = duckControl.Duck("yellow")

while quitVar:
    screen.fill([0, 0, 0])

    blueDuck.duckDraw(screen)
    greenDuck.duckDraw(screen)
    redDuck.duckDraw(screen)
    cyanDuck.duckDraw(screen)
    purpleDuck.duckDraw(screen)
    yellowDuck.duckDraw(screen)

    sceneControl.cursorDraw(screen)
    sceneControl.terrainDraw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()