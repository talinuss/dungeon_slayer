import math

import pygame

import colors
from fireball import Fireball


class Player(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.image = pygame.Surface((32,50))
        self.color = colors.RED
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft= self.level.player_pos)

        self.speed = 6
        self.x_direction = 0
        self.y_direction = 0
        self.x_speed = 0
        self.y_speed = 0

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def handle(self, key):
        if key == pygame.K_w:
            self.moving_up = not self.moving_up
        elif key == pygame.K_a:
            self.moving_left = not self.moving_left
        elif key == pygame.K_s:
            self.moving_down = not self.moving_down
        elif key == pygame.K_d:
            self.moving_right = not self.moving_right

    def mouse_hadler(self, type, mouse_pos, button=None):
        if type == pygame.MOUSEBUTTONDOWN:
            if button == 1:
                self.lmk_spell(mouse_pos)

    def lmk_spell(self, mouse_pos):
        fireball = Fireball(self.rect.center, mouse_pos)
        self.level.projectile_attacks.append(fireball)

    def calculate_speed(self):
        self.x_speed = 0
        self.y_speed = 0
        self.x_direction = 0
        self.y_direction = 0

        side_speed = round(math.sqrt(self.speed**2/2))
        if self.moving_up and self.moving_right:
            self.x_direction = 1
            self.y_direction = -1
        elif self.moving_up and self.moving_left:
            self.x_direction = -1
            self.y_direction = -1
        elif self.moving_down and self.moving_right:
            self.x_direction = 1
            self.y_direction = 1
        elif self.moving_down and self.moving_left:
            self.x_direction = -1
            self.y_direction = 1
        elif self.moving_up:
            self.y_direction = -1
        elif self.moving_down:
            self.y_direction = 1
        elif self.moving_right:
            self.x_direction = 1
        elif self.moving_left:
            self.x_direction = -1

        if self.x_direction != 0 and self.y_direction == 0:
            self.x_speed = self.x_direction * self.speed
        elif self.x_direction == 0 and self.y_direction != 0:
            self.y_speed = self.y_direction * self.speed
        else:
            self.x_speed = self.x_direction * side_speed
            self.y_speed = self.y_direction * side_speed

    def scroll_y(self):
        player_y = self.rect.centery

        if player_y < 300 and self.y_direction < 0:
            self.level.world_shift_y = -1 * self.y_speed
            self.y_speed = 0
        elif player_y > 600 and self.y_direction > 0:
            self.level.world_shift_y = -1 * self.y_speed
            self.y_speed = 0
        else:
            self.level.world_shift_y = 0

        self.level.scroll_y()

    def scroll_x(self):
        player_x = self.rect.centerx

        if player_x < 400 and self.x_direction < 0:
            self.level.world_shift_x = -1 * self.x_speed
            self.x_speed = 0
        elif player_x > 800 and self.x_direction > 0:
            self.level.world_shift_x = -1 * self.x_speed
            self.x_speed = 0
        else:
            self.level.world_shift_x = 0

        self.level.scroll_x()

    def horizontal_movement_collison(self):
        self.rect.x += self.x_speed

        for sprite in self.level.tiles.sprites():
            if sprite.is_material and sprite.rect.colliderect(self.rect):
                if self.x_direction < 0:
                    self.rect.left = sprite.rect.right
                elif self.x_direction > 0:
                    self.rect.right = sprite.rect.left

    def vertical_movement_collison(self):
        self.rect.y += self.y_speed

        for sprite in self.level.tiles.sprites():
            if sprite.is_material and sprite.rect.colliderect(self.rect):
                if self.y_direction < 0:
                    self.rect.top = sprite.rect.bottom
                elif self.y_direction > 0:
                    self.rect.bottom = sprite.rect.top

    def update(self):
        self.calculate_speed()
        self.scroll_x()
        self.horizontal_movement_collison()
        self.scroll_y()
        self.vertical_movement_collison()       

    def draw(self, surface):
        surface.blit(self.image, self.rect)
