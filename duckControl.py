import pygame
import colours
import random

class Duck:
    def __init__(self):
        self.direct = 1 if random.randint(0, 1) == 0 else -1
        self.x = random.randint(-200,-50) if self.direct == 1 else random.randint(1250, 1400)
        self.y = random.randint(50, 400)
        self.colour = random.choice(colours.colourList)

    def duckDraw(self, surface):
        d = self.direct
        pygame.draw.circle(surface, colours.colourType(self.colour), (self.x, self.y), 9)

        if d == 1: pygame.draw.ellipse(surface, colours.colourType(self.colour), (self.x - 49, self.y, 50, 20))

        else: pygame.draw.ellipse(surface, colours.colourType(self.colour), (self.x, self.y, 50, 20))

        pygame.draw.polygon(surface, [200, 200, 200], [(self.x + 9*d, self.y - 2), (self.x + 9*d, self.y + 2), (self.x + 15*d, self.y)])
        pygame.draw.polygon(surface, [200, 200, 200], [(self.x - 10*d, self.y + 2), (self.x - 45*d, self.y + 25), (self.x - 50*d, self.y + 25), (self.x - 35*d, self.y + 2), (self.x - 30*d, self.y), (self.x - 15*d, self.y)])
 
        self.x += colours.colourPoints(self.colour)*d
        self.y -= 0.25