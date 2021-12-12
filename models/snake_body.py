
from typing import List
from enums.direction import Direction
from models.cell import Cell


class SnakeBody(object):
    direction: Direction = Direction.RIGHT
    length: int = 3
    bodyCells: List[Cell] = []

    def __init__(self,startingLength: int = 3,startingCells: List[Cell] = []):
        if startingLength != len(startingCells):
            raise ValueError()
        self.length = startingLength
        self.bodyCells = startingCells
        for cell in self.bodyCells:
            cell.occupied = True


    def __str__(self):
        return str(self.length)
