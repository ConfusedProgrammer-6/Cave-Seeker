from os import walk

import pygame

WINDOW_WIDTH = 1920
VERTICAL_TILE_NUMBER = 15
TILE_SIZE = 16
WINDOW_HEIGHT = 800
BLACK = (0, 0, 0, 0)
LAVENDER = (129, 81, 107)
WIST = (188, 167, 232)

def import_folder(current_path):
    surface_list = []

    for _, __, image_names in walk(current_path):
        for image in image_names:

            full_path = current_path + '/' + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            image_surface = pygame.transform.scale(image_surface, (128, 128))
            image_rect = image_surface.get_bounding_rect(min_alpha=5)
            surface_list.append(image_surface)
    return surface_list
