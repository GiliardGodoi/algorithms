from genetic import Chromosome
import random

def random_binary_genes(size=0):
    tmp = [ random.choice(['0','1']) for _ in range(0,size) ]
    return ''.join(tmp)

def random_population(sizePopulation,sizeChromosome):
    population = list()
    i = 0
    while i < sizePopulation:
        genes = random_binary_genes(size=sizeChromosome)
        population.append(Chromosome(genes=genes))
        i += 1

    return population

## MUTATION operations

def mutation(chromosome,probability=0.1):
    flip_bit = lambda bit : '1' if bit == '0' else '0'
    genes = list(chromosome)

    for i in range(0,len(chromosome)):
        p = random.random()
        if p < probability:
            genes[i] = flip_bit(genes[i])

    return ''.join(genes)


## CROSSOVER operations

def cutting_points(sizeChromosome):
    chop1 = random.randint(0,sizeChromosome)
    chop2 = random.randint(0,sizeChromosome)

    return min(chop1,chop2),max(chop1,chop2)

def crossing_chromosome(chromo1, chromo2):
    
    idx1, idx2 = cutting_points(len(chromo1))

    newOne = chromo1[:idx1] + chromo2[idx1:idx2] + chromo1[idx2:]
    newTwo = chromo2[:idx1] + chromo1[idx1:idx2] + chromo2[idx2:]

    return newOne,newTwo

def crossover(population):
    new_population = list()
    size = len(population)
    i = 0

    while i < size:
        c1, c2 = random.sample(population,k=2)
        chromo1, chromo2 = crossing_chromosome(c1.genes,c2.genes)
        chromo1, chromo2 = mutation(chromo1), mutation(chromo2)
        new_population.append(Chromosome(chromo1))
        new_population.append(Chromosome(chromo2))
        i += 2

    return new_population[:size] #guarantee the population's size
            
## SELECTION operations

def select_by_wheel(population,totalFitness):
    p = random.uniform(0,totalFitness)
    for chromosome in population :
        p -= chromosome.fitness
        if p <= 0:
            break

    return chromosome

def selection(population):
    totalFitness = sum([chromosome.fitness for chromosome in population])

    new_population = list()
    size = len(population)
    i = 0
    while i < size:
        new_population.append(select_by_wheel(population,totalFitness))
        i += 1

    return new_population

## NORMALIZATION 

def normalize(population): 
    return normalize_by_windowing(population)

def normalize_by_ranking(population):
    K = 2 * len(population) # K = sum(map(lambda i: i['fitness'],population),0)
    delta = 2 # delta = int(K/len(population))
    population = sorted(population,key=lambda chromosome: chromosome.score ,reverse=False)
    population[0].fitness = K
    for chromosome in population:
        K = K - delta
        chromosome.fitness = K

    return population

def normalize_by_windowing(population):
    value = max([chromosome.score for chromosome in population]) + 1

    for chromosome in population:
        chromosome.fitness = abs(value - chromosome.score)

    return population