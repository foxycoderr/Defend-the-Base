import pygame
from Source.Scenes.game import GameScene
from Source.settings import Settings


class Application:
    def __init__(self, screen):
        self.scenes = [GameScene()]
        self.screen = screen
        self.game_over = False

    def process_frame(self):
        # wiping screen
        Settings.SCREEN.fill((0, 0, 0))
        # updating frame
        Settings.FRAME += 1
        # polling events
        Settings.EVENT = pygame.event.poll()

        # drawing scenes and processing logic
        for scene in self.scenes:
            scene.logic()
            scene.draw()

        # updating display
        pygame.display.flip()

    def start(self):
        # starting game
        while not self.game_over:
            self.process_frame()
