import random
from typing import List
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
        #for x in range(size):
            #for y  in range(size): 
                #self.board[x][y].adj = self.getAdj(x,y)
    def draw(self):
        pygame.init()
        screen = pygame.display.set_mode((self.windowSize+200,self.windowSize))
        running = True
        space =  self.windowSize/self.size
        black = pygame.Surface((space-1,space-1))
        black2 = pygame.Surface((200,self.windowSize))
        font = pygame.font.Font(None,20)
        for x in range(self.size):
            pygame.draw.line(screen,pygame.Color(255,255,255),(space*(x+1),self.windowSize),(space*(x+1),0))
            pygame.draw.line(screen,pygame.Color(255,255,255),(self.windowSize,space*(x+1)),(0,space*(x+1)))
        
        while running:
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
            count = 0
            screen.blit(black2, (self.windowSize+1,0))
            if(random.randint(0,10) == 5):
                self.spawnFood(screen)
            for person in self.occupied:
                self.board[person.x][person.y].blocked = False
                self.printInfo(font,count,person,screen)
                count += 1
                screen.blit(black,(person.x*space+1,person.y*space+1))
                person.move(self.getAdj(person.x,person.y)).blocked = True
                if(person.hunger >= 150):
                    self.addBeing(being.Being(1,0,0,person.color))
                    person.hunger-= 50
                if(person.hunger <= 0):
                    self.occupied.remove(person)
                else:
                    pygame.draw.rect(screen,person.color,pygame.Rect(person.x*space+1,person.y*space+1,space-1,space-1))
            pygame.display.flip()
            time.sleep(.1)
        pygame.quit()
    def addBeing(self,x,y): 
        self.occupied.append(being.Being(1,x,y))
    def addBeing(self,thing:being.Being):
        thing.updatePos(random.randint(0,self.size-1),random.randint(0,self.size-1))
        self.occupied.append(thing)
    def addBeing(self):
        self.occupied.append(being.Being(1,random.randint(0,self.size-1),random.randint(0,self.size-1)))
    def getAdj(self,x,y)->List:
        re = []
        if(x !=0 ):
            if(not self.board[x-1][y].blocked):
                re.append((self.board[x-1][y]))
        if(y !=0 ):
            if(not self.board[x][y-1].blocked):
                re.append((self.board[x][y-1]))
        if(x != self.size-1):
            if(not self.board[x+1][y].blocked):
                re.append((self.board[x+1][y]))
        if(y != self.size-1):
            if(not self.board[x][y+1].blocked):
                re.append((self.board[x][y+1]))
        return re
    def spawnFood(self,screen):
        x = random.randint(0,self.size-1)
        y = random.randint(0,self.size-1)
        self.board[x][y].food = True
        pygame.draw.rect(screen,(0,255,0),pygame.Rect(x*self.windowSize/self.size+1,y*self.windowSize/self.size+1,self.windowSize/self.size-1,self.windowSize/self.size-1))
    def printInfo(self,font,count,person,screen):
        text = str(count)+ ": x: " + str(person.x) + " y: " + str(person.y) + " hunger:" + str(person.hunger)
        img = font.render(text,False,(255,255,255))
        screen.blit(img,(self.windowSize+50, count * self.windowSize/self.size))
#b =  Board(20,600)
#b.draw()


