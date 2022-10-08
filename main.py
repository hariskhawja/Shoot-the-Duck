import pygame
import duckControl

pygame.init()
pygame.display.set_caption("Shoot the Duck")
screen = pygame.display.set_mode((500, 500))

FPS = 60
fpsClock = pygame.time.Clock()

quitVar = True

testDuck = duckControl.Duck()

floor = pygame.transform.scale(pygame.image.load("images/grass.png").convert_alpha(), (500, 400))

while quitVar:
    screen.fill([100, 255, 255])

    screen.blit(floor, (0, 150))
    testDuck.rect.center = (testDuck.x, testDuck.y)
    screen.blit(testDuck.image, testDuck.rect)

    testDuck.duckDraw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()