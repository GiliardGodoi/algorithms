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


def random_chromosome(length=chromo_length):
    tmp = [random.choice(['0','1']) for _ in range(0,length) ]
    return ''.join(tmp)

def generate_random_population(population_size=20):
    population = list()
    for _ in range(0,population_size):
        population.append(random_chromosome())
    
    return population

def cutting_points(length=chromo_length):
    points = random.sample(range(1,length),2)
    points.sort()
    return points

def crossover(chromo1, chromo2):
    i,j = cutting_points()
    new_chromo1 = chromo1.copy()
    new_chromo2 = chromo2.copy()

    new_chromo1[i:j],new_chromo2[i:j] = chromo2[i:j],chromo1[i:j]

    return new_chromo1,new_chromo2

def mutation(chormosome, probability=0.1):
    tmp = list()
    for g in chormosome:
        if random.random() <= probability:
            t = 1 if int(g) == 0 else 1
            tmp.append(t)
        else:
            tmp.append(g)

    return tmp

def selection():
    pass

    