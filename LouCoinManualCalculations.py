# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 13:16:24 2021

@author: ztand
"""

'''
Program for when I have time to manually update loucoin.com
It's pretty simple. It just asks what the players previosu amount of $LOUCOIN is and how many hits they had for the game
It will loop until 'q' is entered when it asks the players previous amount of LouCoin
'''
import sys
louCoin = 1.3794370
print("Current value of LouCoin: " + str(louCoin))
run = True
while run == True:
    previousLouCoin = input("Enter the players previous amount of LouCoin or 'q' to exit: ")
    if previousLouCoin == 'q':
        sys.exit()
    else:
        hits = input("Enter the amount of hits the player had tonight: ")
        previousLouCoin = float(previousLouCoin)
        hits = float(hits)
        newLouCoin = previousLouCoin+(hits*louCoin)
        print("The players new LouCoin: " + str(newLouCoin))
