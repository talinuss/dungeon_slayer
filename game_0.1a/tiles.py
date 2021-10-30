import pygame

import colors


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, is_material, type_of_tile):
        super().__init__()
        self.is_material = is_material
        self.type_of_tile = type_of_tile
        self.image = pygame.Surface((size, size))
        self.set_color()
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft = pos)

    def set_color(self):
        if self.type_of_tile == 'wall':
            self.color = colors.DARKGRAY
        elif self.type_of_tile == 'floor':
            self.color = (30, 30, 30)
        else:
            self.color = colors.RED

    def update(self, x_shift, y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift
