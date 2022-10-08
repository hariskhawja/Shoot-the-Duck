import pygame

def cursorDraw(surface):
    posX, posY = pygame.mouse.get_pos()

    pygame.draw.circle(surface, [255, 255, 255], (posX, posY), 5, width = 1)
    pygame.draw.circle(surface, [255, 255, 255], (posX, posY), 10, width = 1)
    pygame.draw.rect(surface, [255, 255, 255], (posX + 3, posY, 12, 1))
    pygame.draw.rect(surface, [255, 255, 255], (posX - 15, posY, 12, 1))
    pygame.draw.rect(surface, [255, 255, 255], (posX, posY - 15, 1, 12))
    pygame.draw.rect(surface, [255, 255, 255], (posX, posY + 3, 1, 12))

def staticSceneDraw(surface):
    pygame.draw.rect(surface, [255, 255, 255], (0, 375, 200, 1))
    pygame.draw.rect(surface, [255, 255, 255], (190, 385, 200, 1))
    pygame.draw.rect(surface, [255, 255, 255], (380, 410, 100, 1))