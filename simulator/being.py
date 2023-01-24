from tkinter.messagebox import NO
from turtle import color, update
from typing import List
from pygame import Color
import pygame
import random
import simulator.tile as tile
class Being:
    moves = 1 #=number of moves a being has
    x = 0 # current x coordinate 
    y = 0 #current y coordinate
    hunger = 125 #hunger value, spawns child at 150, dies at 0
    color = (0,0,0) #rgb color of being
    def __init__(self,moves,x,y,color = None):
        # constructer, color value is optional
        self.moves = moves
        self.x = x
        self.y = y
        if(color == None):
            #if color not set, make random color
            color = (random.randint(50,255),random.randint(50,255),random.randint(50,255))
        self.color = color
    def move(self,moves)->tile.Tile:
        #takes all options and chooses randomly, will be updated 
        self.hunger -= 1 # ticks hunger
        tile = random.choice(moves)
        if(tile.food == True): 
            #eats food if the tile it's on has food
            self.eat(tile)
        self.updatePos(tile.x,tile.y)
        #updates coordinates based on where it moves
        return tile
    def updatePos(self,x,y):
        #chnages x and y coordinates
        self.x = x
        self.y = y
    def eat(self,tile):
        #increases hunger and deletes food on tile
        self.hunger += 50
        tile.food = False