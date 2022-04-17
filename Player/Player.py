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
        # player movement
        self.speed = 8
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 1.5
        self.jump_speed = -16

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            assert self.direction.x < 0
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            assert self.direction.x > 0
        elif keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
            self.jump()
        else:
            self.direction.x = 0
            assert self.direction.x == 0
        # if keys[pygame.K_DOWN]:
        #     self.move_up()
        # if keys[pygame.K_UP]:
        #     self.move_down()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
