import random
'''
Simulation model for toss a dice.
'''

def rollDie():
    ''' Returns a random between 1 and 6 '''
    return random.choice([1,2,3,4,5,6])

def rollN(N):
    '''
    Simulates toss' a dice.
    '''
    result = ''
    for i in range(N):
        result += str(rollDie())
    return result

def checkPascal(numRolls, numTrial):
    ''' Assume numTrial > 0
    Retorna uma estimativa de probabilidade de ganho
    '''
    assert numRolls >= 1
    assert numTrial > 0
    numWins = 0.0
    for i in range(numTrial):
        for j in range(numRolls):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                numWins += 1
                break
    return numWins / numTrial

