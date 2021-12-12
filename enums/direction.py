from abc import update_abstractmethods
from enum import Enum, auto
class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

    def moveCoordinates(self,x:int, y:int,maxWidth:int = 0,maxHeight:int = 0):
        newX = x
        newY = y
        if(self == Direction.UP):
            newY -= 1
        if(self == Direction.DOWN):
            newY += 1
        if(self == Direction.LEFT):
            newX -= 1
        if(self == Direction.RIGHT):
            newX += 1
        if maxWidth > 0:
            if maxWidth <= newX:
                newX = 0
            if newX < 0:
                newX = maxWidth - 1
        if maxHeight > 0:
            if maxHeight <= newY:
                newY = 0
            if newY < 0:
                newY = maxHeight - 1
        return newX,newY

    def __str__(self) -> str:
        return self.name