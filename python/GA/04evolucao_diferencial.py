import random
import numpy as np
from visualization import line_plot

def rastrigin_function(variables):
    N = len(variables)
    return (10 * N) + np.sum((np.power(variables,2)) - (10 * np.cos(2 * np.pi * variables)))

def dejong_sphere(variables):
    return np.sum(np.power(variables,2))

def generate_random_population(dimension=2,length=1,bounds=[-1,1]):
    return [np.random.uniform(*bounds,size=dimension) for _ in range(0,length)]

def sample_individuals(population,size=3):
    return random.sample(population,k=size)

def fitness(individual):
    # return dejong_sphere(individual)
    return rastrigin_function(individual)

def tourney(vetor_original,vetor_experimental):
    if fitness(vetor_experimental) < fitness(vetor_original):
        return vetor_experimental
    else:
        return vetor_original

def mutation(alfa,beta,gama,F_mutation=0.8):
    return alfa + F_mutation * (beta - gama)

def crossover(vetor_original,vetor_modificado,cross_rate=0.9):
    return binomial_crossover(vetor_original,vetor_modificado,cross_rate)

def binomial_crossover(vetor_original,vetor_modificado,cross_rate=0.9):
    vetor_random = np.random.uniform(0,1,size=len(vetor_original))
    return np.where(vetor_random < cross_rate,vetor_modificado,vetor_original)

def exponencial_crossover(vetor_original,vetor_modificado,cross_rate=0.9):
    random_number = np.random.rand()
    index = 0
    while random_number < cross_rate:
        index += 1
        random_number = np.random.rand()
    
    return np.concatenate([vetor_modificado[:index],vetor_original[index:]],axis=None)

def print_out(population):
    for p in population: print('->',fitness(p))

def sort_population(population):
    return sorted(population,key=lambda item: fitness(item))
        
if __name__ == "__main__":
    D_DIMENSIONS = 20
    NP_POPULATION = 50
    CR = 0.9
    F = 0.8
    GEN_MAX = 10000
    
    bounds = [-5.12,5.12]

    population = generate_random_population(dimension=D_DIMENSIONS,length=NP_POPULATION,bounds=bounds)

    # print_out(sort_population(population))

    generation = 0
    while generation < GEN_MAX:
        new_population = list()
        for p in population:
            a,b,c = sample_individuals(population)
            V = mutation(a,b,c)
            U = crossover(p,V)
            T = tourney(p,U)
            new_population.append(T)
        
        population = new_population
        generation += 1


    print('\n\nResultado:')
    # print_out(sort_population(population))

    ax = line_plot(data=sort_population(population),
        _x=range(1,len(population)+1),
        _y=lambda i: fitness(i),
        output_file='fitness_dejong.png',
        title="Fitness final da população",
        xlabel="População",
        ylabel="fitness"
        )
