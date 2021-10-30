import pygame

import colors


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, is_material, type):
        super().__init__()
        self.is_material = is_material
        self.is_movable = False
        self.type = type
        self.image = pygame.Surface((size, size))
        self.set_color()
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft = pos)

    def set_color(self):
        if self.type == 'wall':
            self.color = colors.DARKGRAY
        elif self.type == 'floor':
            self.color = (30, 30, 30)
        else:
            self.color = colors.RED

    def update(self):
        pass

    def draw(self, surface, offset):
        pos = (self.rect.topleft[0] - offset[0], self.rect.topleft[1] - offset[1])
        surface.blit(self.image, pos)
