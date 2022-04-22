import os
import pygame

class ImageHolder:
    def get_image(self, relative_path, cell_size):
        path = os.path.join(os.path.dirname(__file__))
        return pygame.transform.scale(pygame.image.load(path + relative_path).convert_alpha(), (cell_size, cell_size))


class FruitImageHolder(ImageHolder):
    def __init__(self, fruit, cell_size):
        self.apple = self.get_image("\graphics\Apple0002.png", cell_size)
        self.rect = pygame.Rect(int(fruit.pos.x * cell_size), int(fruit.pos.y * cell_size), cell_size,cell_size)


class SnakeImageHolder(ImageHolder):
    def __init__(self, snake, cell_size):
        self.head_up = self.get_image("\graphics\\head_up.png", cell_size)
        self.head_down = self.get_image("\graphics\\head_down.png", cell_size)
        self.head_right = self.get_image("\graphics\\head_right.png", cell_size)
        self.head_left = self.get_image("\graphics\\head_left.png", cell_size)
        
        self.tail_up = self.get_image("\graphics\\tail_up.png", cell_size)
        self.tail_down = self.get_image("\graphics\\tail_down.png", cell_size)
        self.tail_right = self.get_image("\graphics\\tail_right.png", cell_size)
        self.tail_left = self.get_image("\graphics\\tail_left.png", cell_size)
        
        self.body_tr = self.get_image("\graphics\\body_tr.png", cell_size)
        self.body_tl = self.get_image("\graphics\\body_tl.png", cell_size)
        self.body_br = self.get_image("\graphics\\body_br.png", cell_size)
        self.body_bl = self.get_image("\graphics\\body_bl.png", cell_size)
        
        self.body_vertical = self.get_image("\graphics\\body_vertical.png", cell_size)
        self.body_horizontal = self.get_image("\graphics\\body_horizontal.png", cell_size)

        self.snake = snake

        self.head_directions = {
            (0,-1) : self.head_up,
            (0,1) : self.head_down,
            (1,0) : self.head_right,
            (-1,0) : self.head_left
        }

        self.tail_directions = {
            (0,-1) : self.tail_up,
            (0,1) : self.tail_down,
            (1,0) : self.tail_right,
            (-1,0) : self.tail_left
        }


    def get_head(self):
        head_direction =  self.snake.body[0] - self.snake.body[1]
        x, y = head_direction.x, head_direction.y
        return self.head_directions[(x, y)]

    def get_tail(self):
        tail_direction =  self.snake.body[-2] - self.snake.body[-1]
        x, y = tail_direction.x, tail_direction.y
        return self.tail_directions[(x, y)]

    def get_corners(self, next_position, previous_position):
        if(previous_position.x == -1 and next_position.y == -1) or (previous_position.y == -1 and next_position.x == -1):
            return self.body_tl
        elif(previous_position.x == 1 and next_position.y == -1) or (previous_position.y == -1 and next_position.x == 1):
            return self.body_tr
        elif(previous_position.x == -1 and next_position.y == 1) or (previous_position.y == 1 and next_position.x == -1):
            return self.body_bl
        elif(previous_position.x == 1 and next_position.y == 1) or (previous_position.y == 1 and next_position.x == 1):
            return self.body_br

