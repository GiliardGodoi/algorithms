from genetic.ga_binary import random_population, mutation, crossover, selection, normalize

def bit2number(bitString):
    return int(bitString,2)

def decode_chromo(chromosome,lenght):
    sequel = [chromosome[i:(i+lenght)] for i in range(0,len(chromosome),lenght) ]
    mapNumbers = map(bit2number,sequel)
    return tuple(mapNumbers)

def function(x,y,w):
    return (x**2 + 2*y + w)

def fitness(chromosome,lenght,Z_target):
    return abs(Z_target - function(*decode_chromo(chromosome,lenght)))

if __name__ == "__main__":
    POPULATION_SIZE = 100
    SUB_LENGHT = 7
    QTD_VARIABLES = 3 # X, Y, Z
    OBJETIVO = 52
    MAX_REPEAT = 2000

    def evaluate_population(population):
        for chromosome in population:
            chromosome.score = fitness(chromosome.genes,SUB_LENGHT,OBJETIVO)

        return population

    def sort_population(population,reversed=False):
        return sorted(population,key=lambda item : item.score, reverse=reversed)

    generation = 0

    population = random_population(sizePopulation=POPULATION_SIZE,sizeChromosome=(SUB_LENGHT * QTD_VARIABLES))

    while generation < MAX_REPEAT:
        population = evaluate_population(population)
        population = sort_population(population)
        population = normalize(population)
        selected = selection(population)
        population = crossover(selected)
        generation += 1

    population = evaluate_population(population)
    population = sort_population(population)

    for p in population: print(p.score)

