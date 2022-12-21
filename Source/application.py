import pygame
from Source.Scenes.game import GameScene
from Source.settings import Settings
from Source.Scenes.menu import MenuScene

class Application:
    def __init__(self, screen):
        self.scenes = [MenuScene(), GameScene()]
        self.screen = screen
        self.game_over = False
        self.scene = self.scenes[Settings.SCENE]

    def process_frame(self):
        # wiping screen
        Settings.SCREEN.fill((0, 0, 0))
        # updating frame
        Settings.FRAME += 1
        # polling events
        Settings.EVENT = pygame.event.poll()

        # drawing scenes and processing logic
        logic = self.scene.logic()
        self.scene.draw()

        if logic == "nextscene":
            if Settings.SCENE == len(self.scenes) - 1:
                exit()
            else:
                Settings.SCENE += 1
                self.scene = self.scenes[Settings.SCENE]

        if logic == "highscores":
            # self.scene = self.scenes[2]
            Settings.SCENE = 2
            exit()

        if logic == "settingscene":
            # self.scene = self.scenes[3]
            Settings.SCENE = 3
            exit()

        # updating display
        pygame.display.flip()

    def start(self):
        # starting game
        while not self.game_over:
            self.process_frame()
