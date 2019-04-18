import pandas as pd
import numpy as np
import time
import os

from pso import SearchSpace
from util.benchmarks import quadratic_noise as function
from genetic.ga_binary import random_population, mutation, crossover, selection, normalize
from util.visualization import line_plot

pso = SearchSpace(costFunction=function,
                    nroParticles=50,
                    maxIteration=1000,
                    dimensions=50,
                    bounds=[-5.12,5.12],
                )
DATA = list()
def fitness(c1,c2,w):
    pso.set_updateStrategiesParams(c1=c1,c2=c2,w=w)
    pso.setup()
    pso.initialize_particles()
    pso.run()
    DATA.append(pso.get_gbest())

    return function(pso.get_gbest())

def decode_genes(genes,sublenght,limInf=-2,limSup=2):
    bit2number = lambda binary_string: int(binary_string,2)
    number2Real = lambda number: limInf + (((limSup - limInf)/(np.power(2,sublenght) - 1)) * number)
    bit2Real = lambda binary : number2Real(bit2number(binary))

    sequel = [genes[i:(i+sublenght)] for i in range(0,len(genes),sublenght) ]
    mapNumbers = map(bit2Real,sequel)
    return tuple(mapNumbers)


def evaluate_population(population):
        for chromosome in population:
            x,y,z = decode_genes(chromosome.genes,SUB_LENGHT)
            chromosome.score = fitness(x,y,z)

        return population

def sort_population(population,reversed=False):
        return sorted(population,key=lambda item : item.score, reverse=reversed)

if __name__ == "__main__":
    POPULATION_SIZE = 10
    SUB_LENGHT = 7
    QTD_VARIABLES = 3 # X, Y, Z
    MAX_REPEAT = 50
    limInf = -2
    limSuperior = 2

    generation = 0

    print('Inicializando GA')
    population = random_population(sizePopulation=POPULATION_SIZE,sizeChromosome=(SUB_LENGHT * QTD_VARIABLES))
    
    t_begin = time.time()
    while generation < MAX_REPEAT:
        print(f'GA: {generation}')
        inicio = time.time()
        population = evaluate_population(population)
        fim = time.time()
        print(f'avaliacao: {(fim-inicio)}')
        population = sort_population(population)
        population = normalize(population)
        selected = selection(population)
        population = crossover(selected)
        generation += 1
    t_end = time.time()

    print(f'Time: {(t_end - t_begin)}')

    population = evaluate_population(population)
    population = sort_population(population)

    for p in population: print(p.genes, p.score)

    line_plot(data=DATA,
            _x=range(1,len(DATA)+1),
            _y=lambda y : function(y),
            title="G_best",
            xlabel="iteracao",
            ylabel="g_best fitness",
            output_file=os.path.join("img",f'opt_{function.__name__}_gbest.png')
        )

    dfData = pd.DataFrame(DATA)
    fit = dfData.apply(function,axis=1)
    dfData["fitness"] = fit
    dfData.to_csv(os.path.join("data",f'opt_{function.__name__}_gbest.csv'))