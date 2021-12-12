from functools import reduce
import random
from models.cell import Cell
from models.board import Board

def generateFruit(board:Board)->Cell:
    possibleFruitTarget = list(
        filter(lambda c: not c.occupied, reduce(lambda a, b: a + b, board.matrix))
    )
    cell = possibleFruitTarget[random.randint(0, len(possibleFruitTarget)-1)]
    cell.occupied = True
    cell.fruit = True

def getFruit(board:Board)->Cell:
    return next((cell for cell in reduce(lambda a,b: a+b,board.matrix) if cell.fruit),None)
