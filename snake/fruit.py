import pygame
from random import choice
from pygame.math import Vector2

class Fruit:
    def __init__(self, possible_positions):
        self.pos = self.random_position(possible_positions)

    def random_position(self, possible_positions):
        x, y = choice(possible_positions)
        return Vector2(x, y)
