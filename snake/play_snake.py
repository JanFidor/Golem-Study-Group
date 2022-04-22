import pygame
from game_ui import GameUI
import sys


def intercept_move():
    x = 1

def game_frame_update(game: GameUI):
    move = intercept_move()

    # make move
    game.board
pygame.init()
game = GameUI()
clock = pygame.time.Clock()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 170)
    #game loop
while not game.board.finished:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit() 
            sys.exit()
        if (event.type == SCREEN_UPDATE):
            game.draw_elements()
        
        user_input = pygame.key.get_pressed()

        if user_input[pygame.K_UP]:
            game.board.snake.change_snake_direction("up")
        if user_input[pygame.K_DOWN]:
            game.board.snake.change_snake_direction("d")
        if user_input[pygame.K_RIGHT]:
            game.board.snake.change_snake_direction("r")
        if user_input[pygame.K_LEFT]:
            game.board.snake.change_snake_direction("left")
            # if index == 1:
            #     if user_input[pygame.K_UP]:
            #         snake.change_snake_direction("d")
            #     if user_input[pygame.K_DOWN]:
            #         snake.change_snake_direction("u")
            #     if user_input[pygame.K_RIGHT]:
            #         snake.change_snake_direction("l")
            #     if user_input[pygame.K_LEFT]:
            #         snake.change_snake_direction("r")
        game.board.update()
        pygame.display.update()
        clock.tick(10)