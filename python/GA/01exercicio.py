import random

Z = 52

def f(x,y,w):
    return (2 * x + y**2 + w)

def fitness(gene):
    x,y,w = translate_gene(gene)

    return abs((Z - f(x,y,w)))

# binary = bin(5) # 0b101
# integer = int(binary,2)
def bit2number(bitString):
    tmp = [ base * (2**int(indice)) for indice,base in enumerate( map(int,bitString[::-1])) ]
    return sum(tmp)
    # bitString = ''.join([str(i) for i in bitString])
    # return int(bitString,2)

def translate_gene(gene,gene_size=9):
    if not gene_size == len(gene):
        return
    
    x_ = bit2number(gene[:3])
    y_ = bit2number(gene[3:6])
    w_ = bit2number(gene[6:])

    return x_,y_,w_

def define_chromosome(size=9) :
    return [random.randint(0,1) for _ in range(0,size)]


def generate_random_population(size):

    population = list()

    for _ in range(0,size):
        chromo = dict()
        chromo['chromosome'] = define_chromosome(size=9)
        chromo['fitness'] = fitness(chromo['chromosome'])
        population.append(chromo)
    
    return population

def crossing_chromosome(chromosome_1, chromosome_2):
    chop1, chop2 = cutting_points()

    newChromosome_One = chromosome_1[:chop1] + chromosome_2[chop1:chop2] + chromosome_1[chop2:]
    newChromosome_Two = chromosome_2[:chop1] + chromosome_1[chop1:chop2] + chromosome_2[chop2:]

    return newChromosome_One, newChromosome_Two

 
def cutting_points():
    geneSize = 9
    chop1 = random.randint(1,geneSize)
    chop2 = random.randint(1,geneSize)
    if chop1 > chop2 :
        chop1, chop2 = chop2, chop1
    elif chop1 == chop2 :
        chop1, chop2 = cutting_points()

    return chop1, chop2


def selection(population):
    '''
        Seleção por torneio dos índividuos.
            - Seleciona dois índividuos da população e seleciona o com o menor fitness.
            - Repete o procedimento até ter uma população final de mesmo tamanho que a população individual.
    '''

    size = len(population) # ira selecionar a mesma quantidade da população inicial

    selected = list()

    for _ in range(0,size): 
        choosed = random.sample(population,k=2) # escolhe aleatoriamente dois elementos do conjunto
        choosed = sorted(choosed,key=lambda item : item['fitness']) # coloca em ordem crescente
        selected.append(choosed[0]) # seleciona sempre o com menor fitness

    return selected
    
def crossover(population):
    
    new_population = list()
    probability = 0.5

    for p1 in population:
        new_chromosome = dict()

        p2 = random.choice(population)
        chromo1, chromo2 = crossing_chromosome(p1['chromosome'],p2['chromosome'])
        new_chromosome['chromosome'] = chromo1 if probability <= random.random() else chromo2
        new_chromosome['chromosome'] = mutation(new_chromosome['chromosome'])
        new_chromosome['fitness'] = fitness(new_chromosome['chromosome'])

        new_population.append(new_chromosome)

    return new_population


def mutation(chromosome, probability=0.1):
    
    for i,g in enumerate(chromosome):
        p = random.random() 
        if p < probability:
            # print('indice: ',i)
            chromosome[i] = 1 if g == 0 else 0
    
    return chromosome

def evaluate(population):
    isSolved = True
    firstIndividual = population[0]
    
    if firstIndividual['fitness'] == 0:
        return isSolved
    else :
        return not isSolved

def print_population(population):
    for p in population: print(p['chromosome'],p['fitness'])

if __name__ == "__main__":
    print('Starting GA algorithm')

    populationSize = 20
    numberOfIteration = 0
    numberOfMaxIterarion = 26 # 

    population = generate_random_population(populationSize)

    while True:
        population = sorted(population,key=lambda item : item['fitness'] )
        
        print('Iteration:    ',(numberOfIteration + 1))
        print_population(population)

        # criterio de parada
        if ( evaluate(population) or (numberOfIteration >= numberOfMaxIterarion) ) :
            break

        selected = selection(population)
        population = crossover(selected)
        numberOfIteration += 1

    chromosome = population[0]
    numbers = translate_gene(chromosome['chromosome'])
    
    print('\n')
    print(numbers,'  ->  ',f(*numbers))
    print('\n')

    print_population([chromosome])