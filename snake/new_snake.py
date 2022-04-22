import pygame
import sys
import random
from pygame.math import Vector2
from sympy import python
import neat
import os


class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.grow = False

    def change_snake_direction(self, dir):
        if self.direction.y == 0:
            if (dir == "u" or dir == "up"):
                self.direction = Vector2(0,-1)
            if dir == "d" or dir == "down":
                self.direction = Vector2(0,1)
        if self.direction.x == 0:        
            if dir == "r" or dir == "right":
                self.direction = Vector2(1,0)
            if dir == "l" or dir == "left":
                self.direction = Vector2(-1,0)

    def move_snake(self):
        if self.direction != Vector2 (0,0):
            if self.grow:
                body_copy = self.body
                self.grow = False
            else:
                body_copy = self.body[:-1]

            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy

    def add_block(self):
        self.grow = True
