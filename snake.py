# Simple pygame program


# Import and initialize the pygame library

import pygame
from action.fruit import generateFruit, getFruit
from action.key_press import executeKeyAction
from action.movement import moveSnake, snakeCollisionCheck
from gui.util import GUIUtil
from models.board import Board
from models.snake_body import SnakeBody


# Set up the drawing window
guiUtil = GUIUtil()
screen = guiUtil.initScreen()


# Run until the user asks to quit

running = True



# Fill the background with white


board = Board()
guiUtil.drawBoard(board,screen)
snakeBody = SnakeBody(3,board.matrix[0][0:3])
guiUtil.drawSnake(snakeBody,screen)
guiUtil.drawFruit(screen,generateFruit(board))

pygame.display.flip()
pygame.time.set_timer(pygame.event.Event(pygame.USEREVENT),300)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            executeKeyAction(event.key,snakeBody)

        if event.type == pygame.USEREVENT:
            if(snakeCollisionCheck(snakeBody,board)):
                running = False
            moveSnake(snakeBody,board)
            pygame.display.update(guiUtil.clearEmptyCells(board,screen))
            pygame.display.update(guiUtil.drawSnake(snakeBody,screen))
            pygame.display.update(guiUtil.drawFruit(screen,getFruit(board)))

# Done! Time to quit.

pygame.quit()