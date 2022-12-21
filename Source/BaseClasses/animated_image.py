import pygame
from Source.settings import Settings
import datetime

# displays an animated image that updates by the FPS given
class AnimatedImage:
    def __init__(self, directory, x, y, frame_number, fps):
        # base attributes
        self.directory = directory
        self.frame_number = frame_number
        self.fps = fps
        self.x = x
        self.y = y

        # rect is not used, only to avoid issues with other objects and collisions
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

        # all frames the animation uses
        self.frames = []

        # loading frames
        for image_index in range(frame_number):
            image = pygame.image.load(f"{self.directory}/{image_index}.png")
            self.frames.append(image)

        # currently displayed frame and its index
        self.current_frame = self.frames[0]
        self.current_frame_index = 0

        # FPS (previous frame time, wait time between image updates)
        self.prev = datetime.datetime.now()
        self.wait_time = 1000000/fps

    def logic(self):
        # getting the updated time and calculating delta between previous and current check
        now = datetime.datetime.now()
        delta = now - self.prev

        # checking if delta is more than the least permitted time between image updates
        if delta.microseconds > self.wait_time:
            # resetting the prev
            self.prev = datetime.datetime.now()

            # updating frame index
            if self.current_frame_index + 1 == self.frame_number:
                self.current_frame_index = 0
            else:
                self.current_frame_index += 1

        # updating frame image
        self.current_frame = self.frames[self.current_frame_index]

    def draw(self):
        # drawing image onto screen
        screen = Settings.SCREEN
        screen.blit(self.current_frame, [self.x, self.y])
