


import pygame
from enums.direction import Direction

from models.snake_body import SnakeBody


def executeKeyAction(key: pygame.key,snakeBody: SnakeBody):
    if key == pygame.K_LEFT and snakeBody.direction != Direction.RIGHT:
            snakeBody.direction = Direction.LEFT
    if key == pygame.K_RIGHT and snakeBody.direction != Direction.LEFT:
            snakeBody.direction = Direction.RIGHT
    if key == pygame.K_UP and snakeBody.direction != Direction.DOWN:
            snakeBody.direction = Direction.UP
    if key == pygame.K_DOWN and snakeBody.direction != Direction.UP:
            snakeBody.direction = Direction.DOWN