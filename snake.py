# Simple pygame program


# Import and initialize the pygame library

import pygame
from action.fruit import generateFruit, getFruit
from action.key_press import executeKeyAction
from action.movement import moveSnake, snakeCollisionCheck
from gui.util import clearEmptyCells, drawBoard, drawFruit, drawSnake
from models.board import Board
from models.snake_body import SnakeBody

pygame.init()


# Set up the drawing window

screen = pygame.display.set_mode([500, 500])


# Run until the user asks to quit

running = True



# Fill the background with white

screen.fill((255, 255, 255))

board = Board()
drawBoard(board,screen)
snakeBody = SnakeBody(3,board.matrix[0][0:3])
drawSnake(board,snakeBody,screen)
drawFruit(board,screen,generateFruit(board))


# Flip the display

pygame.display.flip()
pygame.time.set_timer(pygame.event.Event(pygame.USEREVENT),300)


while running:


    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:
            executeKeyAction(event.key,snakeBody)

        if event.type == pygame.USEREVENT or event.type == pygame.KEYDOWN:
            if(snakeCollisionCheck(snakeBody,board)):
                running = False
            moveSnake(snakeBody,board)
            pygame.display.update(clearEmptyCells(board,screen))
            pygame.display.update(drawSnake(board,snakeBody,screen))
            pygame.display.update(drawFruit(board,screen,getFruit(board)))

# Done! Time to quit.

pygame.quit()