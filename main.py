import pygame
import duckControl

pygame.init()
pygame.display.set_caption("Shoot the Duck")
screen = pygame.display.set_mode(800, 800)

FPS = 60
fpsClock = pygame.time.Clock()

quitVar = True

while quitVar:
    screen.fill([255, 255, 255])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()