import random
import sys

import pygame
from pygame.sprite import Sprite, Group
from pygame.surface import Surface

class Explosion(Sprite):
    #when creating a subclass, make sure you override the correct methods with the correct names
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Surface((25, 25))
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect().move(0, 300)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.left += 1


class Player(Sprite):
    #when creating a subclass, make sure you override the correct methods with the correct names
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Surface((25, 25))
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect().move(0, 300)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.left += 1


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


def handle_Events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)


class GameSetup:
    def __init__(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption("Cave Seeker")
        self.player = Player() # create an instance of the player class
        self.player_group = Group()
        self.player_group.add(self.player)
        self.enemy = Group() # Create a collection of bad guys

        for i in range(15):
            self.enemy.add(Enemy(random.randrange(0, 1024), random.randrange(0, 768))) # add enemies to the bad guy collection, 15 of them.

    def mainLoop(self):
        while True:
            handle_Events()
            self.draw()
            self.update()
            pygame.display.flip()

    def update(self):
        self.player_group.update()
        self.enemy.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player_group.draw(self.screen)
        self.enemy.draw(self.screen)


if __name__ == '__main__':
    GameSetup().mainLoop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
