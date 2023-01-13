import pygame
pygame.init()

class attack():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 15
    def draw(self, root):
        pygame.draw.circle(root, self.color, (self.x, self.y), self.radius)

class enemy():
    def __init__(self, x, y, speed, width, height, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.color = color
    def draw(self, root):
        pygame.draw.rect(root, self.color, ((self.x, self.y), (self.width, self.height)))
