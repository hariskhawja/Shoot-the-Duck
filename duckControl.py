import pygame
import colours
import random
from mathFunctions import gcf

class Duck:
    def __init__(self, colour):
        self.x = random.randint(50, 1150)
        self.y = random.randint(50, 400)
        self.xDirec = random.randint(0, 1150)
        self.yDirec = random.randint(0, 400)
        self.xInc = 1
        self.yInc = 1
        self.colour = colours.colourType(colour)

    def duckDraw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.x, self.y), 9)
        pygame.draw.ellipse(surface, self.colour, (self.x - 49, self.y, 50, 20))
        pygame.draw.polygon(surface, [200, 200, 200], [(self.x + 9, self.y - 2), (self.x + 9, self.y + 2), (self.x + 15, self.y)])
        pygame.draw.polygon(surface, [200, 200, 200], [(self.x - 10, self.y + 2), (self.x - 45, self.y + 25), (self.x - 50, self.y + 25), (self.x - 35, self.y + 2), (self.x - 30, self.y), (self.x - 15, self.y)])

        '''
        rise = self.yDirec - self.y
        run = self.xDirec - self.x

        rise /= (gcf(abs(run), abs(rise)) if gcf(abs(run), abs(rise)) != 0 else 1)
        run /= (gcf(abs(run), abs(rise)) if gcf(abs(run), abs(rise)) != 0 else 1)

        self.x += run
        self.y += rise
        '''

        if self.x - self.xDirec < 0: self.xInc = 1

        else: self.xInc = -1

        if self.y - self.yDirec < 0: self.yInc = 1

        else: self.yInc = -1

        print(self.colour)
        print(colours.colourPoints(self.colour))


        tester = colours.colourPoints(self.colour)
        print(tester)


        self.x += self.xInc * tester
        self.y += self.yInc * tester

        if self.x < self.xDirec + 10 and self.x > self.xDirec - 10: random.randint(0, 1150)
        if self.y < self.yDirec + 10 and self.y > self.yDirec - 10: random.randint(0, 400)