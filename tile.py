class Tile:
    food = False
    x = 0
    y = 0
    blocked = False
    adj = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self) -> int:
        return self.x
    def getY(self) -> int:
        return self.y
