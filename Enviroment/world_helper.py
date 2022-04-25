from csv import reader
from os import walk

import pygame

import settings


def importFolder(path):
    surface_list = []
    for _,__,image_file in walk(path):
        for image in image_file:
            full_path = path + '/'+ image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list


def import_csv_layout(file_path):
    terrain_map = []
    with open(file_path) as map:
        level = reader(map, delimiter=',')
        for row in level:
            terrain_map.append(list(row))
        return terrain_map


def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / settings.TILE_SIZE)
    tile_num_y = int(surface.get_size()[1] / settings.TILE_SIZE)

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * settings.TILE_SIZE
            y = row * settings.TILE_SIZE
            new_surf = pygame.Surface((settings.TILE_SIZE, settings.TILE_SIZE), flags=pygame.SRCALPHA)
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, settings.TILE_SIZE, settings.TILE_SIZE))
            cut_tiles.append(new_surf)

    return cut_tiles
