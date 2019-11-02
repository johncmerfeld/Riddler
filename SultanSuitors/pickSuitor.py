import random as rand
import numpy as np
import pandas as pd

def randomlyOrderSuitors(n):
    return rand.sample(range(n), n)

# the sulton cannot know the suitor's absolute number
# but she can tell whether they are the best one she's seen so far
def isBestSuitorYet(newSuitor, bestSuitor):
    return newSuitor < bestSuitor

def runExperiment(n, wait):
    if wait >= n:
        raise ValueError("You can't wait for that many suitors")
    
    suitors = randomlyOrderSuitors(n)
    
    i = 0
    bestSuitor = 11
    lastSuitor = -1
    for suitor in suitors:
        lastSuitor = suitor
        if isBestSuitorYet(suitor, bestSuitor):
            # if we're past the waiting period, pick this one
            if i >= wait:
                return (suitor + 1, suitor == 0, suitor == 9, suitor < 5)
            # otherwise, mark this as the best suitor so far
            else:
                bestSuitor = suitor
        i += 1
        
    # If I saw the best suitor early on, sad
  #  print("Got to the end, and the last one I saw was", lastSuitor)
    return (lastSuitor + 1, lastSuitor == 0, lastSuitor == 9, lastSuitor < 5)

# run a bunch of trials to get an average
def testOutcomes(n, wait, Ntrials):
    
    results = []
    nWins = 0
    nLosses = 0
    nGoods = 0
    for i in range(0, Ntrials):
        result = runExperiment(n, wait)
        if result[1]:
            nWins += 1
        if result[2]:
            nLosses += 1
        if result[3]:
            nGoods += 1
        results.append(result[0])
    
    return (np.mean(results), np.std(results), nWins, nLosses, nGoods)

output = []

for nTrials in [1, 10, 100, 1000, 10000, 100000]:
    for n in range(10, 11):
        for w in range(0, 10):     
            result = testOutcomes(n, w, nTrials) 
            d = {
                'n' : n,
                'w' : w,
                'rank_sd' : round(result[1], 2),
                'avg_rank' : round(result[0], 2),
                'pct_wins' : (result[2] / nTrials) * 100,
                'pct_losses' : (result[3] / nTrials) * 100,
                'pct_goods' : (result[4] / nTrials) * 100,
                'n_trials' : nTrials
            }
            output.append(d)
        
output = pd.DataFrame(output)
        
#output.to_csv('CommunitiesLeft.csv')

print(output)
