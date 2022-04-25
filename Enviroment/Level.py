import sys

import pygame

import settings
from Enemies import En
from Enviroment import Tile, world_helper, StaticTiles
from Player import Player


class Level:
    def __init__(self, level_data, display_surface):

        # setting up the level
        self.world_shift = 0
        self.world_shift_y = 0
        self.display_surface = display_surface

        self.background_image = pygame.image.load('Assets/Enviroment/layers/middleground.png').convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image,
                                                       (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

        # importing Level Data
        terrain_layout = world_helper.import_csv_layout(level_data.level_1['Terrain'])
        background_layout = world_helper.import_csv_layout(level_data.level_1['Background'])

        death_layout = world_helper.import_csv_layout(level_data.level_1['Kill_tiles'])
        # creating player
        player_layout = world_helper.import_csv_layout(level_data.level_1['Player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

        # Creating tile groups

        self.terrain_sprites = self.create_tile_group(terrain_layout, 'Terrain')
        self.background_sprites = self.create_tile_group(background_layout, 'Background')
        self.death_sprites = self.create_tile_group(death_layout, 'Kill_tiles')

        # Enemies
        enemy_layout = world_helper.import_csv_layout(level_data.level_1['Enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout, 'Enemies')

        # constraints
        constraint_layout = world_helper.import_csv_layout(level_data.level_1['Constraints'])
        self.constraint_sprites = self.create_tile_group(constraint_layout, "Constraints")

    def draw_background(self):
        self.display_surface.blit(self.background_image, (0, 0))

        self.instructions()

    def instructions(self):
        # Instructions
        welcome_font = pygame.font.Font('freesansbold.ttf', 36)
        font = pygame.font.Font('freesansbold.ttf', 24)

        text = welcome_font.render('Welcome To The Cave!', True, settings.LAVENDER, settings.WIST)
        subText = font.render("The rules are simple: Use the arrow keys to move. Space to jump.", True,
                              settings.WIST, settings.LAVENDER)
        newlineText = font.render("Time your jumps by holding space, Press ESC to restart instantly, F1 for level 2",
                                  True,
                                  settings.WIST, settings.LAVENDER)
        lastLineText = font.render("Dont touch the ceiling. Dont fall. Ram the bugs and reach the end, Catch Chungus!",
                                   True,
                                   settings.WIST, settings.LAVENDER)
        textRect = text.get_rect()
        subtextRect = subText.get_rect()
        newlineTextRect = newlineText.get_rect()
        lastLineTextRect = lastLineText.get_rect()

        textRect.center = (400, 100)
        subtextRect.center = (500, 150)
        newlineTextRect.center = (550, 200)
        lastLineTextRect.center = (550, 250)

        self.display_surface.blit(text, textRect)
        self.display_surface.blit(subText, subtextRect)
        self.display_surface.blit(newlineText, newlineTextRect)
        self.display_surface.blit(lastLineText, lastLineTextRect)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < settings.WINDOW_WIDTH / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0

        elif player_x > settings.WINDOW_WIDTH - (settings.WINDOW_WIDTH / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0

        else:
            self.world_shift = 0
            player.speed = 8

    # def scroll_y(self):
    #     player = self.player.sprite
    #     player_y = player.rect.centery
    #     direction_y = player.direction.y
    #
    #     if player_y < settings.WINDOW_HEIGHT / 4 and direction_y <= 0:
    #         self.world_shift_y = 8
    #     elif player_y > settings.WINDOW_HEIGHT - (settings.WINDOW_HEIGHT / 4) and direction_y >= 0:
    #         self.world_shift_y = -8
    #     else:
    #         self.world_shift_y = 0
    #         player.direction.y = 0

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        collidable_sprites = self.terrain_sprites.sprites()
        collidable_enemies = self.enemy_sprites.sprites()
        collidable_goals = self.goal.sprites()

        for enemy in collidable_enemies:
            if pygame.sprite.collide_rect(player, enemy):
                enemy.kill()

        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
        for sprite in collidable_goals:
            if sprite.rect.colliderect(player.rect):
                print("You've hit the exit!")

    def vertical_collision(self):

        player = self.player.sprite
        player.apply_gravity()
        collidable_sprites = self.terrain_sprites.sprites()
        collidable_enemies = self.enemy_sprites.sprites()

        for enemy in collidable_enemies:
            if pygame.sprite.collide_rect(player, enemy):
                enemy.kill()

        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0

    def create_tile_group(self, layout, param):
        sprite_group = pygame.sprite.Group()
        sprite = None

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if int(val) > 0:
                    x = col_index * settings.TILE_SIZE * 2
                    y = row_index * settings.TILE_SIZE * 2
                    if param == 'Terrain':
                        terrain_tile_list = world_helper.import_cut_graphics(
                            'Assets/Enviroment/layers/spritesheet-final.png')
                        tile_surface = terrain_tile_list[int(val)]
                        tile_surface = pygame.transform.scale(tile_surface, (32, 32))
                        sprite = StaticTiles.Static_Tiles(settings.TILE_SIZE, x, y, tile_surface)

                    if param == 'Background':
                        background_tile_list = world_helper.import_cut_graphics(
                            'Assets/Enviroment/layers/spritesheet-final.png')
                        tile_surface = background_tile_list[int(val)]
                        tile_surface = pygame.transform.scale(tile_surface, (32, 32))
                        sprite = StaticTiles.Static_Tiles(settings.TILE_SIZE, x, y, tile_surface)

                    if param == 'Enemies':
                        if val == '1':
                            sprite = En.Enemy(settings.TILE_SIZE, x, y)
                        if val == '2':
                            sprite = En.Jumper(settings.TILE_SIZE, x, y)
                        if val == '11':
                            sprite = En.Chungus(settings.TILE_SIZE, x, y)
                    if param == 'Constraints':
                        sprite = Tile.Tile(settings.TILE_SIZE, x, y)

                    if param == 'Kill_tiles':
                        sprite = Tile.Tile(settings.TILE_SIZE, x, y)

                    sprite_group.add(sprite)
        return sprite_group

    def enemy_Reverse(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraint_sprites, False):
                enemy.reverse()

    def update(self):

        # Draw background game layers
        self.draw_background()
        self.scroll_x()

        self.background_sprites.update(self.world_shift)
        self.background_sprites.draw(self.display_surface)

        self.terrain_sprites.draw(self.display_surface)

        # Enemies and constraints
        self.enemy_sprites.update(self.world_shift)
        self.constraint_sprites.update(self.world_shift)
        self.enemy_Reverse()
        self.enemy_sprites.draw(self.display_surface)

        self.terrain_sprites.update(self.world_shift)

        # player sprites
        self.player.update()
        self.player.draw(self.display_surface)

        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)
        self.player.draw
        self.player.update()

        self.horizontal_collision()
        self.vertical_collision()

    def player_setup(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * settings.TILE_SIZE * 2
                y = row_index * settings.TILE_SIZE * 2
                if int(val) == 26:
                    sprite = Player.Player((x, y), self.display_surface)
                    self.player.add(sprite)

                if val == '0':
                    print("here's the exit")
                    exit_surface = pygame.image.load('Assets/Enviroment/props/gate-02.png').convert_alpha()
                    exit_surface = pygame.transform.scale(exit_surface,
                                                          (128, 128))
                    sprite = StaticTiles.Static_Tiles(settings.TILE_SIZE, x, y, exit_surface)
                    self.goal.add(sprite)


class Level2:
    def __init__(self, level_data, display_surface):

        # setting up the level
        self.world_shift = 0
        self.world_shift_y = 0
        self.display_surface = display_surface

        self.background_image = pygame.image.load('Assets/Enviroment/layers/middleground.png').convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image,
                                                       (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

        # importing Level Data
        terrain_layout = world_helper.import_csv_layout(level_data.level_2['Terrain'])
        #        background_layout = world_helper.import_csv_layout(level_data.level_2['Background'])

        # creating player
        player_layout = world_helper.import_csv_layout(level_data.level_2['Player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

        # Creating tile groups

        self.terrain_sprites = self.create_tile_group(terrain_layout, 'Terrain')
        #  self.background_sprites = self.create_tile_group(background_layout, 'Background')

        # Enemies
        enemy_layout = world_helper.import_csv_layout(level_data.level_1['Enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout, 'Enemies')

        # constraints
        constraint_layout = world_helper.import_csv_layout(level_data.level_1['Constraints'])
        self.constraint_sprites = self.create_tile_group(constraint_layout, "Constraints")

    def create_tile_group(self, layout, param):
        sprite_group = pygame.sprite.Group()
        sprite = None

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if int(val) > 0:
                    x = col_index * settings.TILE_SIZE * 2
                    y = row_index * settings.TILE_SIZE * 2
                    if param == 'Terrain':
                        terrain_tile_list = world_helper.import_cut_graphics(
                            'Assets/Enviroment/layers/spritesheet-final.png')
                        tile_surface = terrain_tile_list[int(val)]
                        tile_surface = pygame.transform.scale(tile_surface, (32, 32))
                        sprite = StaticTiles.Static_Tiles(settings.TILE_SIZE, x, y, tile_surface)

                    # if param == 'Background':
                    #     background_tile_list = world_helper.import_cut_graphics(
                    #         'Assets/Enviroment/layers/spritesheet-final.png')
                    #     tile_surface = background_tile_list[int(val)]
                    #     tile_surface = pygame.transform.scale(tile_surface, (32, 32))
                    #     sprite = StaticTiles.Static_Tiles(settings.TILE_SIZE, x, y, tile_surface)

                    if param == 'Enemies':
                        if val == '1':
                            sprite = En.Enemy(settings.TILE_SIZE, x, y)
                        if val == '2':
                            sprite = En.Jumper(settings.TILE_SIZE, x, y)
                        if val == '11':
                            sprite = En.Chungus(settings.TILE_SIZE, x, y)

                    if param == 'Constraints':
                        sprite = Tile.Tile(settings.TILE_SIZE, x, y)

                    sprite_group.add(sprite)
        return sprite_group

    def player_setup(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * settings.TILE_SIZE * 2
                y = row_index * settings.TILE_SIZE * 2
                if int(val) == 26:
                    sprite = Player.Player((x, y), self.display_surface)
                    self.player.add(sprite)

                if val == '0':
                    print("here's the exit")
                    exit_surface = pygame.image.load('Assets/Enviroment/props/gate-02.png').convert_alpha()
                    exit_surface = pygame.transform.scale(exit_surface,
                                                          (128, 128))
                    sprite = StaticTiles.Static_Tiles(settings.TILE_SIZE, x, y, exit_surface)
                    self.goal.add(sprite)

    def enemy_Reverse(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraint_sprites, False):
                enemy.reverse()

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        font = pygame.font.Font('freesansbold.ttf', 24)

        collidable_enemies = self.enemy_sprites.sprites()
        collidable_goals = self.goal.sprites()

        for enemy in collidable_enemies:
            if pygame.sprite.collide_rect(player, enemy):
                enemy.kill()

        for sprite in self.terrain_sprites.sprites():

            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left

        for sprite in collidable_goals:
            for enemy in collidable_enemies:
                if sprite.rect.colliderect(player.rect):
                    print("You've hit the exit!")
                    self.instructions(1)

    def draw_background(self):

        self.display_surface.blit(self.background_image, (0, 0))

    def end(self):
        pygame.display.quit()
        pygame.quit()

    def instructions(self, wincondition):

        welcome_font = pygame.font.Font('freesansbold.ttf', 36)
        font = pygame.font.Font('freesansbold.ttf', 24)

        if wincondition == 1:
            self.update()

        # Instructions

        text = welcome_font.render('Welcome To Level 2!', True, settings.LAVENDER, settings.WIST)
        subText = font.render("Ram Chungus & Roll to the end to win! Thanks for playing my game!", True,
                              settings.WIST, settings.LAVENDER)
        textRect = text.get_rect()
        subtextRect = subText.get_rect()

        textRect.center = (400, 100)
        subtextRect.center = (450, 150)
        self.display_surface.blit(text, textRect)
        self.display_surface.blit(subText, subtextRect)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < settings.WINDOW_WIDTH / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0

        elif player_x > settings.WINDOW_WIDTH - (settings.WINDOW_WIDTH / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0

        else:
            self.world_shift = 0
            player.speed = 8

    def draw(self):
        # Draw background game layers

        self.draw_background()
        self.scroll_x()

        self.terrain_sprites.draw(self.display_surface)

        # Enemies and constraints
        self.enemy_sprites.update(self.world_shift)
        self.constraint_sprites.update(self.world_shift)
        self.enemy_Reverse()
        self.enemy_sprites.draw(self.display_surface)
        self.instructions(0)

        self.terrain_sprites.update(self.world_shift)

        # player sprites
        self.player.update()
        self.player.draw(self.display_surface)

        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)
        self.player.draw
        self.player.update()

        self.horizontal_collision()

    def update(self):
        font = pygame.font.Font('freesansbold.ttf', 36)

        self.display_surface.fill('grey')
        text = font.render('Congratulations you win!!, thanks for playing!', True, settings.LAVENDER, settings.WIST)
        textRect = text.get_rect()

        textRect.center = (500, 100)

        self.display_surface.blit(text, textRect)
        pygame.display.quit()
        pygame.quit()
        sys.exit(0)
