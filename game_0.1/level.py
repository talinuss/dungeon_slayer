import pygame

import settings
from tiles import Tile


class Level:
    def __init__(self, level_data):
        self.objects = []
        self.setup_level(level_data)
        self.world_shift_x = 0
        self.world_shift_y = 0

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * settings.TILE_SIZE
                y = row_index * settings.TILE_SIZE
                if cell == 'W':
                    tile = Tile((x, y), settings.TILE_SIZE, 1, 'wall')
                    self.objects.append(tile)
                elif cell == ' ':
                    tile = Tile((x, y), settings.TILE_SIZE, 0, 'floor')
                    self.objects.append(tile)
                elif cell == 'P':
                    tile = Tile((x, y), settings.TILE_SIZE, 0, 'floor')
                    self.objects.append(tile)
                    self.startplayer_pos = (x, y)
                    self.offset = list((x - settings.SCREEN_WIDTH // 2, y - settings.SCREEN_HEIGHT // 2))
                    print(self.offset)

    def scroll_x(self):
        self.offset[0] += self.world_shift_x

    def scroll_y(self):
        self.offset[1] += self.world_shift_y
        
    def update(self):
        for index, object in enumerate(self.objects):
            if object.is_movable and object.is_material:
                if object.update(self.objects):
                    self.objects.pop(index)

    def draw(self, surface):
        for object in self.objects:
            object.draw(surface, self.offset)
