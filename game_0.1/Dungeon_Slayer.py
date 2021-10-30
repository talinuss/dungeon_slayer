import time

import pygame

import colors
from game import Game
from level import Level
from player import Player
from settings import *
from text_object import TextObject


class DungeonSlayer(Game):
    def __init__(self):
        Game.__init__(self, 'Dungeon Slayer', SCREEN_WIDTH, SCREEN_HEIGHT, FRAME_RATE)
        self.start_level = False
        self.is_game_running = True
        
        self.create_objects()

    def create_objects(self):
        self.create_level()
        self.create_player(self.level)

    def create_level(self):
        self.level = Level(level_map)
        self.objects.append(self.level)

    def create_player(self, pos):
        self.player = Player(pos)
        self.objects.append(self.player)

        self.mouse_handlers.append(self.player.mouse_hadler)

        self.keydown_handlers[pygame.K_w].append(self.player.handle)
        self.keydown_handlers[pygame.K_a].append(self.player.handle)
        self.keydown_handlers[pygame.K_s].append(self.player.handle)
        self.keydown_handlers[pygame.K_d].append(self.player.handle)

        self.keyup_handlers[pygame.K_w].append(self.player.handle)
        self.keyup_handlers[pygame.K_a].append(self.player.handle)
        self.keyup_handlers[pygame.K_s].append(self.player.handle)
        self.keyup_handlers[pygame.K_d].append(self.player.handle)

    def show_message(self, text, color=colors.WHITE, font_name='Arial', font_size=20, centralized=False):
        message = TextObject(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, lambda: text, color, font_name, font_size)
        self.draw()
        message.draw(self.asurface, centralized)
        pygame.display.update()
        time.sleep(5)


game = DungeonSlayer()
game.run()
