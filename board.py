from ctypes import sizeof
from multiprocessing.connection import wait
from operator import truediv
from typing import List
from webbrowser import get
import pygame
import being
import tile
import time
class Board: 
    board = []
    size = 0
    windowSize = 0
    occupied = []
    def __init__(self,size,windowSize):
        self.windowSize = windowSize
        self.size = size
        for x in range(size):
            self.board.append([])
            for y in range(size):
                self.board[x].append(tile.Tile(x,y))
        for x in range(size):
            for y  in range(size): 
                self.board[x][y].adj = self.getAdj(x,y)
    def draw(self):
        pygame.init()
        screen = pygame.display.set_mode((self.windowSize,self.windowSize))
        running = True
        space =  self.windowSize/self.size
        black = pygame.Surface((space-2,space-2))
        for x in range(self.size-1):
            pygame.draw.line(screen,pygame.Color(255,255,255),(space*(x+1),self.windowSize),(space*(x+1),0))
            pygame.draw.line(screen,pygame.Color(255,255,255),(self.windowSize,space*(x+1)),(0,space*(x+1)))
        
        while running:
            time.sleep(.1)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
            for person in self.occupied:
                screen.blit(black,(person.x*space+1,person.y*space+1))
                person.move(self.getAdj(person.x,person.y))
                pygame.draw.rect(screen,pygame.Color(0,0,255),pygame.Rect(person.x*space+1,person.y*space+1,space-2,space-2))
            pygame.display.flip()
        pygame.quit()
    def addBeing(self,x,y): 
        self.occupied.append(being.Being(1,x,y))
    def getAdj(self,x,y)->List:
        re = []
        if(x !=0 ):
            re.append(self.board[x-1][y])
        if(y !=0 ):
            re.append(self.board[x][y-1])
        if(x != self.size-1):
            re.append(self.board[x+1][y])
        if(y != self.size-1):
            re.append(self.board[x][y+1])
        return re
#b =  Board(20,600)
#b.draw()


