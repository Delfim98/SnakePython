from typing import List
import pygame
import random
from pygame.rect import Rect

from models.board import Board
from models.cell import Cell
from models.snake_body import SnakeBody
from functools import reduce


CELL_BORDER_SIZE = 4


def drawBoard(board: Board, screen: pygame.Surface):
    height = screen.get_height()
    width = screen.get_width()
    cellHeight = height / board.height
    cellWidth = width / board.width
    for line in board.matrix:
        for cell in line:
            rect = Rect(
                (cell.x * cellWidth, cell.y * cellHeight), (cellWidth, cellHeight)
            )
            pygame.draw.rect(screen, (0, 0, 255), rect, CELL_BORDER_SIZE)


def clearEmptyCells(board: Board, screen: pygame.Surface) -> List[Rect]:
    height = screen.get_height()
    width = screen.get_width()
    cellHeight = height / board.height
    cellWidth = width / board.width
    rectsUpdated: List[Rect] = []
    for cell in list(
        filter(lambda c: not c.occupied, reduce(lambda a, b: a + b, board.matrix))
    ):
        rect = Rect(
            (
                CELL_BORDER_SIZE + cell.x * cellWidth,
                CELL_BORDER_SIZE + cell.y * cellHeight,
            ),
            (cellWidth - 2 * CELL_BORDER_SIZE, cellHeight - 2 * CELL_BORDER_SIZE),
        )
        rectsUpdated.append(rect)
        pygame.draw.rect(screen, (255, 255, 255), rect)
    return rectsUpdated


def drawSnake(board: Board, snakeBody: SnakeBody, screen: pygame.Surface) -> List[Rect]:
    height = screen.get_height()
    width = screen.get_width()
    cellHeight = height / board.height
    cellWidth = width / board.width
    rectsUpdated: List[Rect] = []
    for cell in snakeBody.bodyCells:
        rect = Rect(
            (
                CELL_BORDER_SIZE + cell.x * cellWidth,
                CELL_BORDER_SIZE + cell.y * cellHeight,
            ),
            (cellWidth - 2 * CELL_BORDER_SIZE, cellHeight - 2 * CELL_BORDER_SIZE),
        )
        rectsUpdated.append(rect)
        pygame.draw.rect(screen, (0, 255, 0), rect)
    return rectsUpdated


def drawFruit(board: Board,screen: pygame.Surface, cell: Cell = None) -> List[Rect]:
    if(cell):
        height = screen.get_height()
        width = screen.get_width()
        cellHeight = height / board.height
        cellWidth = width / board.width
        rectsUpdated: List[Rect] = []
        rect = Rect(
            (CELL_BORDER_SIZE + cell.x * cellWidth, CELL_BORDER_SIZE + cell.y * cellHeight),
            (cellWidth - 2 * CELL_BORDER_SIZE, cellHeight - 2 * CELL_BORDER_SIZE),
        )
        pygame.draw.rect(screen, (255, 0, 0), rect)
        rectsUpdated.append(rect)
        return rectsUpdated
