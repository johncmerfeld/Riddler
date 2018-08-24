"""
  RockPaperScissorsHop
  
  created by:       John C. Merfeld
  last modified:    08 / 24 / 2018
  
      Basically, we use a 1D array of zeros to represent the 'game board.'
  Players 1 and 2 move toward each other until they meet on the same space or
  adjacent spaces. We flip 3-sided coins to determine the winner (they keep
  playing if it's a tie) and the loser returns to their starting spot. If some-
  one wins while they're at the loser's end, the game stops and the time is
  recorded. Thousands of trials are run to determine an average by number of
  hoops on the board.

"""

import numpy as np
import sys
from random import randint

# define 'game board' class
class Board():

    def __init__(self, Nhoops):
        self.hoops = np.zeros(Nhoops + 2, dtype = int)
        self.hoops[0] = 1
        self.hoops[Nhoops + 1] = 2
        self.Nhoops = Nhoops + 2
        self.t = 0
        self.winner = 0

# plays the game, keeps track of the board throughout time
def iterate(arr):

    # check if they can move
    if playersCanMove(arr):
        # if they can move, move them
        arr = movePlayers(arr)
        arr.t += 1
        #printBoard(arr)
        return arr
    # else, play RPS
    else: 
        arr = playRPS(arr)
        #printBoard(arr)
        return arr

# debugger function
def printBoard(arr):
    print(arr.t)
    print(arr.hoops)

# checks if players can move or if they're close enough to play RPS
def playersCanMove(arr):
    Nhoops = arr.Nhoops
    for x in range(Nhoops):
        # if players are in same hoop
        if arr.hoops[x] == 3:
            return False
        # or if they are in adjacent hoops
        elif arr.hoops[x] == 1 and arr.hoops[x + 1] == 2:
            return False
    return True

# move the players closer together
def movePlayers(arr):
    Nhoops = arr.Nhoops
    x = 0
    while x < Nhoops:
        # move player 1 to the right
        if arr.hoops[x] == 1:
            arr.hoops[x] = 0
            arr.hoops[x + 1] += 1
            x += 2
        # move player 2 to the left
        elif arr.hoops[x] == 2:
            arr.hoops[x] = 0
            arr.hoops[x - 1] += 2
            return arr
        else:
            x += 1
    return arr

# play rock paper scissors and check if anyone has reached the end
def playRPS(arr):
    decided = False
    loser = 0
    while not decided:
        loser = randint(1,3)
        # if it's a tie
        if loser == 3:
            arr.t += 1
            continue
        # if player 1 wins
        elif loser == 2:
            arr.t += 1
            decided = True
        # if player 2 wins
        elif loser == 1:
            arr.t += 1
            decided = True
    
    # adjust the board
    Nhoops = arr.Nhoops
    for x in range(Nhoops):
        if arr.hoops[x] == 3 or arr.hoops[x] == loser:
            arr.hoops[x] -= loser
            if loser == 1:
                # check if player 2 was in a winning position when they won this match
                if arr.hoops[1] == 2:
                    arr.winner = 2
                    return arr
                else:
                    arr.hoops[0] = 1
            else:
                # check if player 1 was in a winning position when they won this match
                if arr.hoops[Nhoops - 2] == 1:
                    arr.winner = 1
                    return arr
                else:
                    arr.hoops[Nhoops - 1] = 2
    return arr

# run a bunch of trials to get an average
def testOutcomes(Nhoops, Ntrials):
    
    results = np.zeros(Ntrials, dtype = int)
    for x in range(len(results)):
        arr1 = Board(Nhoops)
        while arr1.winner == 0:
            arr1 = iterate(arr1)
        results[x] = arr1.t
    
    return np.mean(results)

maxHoops = int(sys.argv[1])
Ntrials = int(sys.argv[2])

rpsh = np.zeros(maxHoops, dtype = float)
for Nhoops in range(maxHoops):
    rpsh[Nhoops] = testOutcomes(Nhoops, Ntrials)

filename = "rpsh_" + str(maxHoops) + "_" + str(Ntrials) + ".csv"

np.savetxt(filename, rpsh, delimiter = ",", fmt = '{%.2f}')
