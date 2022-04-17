import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface


class Player(Sprite):
    # when creating a subclass, make sure you override the correct methods with the correct names
    def __init__(self, pos):
        super().__init__()
        self.image = Surface((32, 64))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 8
        self.direction = pygame.math.Vector2(0, 0)

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            assert self.direction.x < 0
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            assert self.direction.x > 0
        else:
            self.direction.x = 0
            assert self.direction.x == 0
        # if keys[pygame.K_DOWN]:
        #     self.move_up()
        # if keys[pygame.K_UP]:
        #     self.move_down()

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed

    # def move_left(self):
    #     self.rect.left -= 10
    #
    # def move_right(self):
    #     self.rect.right += 10
    #
    # def move_up(self):
    #     self.rect.top += 10
    #
    # def move_down(self):
    #     self.rect.bottom -= 10
