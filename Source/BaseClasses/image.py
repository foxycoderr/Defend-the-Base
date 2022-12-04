import pygame
from Source.settings import Settings

class Image:
    def __init__(self, filename, x, y, resize=100):
        self.filename = filename
        self.x = x
        self.y = y
        self.resize = resize
        self.image = pygame.image.load(self.filename)
        self.resized_coords = [self.image.get_width()*self.resize/100, self.image.get_height()*self.resize/100]
        self.image = pygame.transform.scale(self.image, self.resized_coords)

    def draw(self):
        Settings.SCREEN.blit(self.image, [self.x, self.y])

    def logic(self):
        pass
