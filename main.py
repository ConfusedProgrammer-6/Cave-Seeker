import random
import sys

import pygame
from pygame import key
from pygame.sprite import Sprite, Group
from pygame.sprite import spritecollideany
from pygame.surface import Surface
from pygame.time import Clock

from Enviroment.Ground import Ground
from Player import Player as Player
from Player import Enemies
import settings


# settings class
# Player setup class
# Game Setup Class
# screen shake animation when player hits an enemy, particles fly out (think enter the gungeon)
# enemies


class Viewport:
    def __init__(self):
        self.left = 0

    def update(self, sprite):
        self.left = sprite.rect.left - 300

    def compute_rect(self, group):
        for sprite in group:
            sprite.rect = sprite.rect.move(-self.left, 0)


class Explosion(Sprite):
    # when creating a subclass, make sure you override the correct methods with the correct names
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = Surface((25, 25))
        self.image.fill((0, 0, 200))
        self.rect = self.image.get_rect().move(x, y)

    def update(self, *args, **kwargs):
        pass


class GameSetup:
    def __init__(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pygame.display.set_caption("Cave Seeker")
        self.player = Player.Player()  # create an instance of the player class
        self.player_group = Group()
        self.player_group.add(self.player)
        self.enemy = Group()  # Create a collection of bad guys
        self.static_sprites = Group()
        self.static_sprites.add(Ground())

        for i in range(10):
            self.enemy.add(Enemies.Enemy(random.randrange(0, settings.WORLD_WIDTH),
                                         random.randrange(0, settings.WINDOW_HEIGHT)))

    def mainLoop(self):
        clock = Clock()
        while True:
            self.handle_Events()
            self.draw()
            self.update()
            pygame.display.flip()
            clock.tick(60)

    def handle_Events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F3:
                    pass
                # elif event.key == pygame.K_LEFT:
                #     self.player.move_left()
                # elif event.key == pygame.K_RIGHT:
                #     self.player.move_right()

    def update(self):
        self.player_group.update(key.get_pressed())
        self.enemy.update()
        # self.viewport.update(self.player)
        self.check_collisions()

    def check_collisions(self):
        if self.player.alive() and (collided_with := spritecollideany(self.player, self.enemy)) is not None:
            self.player.kill()
            collided_with.kill()
            self.player_group.add(Explosion(self.player.rect.left, self.player.rect.top))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.static_sprites.draw(self.screen)
        self.player_group.draw(self.screen)
        self.enemy.draw(self.screen)


if __name__ == '__main__':
    GameSetup().mainLoop()
