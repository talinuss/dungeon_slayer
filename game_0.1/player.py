import math

import pygame

import colors
from fireball import Fireball
import settings


class Player(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.image = pygame.Surface((32,50))
        self.color = colors.RED
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft= self.level.startplayer_pos)
        
        self.is_movable = True
        self.is_material = True

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
        start_pos = (self.rect.center[0], self.rect.center[1])
        final_pos = (mouse_pos[0] + self.level.offset[0], mouse_pos[1] + self.level.offset[1])
        fireball = Fireball(start_pos, final_pos)
        self.level.objects.append(fireball)

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

    def scroll_x(self):
        if self.x_direction != 0:
            self.level.world_shift_x = self.x_speed
        else:
            self.level.world_shift_x = 0
        self.level.scroll_x()

    def scroll_y(self):
        if self.y_direction != 0:
            self.level.world_shift_y = self.y_speed
        else:
            self.level.world_shift_y = 0
        self.level.scroll_y()

    def horizontal_movement_collison(self):
        self.rect.x += self.x_speed

        is_collised = 0
        for sprite in self.level.objects:
            if sprite.type in ['wall', 'enemy'] and sprite.rect.colliderect(self.rect):
                if self.x_direction < 0:
                    self.rect.left = sprite.rect.right
                elif self.x_direction > 0:
                    self.rect.right = sprite.rect.left
                is_collised = 1

        if not is_collised:
            self.scroll_x()

    def vertical_movement_collison(self):
        self.rect.y += self.y_speed

        is_collised = 0
        for sprite in self.level.objects:
            if sprite.type in ['wall', 'enemy'] and sprite.rect.colliderect(self.rect):
                if self.y_direction < 0:
                    self.rect.top = sprite.rect.bottom
                elif self.y_direction > 0:
                    self.rect.bottom = sprite.rect.top
                is_collised = 1

        if not is_collised:
            self.scroll_y()

    def update(self):
        self.calculate_speed()
        self.horizontal_movement_collison()
        self.vertical_movement_collison()       

    def draw(self, surface):
        pos = (self.rect.topleft[0] - self.level.offset[0], self.rect.topleft[1] - self.level.offset[1])
        surface.blit(self.image, pos)
