import pygame
from Source.settings import Settings
import math


class MonsterBase:
    def __init__(self, path):
        self.rect = pygame.Rect(0.0, 637.0, 30.0, 30.0)
        self.color = pygame.Color("green")
        self.image = None
        self.path = path
        self.progress = 0
        self.destination = self.path[1]
        self.degrees = 0
        self.shift_x = 0
        self.shift_y = 0
        self.x = 0.0
        self.y = 637.0
        self.speed = 1

    def move(self):
        deltaX = self.destination[0] - self.rect.x
        deltaY = self.destination[1] - self.rect.y

        #print(f"Deltas: {deltaX}, {deltaY}")
        degrees = math.atan2(deltaX, deltaY)/math.pi*180

        #print(degrees)
        if degrees < 0:
            degrees = 360 + degrees

        self.degrees = degrees

        self.shift_x = math.cos(math.radians(int(90 - self.degrees))) * self.speed
        self.shift_y = math.sin(math.radians(int(90 - self.degrees))) * self.speed

        #print([self.shift_x, self.shift_y])
        self.x += self.shift_x
        self.y += self.shift_y

        self.rect.x = self.x
        self.rect.y = self.y

        if abs(self.destination[0] - self.x) < 5 and abs(self.destination[1] - self.y) < 5:
            if not self.progress == len(self.path) - 1:
                self.progress += 1
            self.destination = self.path[self.progress]






    def draw(self):
        pygame.draw.rect(surface=Settings.SCREEN, rect=self.rect, color=self.color)

    def logic(self):
        self.move()
