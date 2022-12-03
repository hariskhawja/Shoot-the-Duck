import pygame
import duckControl
import sceneControl
# import generationControl
# from generationControl import ducks

pygame.init()
pygame.display.set_caption("Shoot the Duck")
screen = pygame.display.set_mode((1200, 500))

pygame.mouse.set_visible(False)

FPS = 120
fpsClock = pygame.time.Clock()

quitVar = True

ducks = []

timer = 5000
score = 0

while quitVar:
    screen.fill([0, 0, 0])

    for duck in ducks:
        if duck.direct == 1 and duck.x > 1300: ducks.remove(duck)

        elif duck.direct == -1 and duck.x < -100: ducks.remove(duck)
        
        else: duck.duckDraw(screen)

    sceneControl.cursorDraw(screen)
    sceneControl.terrainDraw(screen)

    if not timer <= 0: 
        if timer % 23 == 0: ducks.append(duckControl.Duck())
        timer -= 1

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            
            for duck in ducks:
                if duck.direct == -1:
                    if (position[0] >= duck.x - 9 and position[0] <= duck.x + 50) and (position[1] <= duck.y + 25 and position[1] >= duck.y - 9):
                        ducks.remove(duck)
                        score += 1

                else:
                    if (position[0] <= duck.x + 9 and position[0] >= duck.x - 50) and (position[1] <= duck.y + 25 and position[1] >= duck.y - 9):
                        ducks.remove(duck)
                        score += 1

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()