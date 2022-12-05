import pygame
from Source.settings import Settings


class TowerSprite:
    TOWERS = []

    def __init__(self, can_build=False, visibility=False, orig=False, x=0, y=0):
        self.can_build = can_build
        self.visibility = visibility
        self.rect = pygame.Rect(x, y, 70, 70)
        self.color = (0, 0, 255, 50)
        self.outline_green = (0, 255, 0)
        self.outline_red = (255, 0, 0)
        # orig is whether it would follow the cursor
        self.orig = orig

    def draw(self):
        if self.orig:  # check if it should follow the cursor
            pos = pygame.mouse.get_pos()
            self.rect.x, self.rect.y = pos[0], pos[1]

        if self.visibility:  # if visible
            pygame.draw.rect(surface=Settings.SCREEN, color=self.color, rect=self.rect)  # draw tower

            if self.can_build:  # making outline red/green
                pygame.draw.rect(surface=Settings.SCREEN, color=self.outline_green, rect=self.rect, width=10)
            else:
                pygame.draw.rect(surface=Settings.SCREEN, color=self.outline_red, rect=self.rect, width=10)

    def is_clicked(self):
        event = Settings.EVENT
        if event.type == pygame.MOUSEBUTTONUP:  # if clicked
            if self.orig and self.visibility:  # if it's the original, create new tower
                new_tower = TowerSprite(x=self.rect.x, y=self.rect.y, visibility=True)
                self.TOWERS.append(new_tower) # add new tower to towers
                return new_tower

    def logic(self):
        return self.is_clicked()

