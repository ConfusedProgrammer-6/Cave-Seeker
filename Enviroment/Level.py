import pygame
from Enviroment import Tile
from settings import TILE_SIZE,WINDOW_WIDTH
from Player import Player


class Level:
    def __init__(self, level_data, surface):
        # setting up the level
        self.player = None
        self.tiles = None
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        # image = Tile.Tile()
        for row_index, row in enumerate(layout):
            for column_index, cell in enumerate(row):
                x = column_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if cell == 'X':
                    tile = Tile.Tile((x, y), TILE_SIZE)
                    self.tiles.add(tile)
                if cell == '-':
                    tile = Tile.Tile((x, y), TILE_SIZE)
                    tile.set_image_Color('blue')
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player.Player((x, y))
                    self.player.add(player_sprite)
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < WINDOW_WIDTH / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > WINDOW_WIDTH - (WINDOW_WIDTH / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8
    def run(self):
        #World generation
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # create player sprites
        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()