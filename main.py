# DEFEND THE BASE
# Welcome to DtB, an open-source tower defence game.

# The updated version of the project is kept at https://github.com/foxycoderr/Defend-the-Base.
# All credit for the code goes to the DtB team.
# We kindly ask you not to remove or modify this notice if you republish this project elsewhere.


import pygame
from Source.application import Application
from Source.settings import Settings

# creating screen
screen = pygame.display.set_mode([1800, 900])
# writing screen into settings
Settings.SCREEN = screen

# running application
application = Application(screen)
application.start()
