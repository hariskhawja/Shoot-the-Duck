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

blueDuck = duckControl.Duck(250, 250, "blue")
greenDuck = duckControl.Duck(350, 250, "green")
redDuck = duckControl.Duck(450, 250, "red")
cyanDuck = duckControl.Duck(550, 250, "cyan")
purpleDuck = duckControl.Duck(650, 250, "purple")
yellowDuck = duckControl.Duck(750, 250, "yellow")

while quitVar:
    screen.fill([0, 0, 0])

    blueDuck.Duckdraw(screen)
    greenDuck.Duckdraw(screen)
    redDuck.Duckdraw(screen)
    cyanDuck.Duckdraw(screen)
    purpleDuck.Duckdraw(screen)
    yellowDuck.Duckdraw(screen)

    sceneControl.cursorDraw(screen)
    sceneControl.staticSceneDraw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()