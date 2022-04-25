from random import randint

import pygame.transform

from Enviroment.Tile import AnimatedTile


class Enemy(AnimatedTile):

    def __init__(self, size, x, y):
        super().__init__(size, x, y, 'Assets/Animations/Character Animations/Enemy_chars/crab-walk')
        self.speed = randint(1, 3)

    def move(self):
        self.rect.x += self.speed

    def reverseImage(self):
        self.speed > 0
        self.image = pygame.transform.flip(self.image, True, False)

    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverseImage()

    def set_speed(self, speed):
        self.speed *= speed

    def reverse(self):
        self.speed *= -1


class Jumper(AnimatedTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, 'Assets/Animations/Character Animations/Enemy_chars/jumper-idle')
        self.speed = randint(3, 5)

    def move(self):
        self.rect.y += (self.speed * 1.2) / 2

    def reverseImage(self):
        self.speed > 0
        self.image = pygame.transform.flip(self.image, True, False)

    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverseImage()

    def set_speed(self, speed):
        self.speed *= speed

    def reverse(self):
        self.speed *= -1


class Chungus(AnimatedTile):

    def __init__(self, size, x, y):
        super().__init__(size, x, y, 'Assets/Animations/Character Animations/Enemy_chars/octopus')
        self.speed = randint(2, 3)

    def move(self):
        self.rect.x += self.speed

    def reverseImage(self):
        self.speed > 0
        self.image = pygame.transform.flip(self.image, True, False)

    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverseImage()

    def set_speed(self, speed):
        self.speed *= speed

    def reverse(self):
        self.speed *= -1
