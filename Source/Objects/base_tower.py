import pygame
from Source.settings import Settings


class Tower:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 70, 70)
        self.color = (0, 255, 255, 100)

    def draw(self):
        pygame.draw.rect(surface=Settings.SCREEN, color=self.color, rect=self.rect)  # draw tower


    def logic(self):
        return 0

