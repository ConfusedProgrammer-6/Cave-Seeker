import random

from pygame.sprite import Sprite
from pygame.surface import Surface


class Enemy(Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = Surface((25, 25))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect().move(x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.move_ip(random.randint(-10, 10), random.randint(-10, 10))
