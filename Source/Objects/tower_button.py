import pygame
from Source.settings import Settings
from Source.BaseClasses.buttons import Button

class TowerButton(Button):
    TOWERS = []

    def __init__(self):
        super().__init__(font="Candara", height=280, width=140, text="Build tower!", x=250, y=750, text_size=50, text_color=(255,255,255), bg_color=(0,255,0), hover_color=(0,255,0,50), outline=True, outline_color=(255,255,255), outline_width=2)

    def logic(self):
        return super().logic()