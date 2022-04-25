import pygame
from pygame.sprite import Sprite

import settings


class Player(Sprite):
    def __init__(self, pos, surface):
        super().__init__()

        self.isOnfloor = True
        self.animations = {'idle': [], 'run': [], 'jump': [], 'shoot': []}
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.10
        self.image = self.animations['idle'][self.frame_index]
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect(topleft=pos)

        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 20
        self.gravity = 5
        self.jump_speed = -25

        # player status
        self.status = 'idle'
        self.facing_right = True
        self.shoot = False
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

    def import_character_assets(self):
        character_path = './Assets/Animations/Character Animations/Player_char/'

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = settings.import_folder(full_path)


    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image
        self.shoot = False
        # set the rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)

        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)

        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)

        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)

        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)


    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
            if keys[pygame.K_x]:
                self.shoot = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
            if keys[pygame.K_x]:
                self.shoot = True
        elif keys[pygame.K_x]:
            self.shoot = True
        else:
            self.direction.x = 0
            self.direction.y = 0

        if keys[pygame.K_SPACE] and self.direction.y == 0:
            self.jump()


    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            elif self.shoot:
                self.status = 'shoot'
            else:
                self.shoot = False
                self.status = 'idle'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
        self.apply_gravity()

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()


