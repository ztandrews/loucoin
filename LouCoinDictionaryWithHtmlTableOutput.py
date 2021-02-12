# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:00:52 2021

@author: ztand

It would be absolutely nuts if i got this to work.
I'm gonna try to format the output as an html table.
Godspeed. Let's give it a try.

Also, the name of this file is actually hilarous


ALSO, this might be the most unorginized file i've ever done. Lfg.
"""

#Beofre i toss any real code in here i'm gonna try to format a comma seperated list first
#What we in the industry call ''''getting our feet wet''''

#Below is the first code I wrote to test out my methods
'''
str = "Otto Koivula, 1.37879537"
lottaGuys = ["Otto Koivula, 1.37879537","Otto Koivula, 1.37879537","Otto Koivula, 1.37879537","Otto Koivula, 1.37879537","Otto Koivula, 1.37879537"]

table ='' 
for guy in lottaGuys:
    guySplit = guy.split(",")
    table+= "<tr><td>" + guySplit[0]+"</td><td>" + guySplit[1] + "</td></tr>" + "\n"


print (table)
'''

"""
IT WORKS!!!!!!!

BUT IT TAKES SO LONG TO RUN!!!!!!
"""
from sportsipy.nhl.roster import Player, Roster

#Create dictionary to hold players and their LouCoin values
islesDict = {}
#Change this to get stats from different years
currentYear = '2020-21'
islanders = Roster('NYI',slim=True)
iroster =[]
for a in islanders.players:
    p = Player(str(a))
    p(currentYear)
    iroster.append(p)
 
#Current value of 1 LouCoin. Will change based on what OV_Pod says
louCoin = 1.3794370
#Calculate LouCoin
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
htmlTable =''
def sortByValue():
    sortedByValueDict = sorted(islesDict.items(), key=lambda t:t[1], reverse=True)
    #sortedByValueDict is actually an array that is sorted. Each element is an element of the islesDict 
    #This loops through the array and cleans it up by getting rid of unneeded characters
    for player in sortedByValueDict:
        p0 = str(player)
        p1 = p0.replace('(','')
        p2 = p1.replace(')','')
        p3 = p2.replace("'",'')
        #print(p3)
        p4 =  p3.split(",")
        htmlTable = "<tr><td>" + p4[0]+"</td><td>" + p4[1] + "</td></tr>"
        print(htmlTable)

#Calls the sort function and prints out the result. Will then print out the total amount of LouCoin mined
sortByValue()
print()
print("Total LouCoin Mined:")
print(totalLouCoin)
#Now, take the output and copy it into the list to html converter website guy