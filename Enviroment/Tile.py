import pygame
from pygame.sprite import Sprite

import settings


class Tile(Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        # self.rect.bottom = settings.WINDOW_HEIGHT
        # assert self.rect.width == settings.WORLD_WIDTH

    def set_image_Color(self, color):
        self.image.fill(color)

    def update(self, x_shift):
        self.rect.x += x_shift
