import pygame
from Source.Scenes.game import GameScene
from Source.settings import Settings

import time

class Application:
    def __init__(self, screen):
        self.scenes = [GameScene()]
        self.screen = screen
        self.game_over = False

    def process_frame(self):

        Settings.SCREEN.fill((0, 0, 0))
        for scene in self.scenes:
            scene.logic()
            scene.draw()

        pygame.display.flip()


        #time.sleep(0.1)

    def start(self):
        while not self.game_over:
            self.process_frame()