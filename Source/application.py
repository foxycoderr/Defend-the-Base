import pygame
from Source.grid import Grid
from Source.events import EventHandler
from Source.path import Path


class Application:
    def __init__(self, screen):
        self.objects = []
        self.screen = screen
        self.game_over = False
        self.event_handler = EventHandler()

        self.grid = Grid()
        self.path = Path()

        self.objects.append(self.grid)
        self.objects.append(self.path)


    def display(self):
        for obj in self.objects:
            obj.draw(self.screen)

        pygame.display.flip()

    def start(self):
        while not self.game_over:
            self.display()
            self.event_handler.process_logic()