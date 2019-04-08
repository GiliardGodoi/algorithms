import random
from logger import Logger

Z_OBJETIVO = 52
arraybit_lenght = 7 # array's size to represent a only variable (X or Y or Z)
QTD_VARIABLES = 3 # quantidade de variáveis na função objetivo (x,y,w) 3

def function(x,y,w):
    return (x**2 + 2*y + w)

def bit2number(bitString):
    return int(bitString,2)

def number2bit(number):
    return bin(number)[2:]

def decode_chromo(chromosome,lenght=arraybit_lenght):
    seq_chromo = [chromosome[i:(i+lenght)] for i in range(0,len(chromosome),lenght) ]
    mapNumbers = map(bit2number,seq_chromo)
    return tuple(mapNumbers)

def fitness(chromosome):
    return abs(Z_OBJETIVO - function(*decode_chromo(chromosome)))

def random_chromosome(size=0):
    tmp = [ random.choice(['0','1']) for _ in range(0,size) ]
    return ''.join(tmp)

def random_population(size):
    population = list()
    i = 0
    while i < size:
        chromo = dict()
        chromo['chromosome'] = random_chromosome((arraybit_lenght * QTD_VARIABLES))
        chromo['fitness'] = fitness(chromo['chromosome'])
        population.append(chromo)
        i += 1

    return population


def mutation(chromosome):
    # return __mutation_1(chromosome)
    return __mutation_2(chromosome)

def __mutation_1(chromosome,probability=0.1):
    p = random.random()
    if p > probability :
        return chromosome # It don't apply mutation

    change_bit = lambda bit : '1' if bit == '0' else '0'

    index = random.randrange(0,len(chromosome))
    chromo = list(chromosome)
    chromo[index] = change_bit(chromo[index])

    return ''.join(chromo)

def __mutation_2(chromosome,probability=0.1):
    chromo = list(chromosome)
    change_bit = lambda bit : '1' if bit == '0' else '0'

    for i in range(0,len(chromosome)):
        p = random.random()
        if p <= probability:
            chromo[i] = change_bit(chromo[i])

    return ''.join(chromo)


def cutting_points(chromosize):
    chop1 = random.randint(0,chromosize)
    chop2 = random.randint(0,chromosize)

    return min(chop1,chop2),max(chop1,chop2)

def crossing_chromosome(chromo1, chromo2):
    idx1, idx2 = cutting_points((arraybit_lenght * QTD_VARIABLES))

    newOne = chromo1[:idx1] + chromo2[idx1:idx2] + chromo1[idx2:]
    newTwo = chromo2[:idx1] + chromo1[idx1:idx2] + chromo2[idx2:]

    return newOne,newTwo

def crossover(population):
    new_population = list()
    size = len(population)
    i = 0

    _build_chromo = lambda x : {'chromosome' : x, 'fitness' : fitness(x)}
    __get = lambda x : x['chromosome']

    while i < size:
        c1, c2 = random.sample(population,k=2)
        chromo1, chromo2 = crossing_chromosome(__get(c1),__get(c2))
        chromo1, chromo2 = mutation(chromo1), mutation(chromo2)
        new_population.append(_build_chromo(chromo1))
        new_population.append(_build_chromo(chromo2))
        i += 2

    return new_population[:size] #guarantee the population's size

def select_by_wheel(population,totalFitness):
    p = random.uniform(0,totalFitness)
    for individual in population :
        p -= individual['fitness']
        if p <= 0:
            break

    return individual

def selection(population):
    totalFitness = sum([p['fitness'] for p in population])

    new_population = list()
    size = len(population)
    i = 0
    while i < size:
        new_population.append(select_by_wheel(population,totalFitness))
        i += 1

    return new_population

def normalize(population): 
    return __by_ranking(population)
    # return __by_windowing(population,value)

def __by_ranking(population):
    K = 2 * len(population) # K = sum(map(lambda i: i['fitness'],population),0)
    delta = 10 # delta = int(K/len(population))
    population = sorted(population,key=lambda item : item['fitness'],reverse=False)
    population[0]['fitness'] = K
    for i in range(1,len(population)):
        population[i]['fitness'] = (population[(i-1)]['fitness'] - delta)

    return population

def __by_windowing(population):
    value = max([p['fitness'] for p in population]) + 1

    for p in population:
        p['fitness'] = abs(value - p['fitness'])

    return population

def __by_sigma_scaling(population):
    pass

def isSolved(population):
    # return any([p['fitness'] == 0 for p in population])
    return False

def print_out(population):
    for p in population : print(p['chromosome'],p['fitness'])

std = Logger()

def main(populationSize=50,max_repeat=150):
  
    nroGeneration = 0 # iteration's number
    population = random_population(populationSize)
    sorted_pop = lambda population : sorted(population,key=lambda item : item['fitness'])

    while (nroGeneration < max_repeat) and (not isSolved(population)) :
        population = sorted_pop(population)
        population = normalize(population)
        selected = selection(population)
        population = crossover(selected)
        std.logger([p['fitness'] for p in population])
        nroGeneration += 1
    
    population = sorted_pop(population)
    
    return population


if __name__ == "__main__":
    
    population = main(populationSize=50,max_repeat=150)
    data = std.get_statistics_data()
    std.draw_chart()

    print_out(population)
    
    