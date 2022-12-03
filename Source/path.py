import pygame

class Path:
    def __init__(self):
        self.image = pygame.image.load("Assets\\Images\\Path.png")
        self.x = 0
        self.y = 0

    def draw(self, screen):
        screen.blit(self.image, [0, 0])

