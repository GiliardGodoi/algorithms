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
        real = convert2real(binario2number(seq),len(seq))
        variables.append(real)

    return tuple(variables)


def dejong_function(variables):
    powered = [pow(x,2) for x in variables]
    return sum(powered)

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
        old_chromo1 = old_p1.get('chromosome',None)
        old_chromo2 = old_p2.get('chromosome',None)
        
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
    return selection_by_contest(population) 
    # return selection_by_roulette_wheel(population)

def selection_by_contest(population):
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
        choosed = sorted(choosed,key=lambda item : item['fitness'],reverse=True) # coloca em ordem decrescente
        selected.append(choosed[0]) # seleciona sempre o com o maior fitness

    return selected

def selection_by_roulette_wheel(population):
    
    sumFitness = sum([c['fitness'] for c in population ])
    new_population = list()
    for _ in population:
        selected_chromosome = spin_the_wheel(population,sumFitness)
        new_population.append(selected_chromosome)
    return new_population

def spin_the_wheel(population,totalFitness):
    p = random.uniform(0,totalFitness)
    for chromo in population:
        if p <= 0:
            break
        p -= chromo['fitness']

    return chromo

def elitsm(new_population, old_population):
    size = len(old_population)
    return sorted((new_population + old_population),key=lambda item : item['fitness'],reverse=True)[:size]

def print_out(population):
    for p in population:
        print('{}   {:.5f}'.format(p['chromosome'],p['fitness']))


if __name__ == "__main__":
    print('De Jong Benchmark\n')

    populationSize = 100
    iteration = 0
    MAX_REPEAT = 1000


    population = generate_random_population(populationSize)
    population = sorted(population,key=lambda item : item['fitness'])
    print_out(population)

    while iteration < MAX_REPEAT:
        # print("Iteration  ::", (iteration + 1))
        population = sorted(population,key=lambda item : item['fitness'],reverse=True)
        selected = selection(population)
        population = elitsm(crossover(selected),population)
        iteration += 1


    print("\n\n\n")
    population = sorted(population,key=lambda item : item['fitness'])
    print_out(population)
    print(decode_chromosome(population[len(population)-1]['chromosome']))
        



