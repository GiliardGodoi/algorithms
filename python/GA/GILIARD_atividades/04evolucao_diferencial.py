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

def sample_individuals(population,qtd=3):
    return random.sample(population,k=qtd)

def fitness(individual):
    return dejong_sphere(individual)
    # return rastrigin_function(individual)

def tourney(vetor_original,vetor_experimental):
    if fitness(vetor_experimental) < fitness(vetor_original):
        return vetor_experimental
    else:
        return vetor_original

def mutation_simple(alfa,beta,gama,F_mutation=0.8):
    return alfa + F_mutation * (beta - gama)

def mutation_rand2(alfa,beta,gama,teta,omega,F_mutation=0.8):
    return alfa + F_mutation * (beta - gama) + F_mutation * (omega - teta)

def mutation_best(best,alfa,beta,gama,teta,F_mutation=0.8):
    return mutation_rand2(best,alfa,beta,gama,teta,F_mutation=F_mutation)

def mutation_target_to_best(best,x_i,alfa,beta,F_mutation=0.8):
    return x_i + F_mutation * (best - x_i) + F_mutation * (alfa - beta)

def crossover_binomial(vetor_original,vetor_modificado,cross_rate=0.9):
    vetor_random = np.random.uniform(0,1,size=len(vetor_original))
    return np.where(vetor_random < cross_rate,vetor_modificado,vetor_original)

def crossover_exponencial(vetor_original,vetor_modificado,cross_rate=0.9):
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
    from matplotlib import pyplot as plt

    # General configuration
    D_DIMENSIONS = 20
    NP_POPULATION = 100
    CR = 0.9
    F = 0.8
    GEN_MAX = 10000
    bounds = [-5.12,5.12]
    # A função de fitness é definida no início do arquivo, junto com as demais funções

    x = list(range(1,NP_POPULATION+1))


    ## DE/rand/1/bin
    population = generate_random_population(dimension=D_DIMENSIONS,length=NP_POPULATION,bounds=bounds)
    # print_out(sort_population(population))
    generation = 0
    while generation < GEN_MAX:
        new_population = list()
        for p in population:
            a,b,c = sample_individuals(population,qtd=3)
            V = mutation_simple(a,b,c,F_mutation=0.8)
            U = crossover_binomial(p,V,cross_rate=0.9)
            T = tourney(p,U)
            new_population.append(T)
            
        population = new_population
        generation += 1

    # print('\n\nResultado:')
    # print_out(sort_population(population))
    
    rand_bin = sorted([ fitness(p) for p in population ],reverse=True)

    plt.figure()
    plt.plot(x,rand_bin)
    plt.legend(['Rand binomial'],loc='upper right')
    plt.savefig(f'exercicio04-rand-binomial-comparacao-{D_DIMENSIONS}d-{GEN_MAX}r-v1.png')

    # ax = line_plot(data=sort_population(population),
    #     _x=range(1,len(population)+1),
    #     _y=lambda i: fitness(i),
    #     output_file='fitness_dejong.png',
    #     title="Fitness final da população",
    #     xlabel="População",
    #     ylabel="fitness"
    #     )

    ## DE/rand/1/exponencial
    population = generate_random_population(dimension=D_DIMENSIONS,length=NP_POPULATION,bounds=bounds)
    # print_out(sort_population(population))
    generation = 0
    while generation < GEN_MAX:
        new_population = list()
        for p in population:
            a,b,c = sample_individuals(population,qtd=3)
            V = mutation_simple(a,b,c,F_mutation=0.8)
            U = crossover_exponencial(p,V,cross_rate=0.9)
            T = tourney(p,U)
            new_population.append(T)
            
        population = new_population
        generation += 1


    rand_exponencial = sorted([ fitness(p) for p in population ],reverse=True)

    plt.figure()
    plt.plot(x,rand_exponencial)
    plt.legend(['Rand exponencial'],loc='upper right')
    plt.savefig(f'exercicio04-rand-exponencial-comparacao-{D_DIMENSIONS}d-{GEN_MAX}r-v1.png')

    ## DE/best/1/binomial
    population = generate_random_population(dimension=D_DIMENSIONS,length=NP_POPULATION,bounds=bounds)
    # print_out(sort_population(population))

    best_position = population[0]
    # Encontrar best_position antes de iniciar a rodada do algoritmo
    for p in population:
        if fitness(p) < fitness(best_position):
            best_position = np.copy(p)
    
    generation = 0
    while generation < GEN_MAX:
        new_population = list()
        best_i = best_position
        for p in population:
            a,b,c,d = sample_individuals(population,qtd=4)
            ## mutation_best(best,alfa,beta,gama,teta,F_mutation=0.8):
            V = mutation_best(best_i,a,b,c,d,F_mutation=0.8)
            U = crossover_binomial(p,V,cross_rate=0.9)
            T = tourney(p,U)
            new_population.append(T)

            if fitness(T) < fitness(best_position):
                best_position = np.copy(T)

        population = new_population
        generation += 1

    best_binomial = sorted([ fitness(p) for p in population ],reverse=True)

    plt.figure()
    plt.plot(x,best_binomial)
    plt.legend(['Best binomial'],loc='upper right')
    plt.savefig(f'exercicio04-best-binomial-comparacao-{D_DIMENSIONS}d-{GEN_MAX}r-v2.png')

    ## DE/target-to-best/1/binomial
    population = generate_random_population(dimension=D_DIMENSIONS,length=NP_POPULATION,bounds=bounds)
    # print_out(sort_population(population))

    best_position = population[0]
    # Encontrar best_position antes de iniciar a rodada do algoritmo
    for p in population:
        if fitness(p) < fitness(best_position):
            best_position = np.copy(p)
    generation = 0
    while generation < GEN_MAX:
        new_population = list()
        best_i = best_position
        for p in population:
            a,b = sample_individuals(population,qtd=2)
            ## mutation_target_to_best(best,x_i,alfa,beta,F_mutation=0.8)
            V = mutation_target_to_best(best_i,p,a,b,F_mutation=0.8)
            U = crossover_binomial(p,V,cross_rate=0.9)
            T = tourney(p,U)
            new_population.append(T)

            if fitness(T) < fitness(best_position):
                best_position = np.copy(T)

        population = new_population
        generation += 1

    target_best = sorted([fitness(p) for p in population ],reverse=True)
    plt.figure()
    plt.plot(x,target_best)
    plt.legend(['Target-to-best-binomial'],loc='upper right')
    plt.savefig(f'exercicio04-target-to-best-comparacao-{D_DIMENSIONS}d-{GEN_MAX}r-v2.png')