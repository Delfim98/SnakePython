from functools import reduce
from typing import List
from models.cell import Cell

class Board(object):
    matrix: List[List[Cell]] = []
    width = 10
    height = 10

    def __init__(self,width = 10,height = 10):
        self.width = width
        self.height = height
        for y in range(height):
            line = []
            for x in range(width):
                line.append(Cell(x,y))
            self.matrix.append(line)


    def __str__(self):
        return str(self.matrix)

    def findCellByCoordinates(self,x: int,y: int)->Cell:
        return next((cell for cell in reduce(lambda a,b: a+b,self.matrix) if cell.x == x and cell.y == y))

