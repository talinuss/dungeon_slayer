import pygame

from settings import TILE_SIZE
from tiles import Tile


class Level:
    def __init__(self, level_data):
        self.setup_level(level_data)
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.projectile_attacks = []
        

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if cell == 'W':
                    tile = Tile((x, y), TILE_SIZE, 1, 'wall')
                    self.tiles.add(tile)
                elif cell == ' ':
                    tile = Tile((x, y), TILE_SIZE, 0, 'floor')
                    self.tiles.add(tile)
                elif cell == 'P':
                    tile = Tile((x, y), TILE_SIZE, 0, 'floor')
                    self.tiles.add(tile)
                    self.player_pos = (x, y)

    def scroll_x(self):
        self.tiles.update(self.world_shift_x, 0)

    def scroll_y(self):
        self.tiles.update(0, self.world_shift_y)

    def update(self):
        for attack in self.projectile_attacks:
            attack.update()

    def draw(self, surface):
        self.tiles.draw(surface)
        for attack in self.projectile_attacks:
            attack.draw(surface)
