import pygame
import colours
import random
from mathFunctions import gcf

class Duck:
    def __init__(self, colour):
        self.x = random.randint(-200,-50)
        self.y = random.randint(50, 400)
        self.colour = colours.colourType(colour)

    def duckDraw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.x, self.y), 9)
        pygame.draw.ellipse(surface, self.colour, (self.x - 49, self.y, 50, 20))
        pygame.draw.polygon(surface, [200, 200, 200], [(self.x + 9, self.y - 2), (self.x + 9, self.y + 2), (self.x + 15, self.y)])
        pygame.draw.polygon(surface, [200, 200, 200], [(self.x - 10, self.y + 2), (self.x - 45, self.y + 25), (self.x - 50, self.y + 25), (self.x - 35, self.y + 2), (self.x - 30, self.y), (self.x - 15, self.y)])

        self.x += 2
        self.y -= 0.5