WINDOW_WIDTH = 1920
#Collect all totems to open up gate and advance to next leve
# O = Totem
# X = Dirt Tile
# - = Grass Tile
# P = Player
# E = Enemy
# [] = End Gate
LEVEL_1_MAP = [
    '                                        --0--                      ',
    ' P     O                          XXXX              0               ',
    '--   ---                                         -----             ',
    '              -0-             ----      0                          ',
    '  -                  ---    XXXX     XXXX                        ',
    '           ---                              XXXXX            0     ',
    '    ---         ------                                     XXXX    ',
    '              --X                     0              0             ',
    '            -XXX    0               ---          ---------      []',
    '-------------XXXX----------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
]
TILE_SIZE = 64
WINDOW_HEIGHT = TILE_SIZE * len(LEVEL_1_MAP)
WORLD_WIDTH = 4 * WINDOW_WIDTH
