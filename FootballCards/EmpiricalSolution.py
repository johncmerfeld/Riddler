#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 10:09:28 2018

  FootballCards

  created by:       John C. Merfeld
  last modified:    09 / 07 / 2018
  
      An extremely basic simulator. We pick n cards from the set of k and add 
  them to our collection. We stop when the collection is full!
  
"""
import random
import numpy as np

def howManyPacks(cardsInSet, cardsInDeck):
    
    # empty colleciton of carts
    cardsHas = np.zeros(cardsInSet, dtype = int)   
    packsBought = 0
    
    # buy cards until we have them all
    while np.any(cardsHas[:] == 0): 
        packsBought += 1
        # random.sample ensures no duplicates
        set = random.sample(range(0, cardsInSet), cardsInDeck)
        for i in set:
            cardsHas[i] = 1   
    return packsBought

# run a bunch of trials to get an average
def testOutcomes(Ntrials, cardsInSet, cardsInDeck):
    
    results = np.zeros(Ntrials, dtype = int)
    for x in range(len(results)):
        results[x] = howManyPacks(cardsInSet, cardsInDeck)
    
    return np.mean(results)

