from pygame.math import Vector2
from game import Game
from image_holder import SnakeImageHolder, FruitImageHolder
import pygame
import os

class GameUI:
    def __init__(self, board_width=20, cell_size=40):
        self.board_width = board_width
        self.board = Game(board_width)

        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((board_width * cell_size, board_width*cell_size))
        self.game_font = pygame.font.Font(os.path.join(os.path.dirname(__file__)) + "\VT323.ttf", 40)

        self.fruit_image_holder = FruitImageHolder(self.board.fruit, cell_size)
        self.snake_image_holder = SnakeImageHolder(self.board.snake, cell_size)
    
    def draw_elements(self):
        self.screen.fill((136, 222, 53))
        self.draw_fruit()
        self.draw_snake()
        self.draw_grass()
        self.draw_score()
        

    def draw_fruit(self):
        self.screen.blit(self.fruit_image_holder.apple, self.fruit_image_holder.rect)
            
    def draw_snake(self):
        snake_body = self.board.snake.body
        for index, block in enumerate(snake_body):
            x_pos = int(block.x * self.cell_size)
            y_pos = int(block.y * self.cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size)

            if (index == 0):
                self.screen.blit(self.snake_image_holder.get_head(), block_rect)
            elif (index == len(snake_body) - 1):
                self.screen.blit(self.snake_image_holder.get_tail(), block_rect)
            else:
                self.draw_snake_body(index, block, block_rect)
    

    def draw_snake_body(self, index, block, block_rect):
        snake_body = self.board.snake.body

        next_block =  snake_body[index + 1] - block
        previous_block = snake_body[index - 1] - block
        
        #horizontal / vertical
        if(previous_block.x == next_block.x):
            self.screen.blit(self.snake_image_holder.body_vertical, block_rect)
        elif(previous_block.y == next_block.y):
            self.screen.blit(self.snake_image_holder.body_horizontal, block_rect)
        #turning
        else:
            corner_image = self.snake_image_holder.get_corners(next_block, previous_block)
            self.screen.blit(corner_image, block_rect)

    def draw_grass(self):
        grass_color = (136, 202, 53)

        modifier = 0
        for row in range(self.board_width):
            if row % 2 == 0: modifier = 0
            else: modifier = 1

            for col in range(self.board_width):
                if (col + modifier) % 2 == 0:
                    grass_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, grass_color, grass_rect)
    
    def draw_score(self):
        score_text = str(len(self.board.snake.body) - 3)
        score_surface = self.game_font.render(score_text,True, (0,0,0))
        score_x = int(self.cell_size* self.board_width - 60)
        score_y = int(self.cell_size * self.board_width - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = self.fruit_image_holder.apple.get_rect(midright = (score_rect.left, score_rect.centery))

        self.screen.blit(score_surface, score_rect)
        self.screen.blit(self.fruit_image_holder.apple ,apple_rect)