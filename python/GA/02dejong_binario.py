import random

N_dimensions = 3
X_inf = -5.12
X_sup = 5.12
chromo_length = 15


def number2binario(number):
    return bin(number)[2:]

def binario2number(binario):
    return int(binario,2)

def convert2real(number,k_bits=3):
    delta = X_sup - X_inf
    bits_factor = pow(2,k_bits) - 1

    return X_inf + (delta/bits_factor) * number

def decode_chromosome(chromosome,dimensions=N_dimensions):
    
    lenght = len(chromosome) // dimensions

    variables = list()

    for i in range(0,len(chromosome), lenght):
        seq = chromosome[i:i+lenght]
        number = binario2number(seq)
        real = convert2real(number,len(seq))
        variables.append(real)

    return tuple(variables)


def dejong_function(variables):
    mapped = map(lambda x: pow(x,2), variables)
    return sum(list(mapped))

def fitness(chromosome):
    return 1 / (dejong_function(decode_chromosome(chromosome)) + 1)
    # return dejong_function(decode_chromosome(chromosome))

def random_chromosome(length=chromo_length):
    tmp = [random.choice(['0','1']) for _ in range(0,length) ]
    return ''.join(tmp)

def generate_random_population(population_size=20):
    population = list()
    
    for _ in range(0,population_size):
        chromo = dict()
        chromo['chromosome'] = random_chromosome()
        chromo['fitness'] = fitness(chromo['chromosome'])
        population.append(chromo)
    
    return population

def cutting_points(length=chromo_length):
    points = random.sample(range(1,length),2)
    points.sort()
    return points

def crossing_chromosome(chromo1, chromo2):
    i,j = cutting_points()
    
    new_chromo1 = (chromo1[:i] + chromo2[i:j] + chromo1[j:])
    new_chromo2 = (chromo2[:i] + chromo1[i:j] + chromo2[j:])

    return new_chromo1,new_chromo2

def mutation(chormosome, probability=0.1):
    tmp = list()
    for g in chormosome:
        if random.random() <= probability:
            t = "1" if int(g) == 0 else "0"
            tmp.append(t)
        else:
            tmp.append(g)

    return "".join(tmp)

def crossover(population):

    new_population = list()

    for _ in range(0,len(population),2):
        old_p1, old_p2 = random.sample(population,k=2)
        old_chromo1 = old_p1['chromosome']
        old_chromo2 = old_p2['chromosome']
        
        new_chromo1, new_chromo2 = crossing_chromosome(old_chromo1,old_chromo2)

        new_chromo1 = mutation(new_chromo1)
        new_chromo2 = mutation(new_chromo2)

        new_subject1 = dict()
        new_subject1['chromosome'] = new_chromo1
        new_subject1['fitness'] = fitness(new_chromo1)
        new_population.append(new_subject1)
        
        new_subject2 = dict()
        new_subject2['chromosome'] = new_chromo2
        new_subject2['fitness'] = fitness(new_chromo2)
        new_population.append(new_subject2)

    return new_population
    

def selection(population):
    '''
        Seleção por torneio dos índividuos.
            - Seleciona dois índividuos da população e seleciona o com o menor fitness.
            - Repete o procedimento até ter uma população final de mesmo tamanho que a população individual.
    '''
    selected = list()
    size = len(population) # ira selecionar a mesma quantidade da população inicial
    metade = (size // 2)
    for _ in range(0,size): 
        choosed = random.sample(population[:metade],k=2) # escolhe aleatoriamente dois elementos do conjunto
        choosed = sorted(choosed,key=lambda item : item['fitness']) # coloca em ordem crescente
        selected.append(choosed[0]) # seleciona sempre o com menor fitness

    return selected


def print_out(population):
    for p in population:
        print('{}   {:.5f}'.format(p['chromosome'],p['fitness']))


def evaluate(population):
    isSolved = True
    firstIndividual = population[0]
    
    if firstIndividual['fitness'] == 0:
        return isSolved
    else :
        return not isSolved


if __name__ == "__main__":
    print('De Jong Benchmark\n\n')

    populationSize = 20
    iteration = 0
    MAX_REPEAT = 200


    population = generate_random_population(populationSize)

    while True:
        print("Iteration  ::", (iteration + 1))
        
        population = sorted(population,
            key=lambda item : item['fitness'])
        print_out(population)

                # criterio de parada
        if ( evaluate(population) or (iteration >= MAX_REPEAT) ) :
            break

        selected = selection(population)
        population = crossover(selected)
        iteration += 1


    print("\n\n\n")
    print_out(population)
    print(decode_chromosome(population[0]['chromosome']))
        



