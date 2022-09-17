import pygame

class Duck:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/duck.png")