import pygame
import colours

class Duck:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colours.colourTypes[colour]

    def Duckdraw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.x, self.y), 9)
        pygame.draw.ellipse(surface, self.colour, (self.x - 49, self.y, 50, 20))
        pygame.draw.polygon(surface, [200, 200, 200], [(self.x + 9, self.y - 2), (self.x + 9, self.y + 2), (self.x + 15, self.y)])
        pygame.draw.polygon(surface, [200, 200, 200], [(self.x - 10, self.y + 2), (self.x - 45, self.y + 25), (self.x - 50, self.y + 25), (self.x - 35, self.y + 2), (self.x - 30, self.y), (self.x - 15, self.y)])