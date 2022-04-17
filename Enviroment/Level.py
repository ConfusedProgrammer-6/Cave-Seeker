import pygame
from Enviroment import Tile
from settings import TILE_SIZE


class Level:
    def __init__(self, level_data, surface):
        #setting up the level
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        #image = Tile.Tile()
        for row_index, row in enumerate(layout):
            for column_index, cell in enumerate(row):
                if cell == 'X':
                    x = column_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    tile = Tile.Tile((x, y), TILE_SIZE)
                    self.tiles.add(tile)
                if cell == '-':
                    x = column_index * TILE_SIZE
                    y = row_index * TILE_SIZE

                    tile = Tile.Tile((x, y), TILE_SIZE)
                    tile.set_image_Color('blue')
                    self.tiles.add(tile)

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
