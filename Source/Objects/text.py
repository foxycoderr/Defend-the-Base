import pygame
from Source.settings import Settings


class Text:
    def __init__(self, text, font, size, color, x, y):
        pygame.font.init()
        self.text = text
        self.size = size
        self.font = self.font = pygame.font.SysFont(font, self.size, True, False)
        self.x = x
        self.y = y
        self.color = color
        self.texture = self.font.render(self.text, True, self.color)
        self.rect = pygame.Rect(self.x, self.y, self.texture.get_width(), self.texture.get_height())

    def draw(self):
        Settings.SCREEN.blit(self.texture, self.rect)

    def logic(self):
        pass
