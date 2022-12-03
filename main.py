import pygame
from Source.application import Application

screen = pygame.display.set_mode([1800, 900])

application = Application(screen)
application.start()