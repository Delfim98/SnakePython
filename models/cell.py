class Cell(object):
    fruit = False
    occupied = False
    x = 0
    y = 0

    def __init__(self,x:int = 0 ,y:int = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x)