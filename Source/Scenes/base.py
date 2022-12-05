import pygame
from Source.settings import Settings
class BaseScene:
    def __init__(self):
        # creating objects list
        self.objects = []

    def check_close(self):
        # checking if the game is closed
        event = Settings.EVENT
        if event.type == pygame.QUIT:
            exit()

    def logic(self):
        self.check_close()
        # running all the objects' logic
        for object in self.objects:
            object.logic()

    def draw(self):
        # drawing all the objects
        for object in self.objects:
            object.draw()