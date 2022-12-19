import pygame
from Source.BaseClasses.buttons import Button

class HighscoreButton(Button):
    def __init__(self, x, y, width, height, font, text_color, text_size, text, bg_color=None, hover_color=None, outline=None, outline_color=(0, 0, 0), outline_width=5):
        super().__init__(x, y, width, height, font, text_color, text_size, text, bg_color, hover_color, outline, outline_color, outline_width)

    def logic(self):
        self.on_hover()
        if self.on_click():
            return "highscores"