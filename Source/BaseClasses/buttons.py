import pygame
from Source.BaseClasses.text import Text
from Source.settings import Settings



class Button:
    def __init__(self, x, y, width, height, font, text_color, text_size, text, bg_color=None, hover_color=None, outline=None, outline_color=(0,0,0), outline_width=5):
        self.text = Text(color=text_color, font=font, size=text_size, text=text, x=0, y=0)
        self.bodytype = 0
        self.outline_width = outline_width
        self.bg_color = bg_color
        self.outline = outline
        self.outline_color = outline_color

        # creating of body attributes, which contain the button's body (rect and color)
        if bg_color:
            self.body = [pygame.Rect(x, y, height, width), bg_color]
            self.bodytype = 1
        else:
            self.body = [pygame.Rect(x, y, height, width), None]

        # updating text position to center it in the body
        self.text.rect.x = (self.body[0].width - self.text.texture.get_width()) / 2 + x
        self.text.rect.y = (self.body[0].height - self.text.texture.get_height()) / 2 + y

        self.hover_color = hover_color

    def draw(self):
        # checking if there is a body
        if self.bodytype == 1:
            pygame.draw.rect(surface=Settings.SCREEN, color=self.body[1], rect=self.body[0])
            if self.outline:
                pygame.draw.rect(surface=Settings.SCREEN, color=self.outline_color, rect=self.body[0], width=self.outline_width)
        self.text.draw()


    def on_hover(self):
        pos = pygame.mouse.get_pos()
        # checking whether the mouse is in the button, changing color to hover_color
        if self.body[0].collidepoint(pos) and self.hover_color:
            self.body[1] = self.hover_color
            return 1

        else:
            self.body[1] = self.bg_color
            return 0

    def on_click(self):
        # checking if the button is clicked
        event = Settings.EVENT
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if self.body[0].collidepoint(pos):
                return True

    def logic(self):
        self.on_hover()
        return self.on_click()
