import pygame
from Source.Objects.text import Text
from Source.settings import Settings



class Button:
    def __init__(self, x, y, width, height, font, text_color, text_size, text, bg_color=None, hover_color=None):
        self.text = Text(color=text_color, font=font, size=text_size, text=text, x=0, y=0)
        self.bodytype = 0
        self.bg_color = bg_color

        if bg_color:
            self.body = [pygame.Rect(x, y, width, height), bg_color]
            self.bodytype = 1
        else:
            self.body = [pygame.Rect(x, y, width, height), None]

        self.text.rect.x = (self.body[0].width - self.text.texture.get_width()) / 2 + x
        self.text.rect.y = (self.body[0].height - self.text.texture.get_height()) / 2 + y

        self.hover_color = hover_color

    def draw(self):
        if self.bodytype == 1:
            pygame.draw.rect(surface=Settings.SCREEN, color=self.body[1], rect=self.body[0])

        self.text.draw()

    def on_hover(self):
        pos = pygame.mouse.get_pos()
        if self.body[0].collidepoint(pos) and self.hover_color:
            self.body[1] = self.hover_color
            return 1

        else:
            self.body[1] = self.bg_color
            return 0

    def on_click(self):
        pass

    def logic(self):
        self.on_hover()
        self.on_click()
