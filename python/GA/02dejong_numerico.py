import random

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

def crossing_cromosome(chromo1, chromo2):
    pass

def crossover(population):
    pass

def mutation(chromosome):
    pass

def selection(population):
    pass

def evaluate(population):
    pass

def print_out(population):
    for p in population:
        print('{}   {:.5f}'.format(p['chromosome'],p['fitness']))

if __name__ == "__main__":
    print('De Jong Benchmark\t... a real implementation\n\n')

    populationSize = 20
    iteration = 0
    MAX_REPEAT = 200

    population = generate_random_population(populationSize)

    print_out(population)
