import sys

import pygame
from pygame.time import Clock

import settings
from Enviroment import Level
from Enviroment import world_data
from Player import Player as Player


# TODO Player setup class
# TODO Game Setup Class
# TODO screen shake animation when player hits an enemy, particles fly out (think enter the gungeon)

class win():
    print("congrats!")

class GameSetup:
    def __init__(self):
        pygame.display.init()
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        self.background_image = pygame.image.load('Assets/Enviroment/layers/background.png').convert()
        self.current_level = 1
        pygame.display.set_caption("Cave Seeker")

        self.background_image = pygame.transform.scale(self.background_image,
                                                       (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

        self.level = Level.Level(world_data, self.screen)
        self.level_2 = Level.Level2(world_data,self.screen)

        self.player = Player.Player((255,255), self.screen)


    def mainLoop(self, level):
        clock = Clock()
        if level == 1:
            while True:
                self.screen.blit(self.background_image, (0, 0))
                self.handle_Events()
                self.level.update()
                self.player.update()

                pygame.display.update()
                clock.tick(60)
        if level == 2:
            print("welcome to level 2!")
            while True:
                self.screen.blit(self.background_image, (0, 0))
                self.handle_Events()
                self.level_2.draw()
                self.player.update()

                pygame.display.update()
                clock.tick(60)

    def handle_Events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    GameSetup().mainLoop(self.current_level)
                if event.key == pygame.K_F1:
                    self.current_level = 2
                    GameSetup().mainLoop(self.current_level)

if __name__ == '__main__':
    GameSetup().mainLoop(1)


