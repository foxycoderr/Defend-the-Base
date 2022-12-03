import pygame
from Source.application import Application
from Source.settings import Settings

screen = pygame.display.set_mode([1800, 900])
Settings.SCREEN = screen

application = Application(screen)
application.start()