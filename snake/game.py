
from pygame.math import Vector2
from new_snake import Snake
from fruit import Fruit

class Game:
    def __init__(self, board_width):
        self.board_width = board_width
        self.score = 0
        self.finished = False

        self.snake = Snake()
        self.fruit = Fruit(self.get_empty_positions())
        
    def update(self):
        self.snake.move_snake()
        self.update_fruit()
        self.check_fail()

    def get_empty_positions(self):
        empty_positions = []
        for x in range(self.board_width):
            for y in range(self.board_width):
                pos = x, y
                if pos not in self.snake.body:
                    empty_positions.append(pos)
        return empty_positions
    
    def update_fruit(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit = Fruit(self.get_empty_positions())
            self.snake.add_block()
            self.score += 1
             
    def check_fail(self):
        head = self.snake.body[0]
        if self.check_collision_wall(head.x) or self.check_collision_wall(head.y):
            self.finished = True
        
        if(self.snake.body[0] in self.snake.body[1:]):
            self.finished = True
    
    def check_collision_wall(self, coordinate):
        return not 0 <= coordinate < self.board_width
    
    def check_max_score(self):
        if self.score == self.board_width**2:
            self.finished = True

    # make snake move
    def make_move(self, vector):
        self.snake.direction = vector
    

    def accuator(self, moves):
        filtered_moves = [move * filter for move, filter in zip(moves, self._legal_move_filter())]
        sorted_moves = reversed(sorted(enumerate(filtered_moves), key=lambda x:x[1]))
        
        direction = list(sorted_moves)[0][0]
        return self.get_move_vectors[direction]

    def _legal_move_filter(self):
        return [not self.equal_vectors([1], self.snake.body[0] + v) for v in self.get_move_vectors()]
    
    def get_move_vector(self, index):
        return self.get_move_vectors[index]
    
    def get_move_vectors(self):
        return (Vector2(0, 1), Vector2(1, 0), Vector2(0, -1), Vector2(-1, 0))    
    
    def equal_vectors(self, v1, v2):
        return v1.x == v2.x and v1.y == v2.y
    
    def get_snake_body(self, player):
        return [self.map_state(player, i % self.size, i // self.size) for i in range(self.board_width**2)]
    
    
    def get_fruit_states(self, player):
        return [self.equal_vectors(Vector2(i % self.size, i // self.size), self.fruit.pos) for i in range(self.board_width**2)]


    def reset(self):
        # pygame.quit() 
        # sys.exit()
        self.snake.reset()
#setup & game variables