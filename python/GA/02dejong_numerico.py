import random
from functools import reduce

N_dimensions = 5
X_inf = -5.12
X_sup = 5.12

def dejong_function(variables):
    mapped = map(lambda x: pow(x,2), variables)
    return sum(list(mapped))

def fitness(chromosome):
    variables = chromosome # neste caso o cromossomo representa diretamente as variáveis de interesse
    return 1 / (dejong_function(variables) + 1)

def random_chromosome(length=N_dimensions):    
    return [ random.uniform(X_inf,X_sup) for _ in range(0, length)]

def generate_random_population(population_size=10):
    population = list()
    for _ in range(0,population_size):
        chromo = dict()
        chromo['chromosome'] = random_chromosome()
        chromo['fitness'] = fitness(chromo['chromosome'])
        population.append(chromo)

    return population

def crossover(population):
    new_population = list()
    size_population = len(population)

    for _ in range(0,size_population):
        p1,p2 = random.sample(population,k=2)
        chromo1 = p1['chromosome']
        chromo2 = p2['chromosome']

        chromo1,chromo2 = crossing_cromosome(chromo1,chromo2)

        chromo1 = mutation(chromo1)
        chromo2 = mutation(chromo2)

        new_chromo = dict()
        new_chromo['chromosome'] = chromo1 if fitness(chromo1) >= fitness(chromo2) else chromo2
        new_chromo['fitness'] = fitness(new_chromo['chromosome'])

        new_population.append(new_chromo)

    return new_population

def crossing_cromosome(chromo1, chromo2):
    return crossing_uniform(chromo1, chromo2)

def crossing_uniform(chromo1,chromo2,probability=0.7): 
    size = 0
    if len(chromo1) == len(chromo2):
        size = len(chromo1)
    else:
        raise Exception("chromosomes have different size")

    new_chromo1 = list()
    new_chromo2 = list()

    for i in range(0,size):
        # binary = random.randint(0,1)
        binary = 1 if random.random() >= probability else 0
        if binary == 1 :
            new_chromo1.append(chromo2[i])
            new_chromo2.append(chromo1[i])
        else:
            new_chromo1.append(chromo1[i])
            new_chromo2.append(chromo2[i])

    return new_chromo1,new_chromo2

    

def mutation(chromosome):
    return mutation_simple_random(chromosome)


def mutation_simple_random(chromosome, probability=0.1):
    for i,_ in enumerate(chromosome) :
        p = random.random()
        if p <= probability:
            chromosome[i] = random.uniform(X_inf,X_sup)

    return chromosome


def selection(population):
    return selection_by_wheel(population)

def selection_by_wheel(population):
    '''
        roulette wheel selection (let's keep the things easy, though)
        thanks for the internet: https://stackoverflow.com/questions/177271/roulette-selection-in-genetic-algorithms
    '''
    fitnessSum = reduce(lambda x,y : x + y,[i['fitness'] for i in population])

    new_population = list()

    for _ in population :
        seleted_chromosome = spinning_the_wheel(population,fitnessSum)
        new_population.append(seleted_chromosome)

    return new_population


def spinning_the_wheel(population,totalFitness):
    p = random.uniform(0,totalFitness)
    for individual in population:
        if p <= 0 : 
            break
        p -= individual['fitness']

    return individual

def selection_by_contest(population): 
    pass

def evaluate(population):
    pass

def print_out(population):
    for p in population:
        print('{}   {:.5f}'.format(p['chromosome'][:3],p['fitness']))

if __name__ == "__main__":
    print('De Jong Benchmark\t... a \'real\' implementation :P\n\n')

    populationSize = 20
    iteration = 0
    MAX_REPEAT = 200

    population = generate_random_population(populationSize)

    while (iteration < MAX_REPEAT):
        population = sorted(population,key=lambda item: item['fitness'])
        # print('Iteration::  ', iteration)
        # print_out(population)

        selected = selection(population)
        population = crossover(selected)
        iteration += 1

    population = sorted(population,key=lambda item: item['fitness'])
    print('Iteration::  ', iteration)
    print_out(population)
        

