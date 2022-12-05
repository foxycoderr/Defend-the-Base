import pygame
from Source.settings import Settings
from Source.BaseClasses.text import Text

class Castle:
    def __init__(self):
        self.hp = 100
        self.rect = pygame.Rect(1740, 463, 120, 120)
        self.color = (255, 0, 0)
        self.hp_text = Text(text=f"HP: {self.hp}", color=(255, 255, 255), font="Candara", x=1730, y=10, size=20)

    def draw(self):
        # drawing the castle and the HP counter
        pygame.draw.rect(surface=Settings.SCREEN, rect=self.rect, color=self.color)
        self.hp_text.draw()


    def reduce_hp(self, amount):
        # reduces HP, exits program when it's below zero
        self.hp -= amount
        if self.hp <= 0:
            exit()
        self.hp_text.text = f"HP: {self.hp}"

    def logic(self):
        pass

