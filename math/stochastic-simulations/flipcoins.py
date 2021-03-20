'''
Simulation model for flipping a coin.
'''
import random

def flip(numFlips):
    ''' Simulates flipping a coin numFlips times,
    and returns the fraction of flips that came up heads.
    '''
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads / numFlips

def flipSimulation(numFlipsPerTrial, numTrials):
    '''
    It runs flip function by 'numTrials' times.
    Returns the mean of heads percentages funded each trial.
    '''
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads) / len(fracHeads)
    return mean