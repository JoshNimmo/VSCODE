


from cmath import nan
from turtle import position
from unicodedata import name
import numpy

class Player:
    name = ""
    position = ""
    points = 0
    adp = 0.0
    def __init__(self,name,position,points,adp) -> None:
        self.name = name
        self.position = position
        self.points = points
        self.adp = adp
    def __le__(self,other) -> bool:
        if(other.adp == 0):
            return False
        return self.points <= other.points
    def __ge__(self,other) -> bool:
        if(other.adp == 0):
            return True
        return self.points >= other.points
    def __str__(self) -> str:
        return "Name: " + str(self.name) + "\tPosition: " + str(self.position) + "\tPoints: " + str(self.points) + "\tADP: " + str(self.adp) + "\n"