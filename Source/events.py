import pygame

class EventHandler:
    def __init__(self):
        self.event = pygame.event.poll

    def check_for_closing(self):
        if self.event.type == pygame.QUIT:
            exit()

    def process_logic(self):
        self.event = pygame.event.poll()
        self.check_for_closing()