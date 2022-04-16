import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface


class Player(Sprite):
    # when creating a subclass, make sure you override the correct methods with the correct names
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Surface((25, 25))
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect().move(0, 300)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_DOWN]:
            self.move_up()
        if keys[pygame.K_UP]:
            self.move_down()

    def move_left(self):
        self.rect.left -= 10

    def move_right(self):
        self.rect.right += 10

    def move_up(self):
        self.rect.top += 10

    def move_down(self):
        self.rect.bottom -= 10
