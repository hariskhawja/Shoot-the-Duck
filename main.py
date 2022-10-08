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

while quitVar:
    screen.fill([0, 0, 0])

    '''cursor.cursorDraw(screen)
    print(cursor.x)
    print(cursor.y)'''

    sceneControl.cursorDraw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()