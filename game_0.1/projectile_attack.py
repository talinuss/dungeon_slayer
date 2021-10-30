import time
import math
from random import randint
import random

import pygame


class ProjectileAttack(pygame.sprite.Sprite):
    def __init__(self, size, start_pos, final_pos, speed, image):
        super().__init__()
        self.type = 'player_attack'

        self.start_pos = start_pos
        self.final_pos = final_pos
        self.coor_x = start_pos[0] - size // 2
        self.coor_y = start_pos[1] - size // 2
        self.speed = speed

        self.image = image
        self.rect = self.image.get_rect(center= self.start_pos)

    def direction(self):
        x_side = self.final_pos[0] - self.start_pos[0]
        y_side = self.final_pos[1] - self.start_pos[1]

        if x_side == 0: x_side = 1
        if y_side == 0: y_side = 1

        x_speed_digit = x_side / abs(x_side)
        x_side = abs(x_side)

        y_speed_digit = y_side / abs(y_side)
        y_side = abs(y_side)

        if x_side >= y_side:
            y_side /= x_side
            x_side /= x_side

        elif x_side < y_side:
            x_side /= y_side
            y_side /= y_side

        self.x_speed = math.sqrt(self.speed**2 / (x_side**2 + y_side**2)) * x_side 
        self.y_speed = self.x_speed / x_side * y_side 

        self.x_speed, self.y_speed = self.x_speed * x_speed_digit, self.y_speed * y_speed_digit
    
    def horizontal_movement_collison(self, level_objects):
        self.coor_x += self.x_speed
        self.rect.x = round(self.coor_x)

        for sprite in level_objects:
            if sprite.type in ['wall', 'enemy'] and sprite.rect.colliderect(self.rect):
                # some doings
                return True

    def vertical_movement_collison(self, level_objects):
        self.coor_y += self.y_speed
        self.rect.y = round(self.coor_y)

        for sprite in level_objects:
            if sprite.type in ['wall', 'enemy'] and sprite.rect.colliderect(self.rect):
                # some doings
                return True
                
    
    def update(self, level_objects):
        if self.horizontal_movement_collison(level_objects): return True

        if self.vertical_movement_collison(level_objects): return True

    def draw(self, surface, offset):
        pos = (self.rect.topleft[0] - offset[0], self.rect.topleft[1] - offset[1])
        surface.blit(self.image, pos)
