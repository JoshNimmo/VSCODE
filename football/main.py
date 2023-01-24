from typing import List
import pandas 
from player import Player
playerCount = [0,0,0,0,0,0]
draftList = [[],[],[],[],[],[]]
def addToArray(ar:List, person:Player):
        index = 0
        while(index < len(ar) and ar[index] >= person):
            index += 1
        list.insert(ar,index,person)
def returnRow(positionName)-> int:
    if(positionName == "RB"):
        return 0
    if(positionName == "WR"):
        return 1
    if(positionName == "TE"):
        return 2
    if(positionName == "QB"):
        return 3
    if(positionName == "D"):
        return 4
    if(positionName == "K"):
        return 5
    return -1
def lastRemainingPlayer(list,limit)->Player:
    index = 0
    while(len(list) > index and list[index + 1].adp < limit):
        index += 1
    
    #if(index == 0 and len(list) > 1):
     #   print(list[index + 1])
    #  return list[index + 1]
    #print(list[index])
    return list[index]

def makePick(picksToNextPick,pickNumber):
    currentChoice = draftList[0][0]
    currentMax = 0
    count = 0
    for list in draftList:
       # print("First Player:\t")
       # print(list[0])
       # print("Last player: \t")
        difference = list[0].points - lastRemainingPlayer(list,pickNumber+picksToNextPick).points
        if((count <= 2 and playerCount[count] >= 2) or (count >= 3 and playerCount[count] >= 1)):
            print("divided")
            difference /= 4
        if(difference > currentMax):
            currentChoice = list[0]
            currentMax = difference
            count += 1 
    print("Pick: " + currentChoice.name)
    playerCount[returnRow(currentChoice.position)] += 1
    #removePlayer(currentChoice.name)
    pick = input("Enter player picked: ")
    toRemove = removePlayer(pick)
def removePlayer(name):
    re = []
    for list in draftList:
        for play in list:
            if(name in play.name):
                re.append(play)
    if(len(re) == 1):
        print("Removed " + re[0].name)
        draftList[returnRow(re[0].position)].remove(re[0])
    elif(len(re) > 1):
        print("Multiple players found, please enter more letters")
        for play in re:
            print(play)
        removePlayer(input("Enter player picked: "))
    else:
        print("No players found, please try again")
        removePlayer(input("Enter player picked: "))

def main():
    data = pandas.read_excel('/Users/joshuanimmo/Desktop/VSCODE/football/Player Rankings 2022.xlsx')
    data = data.fillna(0)
    #print(data.head(200))
    for x in range(len(data)): 
        toAdd:Player = Player(data.iloc[x]["Name"].lower(), data.iloc[x]["Position"],data.iloc[x]["Points"],data.iloc[x]["Average of  Mock"])
        addToArray(draftList[returnRow(toAdd.position)],toAdd)
    num = int(input("Enter number of players: "))
    numberOfDraftMembers = num
    round = int(input("Enter number of rounds: "))
    totalRounds = round
    pos = int(input("Enter your position: "))
    draftPosition = pos
    currentPosition = 1
    incrementing = True
    for x in range(totalRounds*numberOfDraftMembers):
        if(currentPosition == draftPosition):
            if(incrementing):
                if(currentPosition == numberOfDraftMembers):
                    makePick(numberOfDraftMembers*2 - 1,x)
                else :
                    makePick((currentPosition - numberOfDraftMembers)* -2,x)
            else:
                if(currentPosition == 1):
                    makePick(numberOfDraftMembers*2 - 1,x)
                else :
                    makePick((currentPosition - 1)* 2,x)
        else:
            pick = input("Enter player picked: ")
            toRemove = removePlayer(pick)
        if(incrementing):
            if(currentPosition == numberOfDraftMembers):
                incrementing = False
                currentPosition -= 1
            currentPosition += 1
        else:
            if(currentPosition == 1):
                incrementing = True
                currentPosition += 1
            currentPosition -= 1
        
main()        