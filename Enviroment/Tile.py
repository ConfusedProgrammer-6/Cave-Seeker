import pygame
from pygame.sprite import Sprite

from Enviroment.world_helper import importFolder


class Tile(Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.image.fill('grey')

    def set_image_Color(self, color):
        self.image.fill(color)

    def update(self, x_shift ):

        self.rect.x += x_shift


class AnimatedTile(Tile):
    def __init__(self, size, x, y, path):
        super().__init__(size, x, y)
        self.frames = importFolder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self):
        self.frame_index += .15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
        self.image = pygame.transform.scale(self.image, (75, 75))

    def update(self, shift):
        self.animate()
        self.rect.x += shift

