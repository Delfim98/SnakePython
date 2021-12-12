from typing import List
from action.fruit import generateFruit
from models.cell import Cell
from models.snake_body import SnakeBody
from models.board import Board

def snakeCollisionCheck(snakeBody: SnakeBody, board: Board) -> bool:
    headCell: Cell = snakeBody.bodyCells[len(snakeBody.bodyCells) - 1]
    x, y = snakeBody.direction.moveCoordinates(headCell.x, headCell.y,board.width,board.height)
    newHeadCell: Cell = board.findCellByCoordinates(x, y)
    if(newHeadCell.occupied):
        if(newHeadCell.fruit):
            eatFruit(snakeBody,newHeadCell)
            generateFruit(board)
        else:
            return True
    return False

def eatFruit(snakeBody:SnakeBody,cellWithFruit:Cell):
    snakeBody.length += 1
    cellWithFruit.fruit = False
    snakeBody.bodyCells.append(cellWithFruit)

def moveSnake(snakeBody: SnakeBody, board: Board) -> List[Cell]:
    headCell: Cell = snakeBody.bodyCells[len(snakeBody.bodyCells) - 1]
    tailCell: Cell = snakeBody.bodyCells.pop(0)
    tailCell.occupied = False
    x, y = snakeBody.direction.moveCoordinates(headCell.x, headCell.y,board.width,board.height)
    newHeadCell: Cell = board.findCellByCoordinates(x, y)
    newHeadCell.occupied = True
    snakeBody.bodyCells.append(newHeadCell)
