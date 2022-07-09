from turtle import update
from typing import List
from pygame import Color
import pygame
import random
import tile


class Being:
    moves = 1
    x = 0
    y = 0
    def __init__(self,moves,x,y):
        self.moves = moves
        self.x = x
        self.y = y
    def move(self,moves)->tile.Tile:
        #print(moves)
        tile = random.choice(moves)
        self.updatePos(tile.x,tile.y)
        return tile
    def updatePos(self,x,y):
        self.x = x
        self.y = y