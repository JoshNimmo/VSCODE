from turtle import color, update
from typing import List
from pygame import Color
import pygame
import random
import tile


class Being:
    moves = 1
    x = 0
    y = 0
    hunger = 150
    color = (0,0,0)
    def __init__(self,moves,x,y,color = (random.randint(50,255),random.randint(50,255),random.randint(50,255))):
        self.moves = moves
        self.x = x
        self.y = y
        self.color = color
    def move(self,moves)->tile.Tile:
        self.hunger -= 1
        #print(moves)
        tile = random.choice(moves)
        if(tile.food == True): 
            self.eat(tile)
        self.updatePos(tile.x,tile.y)
        return tile
    def updatePos(self,x,y):
        self.x = x
        self.y = y
    def eat(self,tile):
        self.hunger += 50
        tile.food = False