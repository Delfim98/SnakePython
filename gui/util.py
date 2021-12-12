from typing import List
import pygame
import math
from pygame.rect import Rect
from config.graphic_conf import GraphicConfig

from models.board import Board
from models.cell import Cell
from models.snake_body import SnakeBody
from functools import reduce

class GUIUtil(object):

    config:GraphicConfig
    height:int
    width:int
    cellHeight:int
    cellWidth:int

    def __init__(self) -> None:
        super().__init__()
        self.config = GraphicConfig()
        

    def initScreen(self)-> pygame.Surface:
        pygame.init()
        screen = pygame.display.set_mode([self.config.windowWidth, self.config.windowHeight])
        pygame.display.set_caption(self.config.windowCaption)
        screen.fill(self.config.backgroundColor)
        self.height = screen.get_height()
        self.width = screen.get_width()
        
        return screen


    def drawBoard(self,board: Board, screen: pygame.Surface):
        self.cellHeight = math.ceil(self.height / board.height)
        self.cellWidth = math.ceil(self.width / board.width)
        for line in board.matrix:
            for cell in line:
                rect = Rect(
                    (cell.x * self.cellWidth, cell.y * self.cellHeight), (self.cellWidth, self.cellHeight)
                )
                pygame.draw.rect(screen, self.config.cellBorderColor, rect, self.config.cellBorderSize)


    def clearEmptyCells(self,board: Board, screen: pygame.Surface) -> List[Rect]:
        rectsUpdated: List[Rect] = []
        for cell in list(
            filter(lambda c: not c.occupied, reduce(lambda a, b: a + b, board.matrix))
        ):
            rect = Rect(
                (
                    self.config.cellBorderSize + cell.x * self.cellWidth,
                    self.config.cellBorderSize + cell.y * self.cellHeight,
                ),
                (self.cellWidth - 2 * self.config.cellBorderSize, self.cellHeight - 2 * self.config.cellBorderSize),
            )
            rectsUpdated.append(rect)
            pygame.draw.rect(screen, self.config.backgroundColor, rect)
        return rectsUpdated


    def drawSnake(self, snakeBody: SnakeBody, screen: pygame.Surface) -> List[Rect]:
        rectsUpdated: List[Rect] = []
        for cell in snakeBody.bodyCells:
            rect = Rect(
                (
                    self.config.cellBorderSize + cell.x * self.cellWidth,
                    self.config.cellBorderSize + cell.y * self.cellHeight,
                ),
                (self.cellWidth - 2 * self.config.cellBorderSize, self.cellHeight - 2 * self.config.cellBorderSize),
            )
            rectsUpdated.append(rect)
            pygame.draw.rect(screen, self.config.snakeColor, rect)
        return rectsUpdated


    def drawFruit(self,screen: pygame.Surface, cell: Cell = None) -> List[Rect]:
        if(cell):
            rectsUpdated: List[Rect] = []
            rect = Rect(
                (self.config.cellBorderSize + cell.x * self.cellWidth, self.config.cellBorderSize + cell.y * self.cellHeight),
                (self.cellWidth - 2 * self.config.cellBorderSize, self.cellHeight - 2 * self.config.cellBorderSize),
            )
            pygame.draw.rect(screen, self.config.fruitColor, rect)
            rectsUpdated.append(rect)
            return rectsUpdated
