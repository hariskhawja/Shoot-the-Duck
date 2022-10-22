from xml.etree.ElementTree import PI
import pygame

class Duck:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Duckdraw(self, surface):
        pygame.draw.circle(surface, [255, 255, 255], (self.x, self.y), 9)
        '''pygame.draw.arc(surface, [255, 255, 255], (self.x - 50, self.y - 5, 50, 30), 3.14, 2 * 3.14)
        pygame.draw.line(surface, [255, 255, 255], (self.x - 50, self.y + 9), (self.x, self.y + 9))'''

        pygame.draw.ellipse(surface, [255, 255, 255], (self.x - 50, self.y + 4, 50, 35))

        pygame.draw.polygon(surface, [255, 255, 255], [(self.x - 15, self.y + 9), (self.x - 40, self.y + 35), (self.x - 35, self.y + 9)], width = 1)
        pygame.draw.polygon(surface, [255, 255, 255], [(self.x + 9, self.y - 2), (self.x + 9, self.y + 2), (self.x + 15, self.y)], width = 1)