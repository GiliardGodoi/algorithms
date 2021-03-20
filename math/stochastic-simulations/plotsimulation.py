#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 Builds simulation's plots
'''
import random
import pylab

def plotFlip(minExp, maxExp):
    '''
    Assume minExp e maxExp inteiros positivos com minExp < maxExp.
    Desenha o gráfico de 2**minExpa 2**maxExp lançamentos de moedas.
    '''
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp,maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))
    pylab.title('Difference between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.semilogx(xAxis, diffs, ' ')
    pylab.semilogy(xAxis, diffs, ' ')
    pylab.plot(xAxis, diffs, 'bo')
    pylab.figure()
    pylab.title('Head/Tails Ratios')
    pylab.xlabel('Number of flips')
    pylab.ylabel('#Heads/#Tails')
    pylab.semilogx(xAxis, ratios, ' ')
    pylab.plot(xAxis, ratios, 'bo')
    pylab.show()

random.seed(0)
plotFlip(4, 20)
