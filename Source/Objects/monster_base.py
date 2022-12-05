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
        # get deltas
        deltaX = self.destination[0] - self.rect.x
        deltaY = self.destination[1] - self.rect.y

        # get angle of movement using arctan
        degrees = math.atan2(deltaX, deltaY)/math.pi*180

        # checking if angle is negative
        if degrees < 0:
            degrees = 360 + degrees

        self.degrees = degrees

        # setting shifts to move by the angle
        self.shift_x = math.cos(math.radians(int(90 - self.degrees))) * self.speed
        self.shift_y = math.sin(math.radians(int(90 - self.degrees))) * self.speed

        # moving
        self.x += self.shift_x
        self.y += self.shift_y

        # changing rect attributes
        self.rect.x = self.x
        self.rect.y = self.y

        # checking if arrived at destination
        if abs(self.destination[0] - self.x) < 5 and abs(self.destination[1] - self.y) < 5:
            if not self.progress == len(self.path) - 1:  # increasing progress in case the end was not reached
                self.progress += 1
            self.destination = self.path[self.progress]  # choosing new destination






    def draw(self):
        # draws monster on the screen
        pygame.draw.rect(surface=Settings.SCREEN, rect=self.rect, color=self.color)

    def logic(self):
        self.move()
