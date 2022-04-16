import pygame
from pygame.sprite import Sprite

import settings


class Ground(Sprite):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = pygame.image.load("Assets/Images/background.png")
        self.rect = self.image.get_rect().copy()
        self.rect.bottom = settings.WINDOW_HEIGHT
        assert self.rect.width == settings.WORLD_WIDTH
