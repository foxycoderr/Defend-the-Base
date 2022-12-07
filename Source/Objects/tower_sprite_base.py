import pygame
from Source.settings import Settings


class TowerSprite:
    TOWERS = []

    def __init__(self, can_build=False, visibility=False):
        self.can_build = can_build
        self.visibility = visibility
        self.rect = pygame.Rect(0, 0, 70, 70)
        self.color = (0, 0, 255, 50)
        self.outline_green = (0, 255, 0)
        self.outline_red = (255, 0, 0)

    def draw(self):
        pos = pygame.mouse.get_pos()
        self.rect.x, self.rect.y = pos[0], pos[1]  # make the sprite follow the cursor

        if self.visibility:  # if visible
            pygame.draw.rect(surface=Settings.SCREEN, color=self.color, rect=self.rect)  # draw tower

            if self.can_build:  # making outline red/green
                pygame.draw.rect(surface=Settings.SCREEN, color=self.outline_green, rect=self.rect, width=10)
            else:
                pygame.draw.rect(surface=Settings.SCREEN, color=self.outline_red, rect=self.rect, width=10)

    def is_clicked(self):
        event = Settings.EVENT
        if event.type == pygame.MOUSEBUTTONUP:  # if clicked
            if self.visibility:  # if it's the original, create new tower
                new_tower = "New tower class goes here"
                self.TOWERS.append(new_tower)  # add new tower to towers
                return new_tower

    def logic(self):
        return self.is_clicked()

