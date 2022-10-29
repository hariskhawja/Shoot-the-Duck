import pygame

class Duck:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

    def Duckdraw(self, surface):
        colour = []
        if (self.colour == "blue"): colour = [0, 0, 150]

        if (self.colour == "green"): colour = [0, 150, 0]

        if (self.colour == "red"): colour = [150, 0, 0]

        if (self.colour == "cyan"): colour = [0, 150, 150]

        if (self.colour == "purple"): colour = [150, 0, 150]

        if (self.colour == "yellow"): colour = [150, 150, 0]


        pygame.draw.circle(surface, colour, (self.x, self.y), 9)
        pygame.draw.ellipse(surface, colour, (self.x - 49, self.y, 50, 20))
        pygame.draw.polygon(surface, [200, 200, 200], [(self.x + 9, self.y - 2), (self.x + 9, self.y + 2), (self.x + 15, self.y)])
        pygame.draw.polygon(surface, [200, 200, 200], [(self.x - 10, self.y + 2), (self.x - 45, self.y + 25), (self.x - 50, self.y + 25), (self.x - 35, self.y + 2), (self.x - 30, self.y), (self.x - 15, self.y)])

