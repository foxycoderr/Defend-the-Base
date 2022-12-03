import pygame
from Source.Scenes.game import GameScene


class Application:
    def __init__(self, screen):
        self.scenes = [GameScene()]
        self.screen = screen
        self.game_over = False

    def process_frame(self):
        pygame.display.flip()
        for scene in self.scenes:
            scene.logic()
            scene.draw()

    def start(self):
        while not self.game_over:
            self.process_frame()