# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:18:06 2021

@author: ztand
The offical back end to the LouCoin tracker
Code is neatly commented to make it easy to follow along on what is going on
"""

from sportsipy.nhl.roster import Player, Roster

#Create dictionary to hold players and their louCoin values
islesDict = {}
#Change this to get stats from different years
currentYear = '2020-21'
islanders = Roster('NYI',slim=True)
iroster =[]
for a in islanders.players:
    p = Player(str(a))
    p(currentYear)
    iroster.append(p)
 
#Calculate Lou Coin
louCoin = 1.3794370
def calculateLouCoin(Player):
    return Player.hits_at_even_strength*louCoin


#List of players that are either not skaters or have never played
neverPlayed = ['Cory Schneider','Jakub Skarek','Semyon Varlamov','Ilya Sorokin', 'Thomas Hickey', 'Tom Kuhnhackl', 'Otto Koivula', 'Sebastian Aho']

#Variable for total LouCoin mined so far. Will get calculated in next loop
totalLouCoin = 0

#Loop through the players, calculate their Lou Coin, add to total LouCoin, add to dict
for i in iroster:
    if i.name in neverPlayed:
        continue
    else:
        playersLouCoin = calculateLouCoin(i)
        totalLouCoin = playersLouCoin+totalLouCoin
        islesDict[i.name] = playersLouCoin

#Sort the dictionary that holds Islanders players and their LouCoin values
def sortByValue():
    sortedByValueDict = sorted(islesDict.items(), key=lambda t:t[1], reverse=True)
    #sortedByValueDict is actually an array that is sorted. Each element is an element of the islesDict 
    #This loops through the array and cleans it up by getting rid of unneeded characters
    for player in sortedByValueDict:
        p0 = str(player)
        p1 = p0.replace('(','')
        p2 = p1.replace(')','')
        p3 = p2.replace("'",'')
        print(p3)

#Calls the sort function and prints out the result. Will then print out the total amount of LouCoin mined
sortByValue()
print()
print("Total LouCoin Mined:")
print(totalLouCoin)
#Now, take the output and copy it into the list to html converter website guy
