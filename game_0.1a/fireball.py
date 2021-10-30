import pygame
from random import randint
import math

import colors
from projectile_attack import ProjectileAttack


class Fireball(ProjectileAttack):
    def __init__(self, start_pos, final_pos):
        SPEED = 6
        self.size_of_attack = 50
        image = pygame.Surface((self.size_of_attack, self.size_of_attack))
        image.fill(colors.DARKORANGE)
        super().__init__(self.size_of_attack, start_pos, final_pos, SPEED, image)
        self.direction()
