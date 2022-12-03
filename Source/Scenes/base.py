import pygame

class BaseScene:
    def __init__(self):
        self.objects = []

    def check_close(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            exit()

    def logic(self):
        self.check_close()
        for object in self.objects:
            object.logic()

    def draw(self):
        for object in self.objects:
            object.draw()