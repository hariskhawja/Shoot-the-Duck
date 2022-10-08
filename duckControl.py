import pygame
import random

# fly all over the screen in a randomized direction (changes direction (up, down, left, right) when hitting a wall)
# will leave the screen and get deleted if it exits from the top

'''
class Duck:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/duck.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 75))
        self.rect = self.image.get_rect()'''

class Duck:
    def __init__(self):
        self.x, self.y = random.randint(0, 500), random.randint(0, 400)
        self.xSpeed = self.ySpeed = random.randint(-10, 10)
        self.xPoint, self.yPoint = random.randint(0, 500), random.randint(0, 400)

        # self.directLock = True
        self.image = pygame.image.load("images/duck.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 75))
        self.rect = self.image.get_rect()
    
    '''def flipCheck(self, directLock):
        if not directLock:
            self.image = pygame.transform.flip(self.image, True, False)
            directLock = True'''

    def duckDraw(self):
        self.x += self.xSpeed
        self.y += self.ySpeed

        if self.x > 500 or self.x < 0:
            self.xSpeed *= -1
        
        if self.y > 400 or self.y < 0:
            self.ySpeed *= -1

        if self.x <= self.xPoint + 5 and self.x >= self.xPoint - 5:
            self.xSpeed = 0

        if self.y <= self.yPoint + 5 and self.y >= self.yPoint - 5:
            self.ySpeed = 0

        if self.xSpeed and self.ySpeed == 0:
            self.xSpeed = self.ySpeed = random.randint(-10, 10)