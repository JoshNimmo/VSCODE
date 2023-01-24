import random
from typing import List
import pygame
import simulator.being as being
import simulator.tile as tile
import time
class Board: 
    board = [] #2d array of tiles to represent area blobs move on
    size = 0 #number of tiles in each row and column
    windowSize = 0 # size of the window created
    occupied = [] #list of beings currently on the board
    def __init__(self,size,windowSize):
        #constructer
        self.windowSize = windowSize
        self.size = size
        #creates size by size board of empty tiles
        for x in range(size):
            self.board.append([])
            for y in range(size):
                self.board[x].append(tile.Tile(x,y))
    def draw(self):
        # handles all of the drawing
        pygame.init()
        screen = pygame.display.set_mode((self.windowSize+200,self.windowSize)) # screen that will be drawn on
        running = True # variable for stopping drawing
        space =  self.windowSize/self.size #size of each of the tiles
        black = pygame.Surface((space-1,space-1))
        black2 = pygame.Surface((200,self.windowSize))
        font = pygame.font.Font(None,20)
        for x in range(self.size):
            #makes the lines on the scren
            pygame.draw.line(screen,pygame.Color(255,255,255),(space*(x+1),self.windowSize),(space*(x+1),0))
            pygame.draw.line(screen,pygame.Color(255,255,255),(self.windowSize,space*(x+1)),(0,space*(x+1)))
        
        while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    #quit if exit out
                    running=False
            count = 0
            screen.blit(black2, (self.windowSize+1,0))
            if(random.randint(0,2) == 0):
                #random chance to spawn food on the screen
                self.spawnFood(screen)
            for person in self.occupied:
                #moves person, prints their info on the side, makes them
                #reproduce if their hunger is above 150, and deletes them 
                #if the hunger is at 0
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
            #waits a tiny bit before running again
            time.sleep(.05)
        pygame.quit()
    def addBeing(self,thing:being.Being = None,x = -1, y = -1):
        #adds being to the board, thing, x, and y are optional
        if(x == -1):
            #if x not given, give random x
            x = random.randint(0,self.size-1)
        if(y == -1):
            #if y not given, give random y
            y = random.randint(0,self.size-1)
        if(thing == None):
            #if thing not given, create thing
            thing = being.Being(1,x,y)
        else:
            #otherwise update it to correct position
            thing.updatePos(x,y)
        self.occupied.append(thing)
    def getAdj(self,x,y)->List:
        #gets adjacent open tiles to whatever tiles is at x,y 
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
        if(len(re) == 0):
            #if nothing open, return the current tile
            re.append(self.board[x][y])
        return re
    def spawnFood(self,screen):
        #puts food at random x and y and draws green square to represent that
        x = random.randint(0,self.size-1)
        y = random.randint(0,self.size-1)
        self.board[x][y].food = True
        pygame.draw.rect(screen,(0,255,0),pygame.Rect(x*self.windowSize/self.size+1,y*self.windowSize/self.size+1,self.windowSize/self.size-1,self.windowSize/self.size-1))
    def printInfo(self,font,count,person,screen):
        #shows info of being on side of the screen
        text = str(count)+ ": x: " + str(person.x) + " y: " + str(person.y) + " hunger:" + str(person.hunger)
        img = font.render(text,False,(255,255,255))
        screen.blit(img,(self.windowSize+50, count * self.windowSize/self.size))
#b =  Board(20,600)
#b.draw()


