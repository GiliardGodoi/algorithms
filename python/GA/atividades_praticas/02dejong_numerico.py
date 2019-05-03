import random

def dejong_function(variables):
    return sum([pow(x,2) for x in variables ])

def fitness(chromosome,auxiliary=100):
    variables = chromosome # neste caso o cromossomo representa diretamente as variáveis de interesse
    return auxiliary / (dejong_function(variables) + auxiliary)

def random_chromosome(length,limUnder,limUpper):
    return [ random.uniform(limUnder,limUpper) for _ in range(0, length)]

def random_population(population_size=10,chromosome_size=3,limUnder=0,limUpper=1):
    population = list()
    for _ in range(0,population_size):
        chromo = dict()
        chromo['chromosome'] = random_chromosome(length=chromosome_size,limUnder=limUnder,limUpper=limUpper)
        chromo['fitness'] = fitness(chromo['chromosome'])
        population.append(chromo)

    return population

def crossover(population,roundedBy=10):
    new_population = list()
    size_population = len(population)

    for _ in range(0,size_population):
        p1,p2 = random.sample(population,k=2)
    
        chromo1,chromo2 = crossing_cromosome(p1,p2)

        chromo1 = mutation(chromo1)
        chromo2 = mutation(chromo2)

        new_chromo = dict()
        new_chromo['chromosome'] = chromo1 if fitness(chromo1) >= fitness(chromo2) else chromo2
        new_chromo['chromosome'] = [ round(nro,roundedBy) for nro in new_chromo['chromosome'] ]
        new_chromo['fitness'] = fitness(new_chromo['chromosome'])

        new_population.append(new_chromo)

    return new_population

def crossing_cromosome(indv_1, indv_2):
    chromo1, chromo2 = indv_1['chromosome'],indv_2['chromosome']
#    return crossing_parametric(chromo1,chromo2)
#    return crossing_discrete(chromo1, chromo2)
    return crossing_flat(chromo1,chromo2)
     
def crossing_discrete(chromo1,chromo2,probability=0.3):
    new_chromo1 = list()
    new_chromo2 = list()

    for i,j in zip(chromo1,chromo2):
        if random.random() < probability :
            new_chromo1.append(j)
            new_chromo2.append(i)
        else :
            new_chromo1.append(i)
            new_chromo2.append(j)

    return new_chromo1,new_chromo2

def crossing_parametric(chromo1,chromo2):
    delta = random.random()
    zeta = lambda x, y : (delta *  x) + (1 - delta) * y

    new_chromo1 = list()
    new_chromo2 = list()

    for c1,c2 in zip(chromo1,chromo2):
        new_chromo1.append(zeta(c1,c2))
        new_chromo2.append(zeta(c2,c1))

    return new_chromo1,new_chromo2

def crossing_flat(chromo1,chromo2):

    uniform = lambda x, y : random.uniform(x,y)

    new_chromo1 = list()
    new_chromo2 = list()

    for c1, c2 in zip(chromo1,chromo2):
        new_chromo1.append(uniform(c1,c2))
        new_chromo2.append(uniform(c1,c2))

    return new_chromo1,new_chromo2


def mutation(chromosome):
    return mutation_simple_random(chromosome)


def mutation_simple_random(chromosome,limUnder=-5.12,limUpper=5.12,probability=0.2):
    for i in range(0,len(chromosome)):
        if random.random() <= probability:
            chromosome[i] = random.uniform(limUnder,limUpper)

    return chromosome


def selection(population):
    return selection_by_wheel(sorted(population,key=lambda item: item['fitness']))
#    return selection_by_contest(sorted(population,key=lambda item: item['fitness']))

def selection_by_wheel(population):

    fitnessSum = sum([i['fitness'] for i in population])
    new_population = list()
    i = 0
    while i < len(population):
        new_population.append(spinning_the_wheel(population,fitnessSum))
        i += 1

    return new_population

def spinning_the_wheel(population,totalFitness):
    r = random.uniform(0,totalFitness)
    for individual in population:
        r -= individual['fitness']
        if r < 0 : 
            break

    return individual

def selection_by_contest(population): 
    new_population = list()
    for _ in population:
        c1, c2 = random.sample(population,k=2)
        new_chromo = c1 if c1.get("fitness") >= c2.get("fitness") else c2
        new_population.append(new_chromo)

    return new_population

def elitsm(new_population,old_population):
    size = len(old_population)
    return sorted((new_population + old_population),key=lambda item : item['fitness'],reverse=True)[:size]

def print_out(population):
    for p in population:
        print('{}   {:.5f}'.format(p['chromosome'][:3],p['fitness']))

# if __name__ == "__main__":
#     print('De Jong Benchmark\t... a \'real\' implementation :P\n\n')
#     from visualization import line_plot

#     populationSize = 100 
#     iteration = 0
#     MAX_REPEAT = 1000
#     N_dimensions = 10
#     rounderNumber = 3
#     X_inf, X_sup = -5.12, 5.12
    

#     rodada, MAX_RODADA = 0, 100
#     historico_melhor_fitness = list()
#     historico_media_fitness = list()

#     while rodada < MAX_RODADA:
#         population = random_population(population_size=populationSize,
#                                         chromosome_size=N_dimensions,
#                                         limUnder=X_inf,
#                                         limUpper=X_sup
#                                         )

#         # print_out(population)
#         # print("\n\n\n")
#         iteration = 0
#         while (iteration < MAX_REPEAT):
#             print(f'Iteration: {iteration}',end='\r')
#             selected = selection(population)
#             population = crossover(selected)
#     #        new_population = crossover(selected,roundedBy=rounderNumber)
#     #        population = elitsm(new_population,population)
#             iteration += 1

#         rodada += 1

#         population = sorted(population,key=lambda item: item['fitness'],reverse=True)
#         print(population[0])
#         historico_melhor_fitness.append(population[0]['fitness'])



#     line_plot(data=historico_melhor_fitness,
#                 _x=range(0,len(historico_melhor_fitness)),
#                 _y=lambda y: y,
#                 xlabel="Repetições do algoritmo",
#                 ylabel="Melhor Fitness alcançado",
#                 title="Histórico melhor fitness",
#                 outpu_file="historico-melhor-fitness.png"
#             )

if __name__ == "__main__":
    print('De Jong Benchmark\t... a \'real\' implementation :P\n\n')
    from visualization import line_plot

    populationSize = 100
    iteration = 0
    MAX_REPEAT = 1000
    N_dimensions = 10
    rounderNumber = 3
    X_inf, X_sup = -5.12, 5.12
    

    rodada, MAX_RODADA = 0, 100
    # MANTEM O HISTÓRICO PARA TODAS AS RODADAS
    historico_fitness_geracao = list()  # Ma
    historico_melhor_fitness = list() # Mantém os dados do melhor fitness ao final de uma rodada
    historico_media_fitness = list() # Mantem o dados da média do fitness
    calcula_media = lambda x : sum(x) / len(x)

    while rodada < MAX_RODADA:
        population = random_population(population_size=populationSize,
                                        chromosome_size=N_dimensions,
                                        limUnder=X_inf,
                                        limUpper=X_sup
                                        )

        # print_out(population)
        # print("\n\n\n")
        iteration = 0
        media_geracao_rodada = list()
        fitness_geracao = list()
        while (iteration < MAX_REPEAT):
            print(f'Iteration: {iteration}',end='\r')
            aptidao = [ dejong_function(p['chromosome']) for p in population]
            historico_fitness_geracao.append(aptidao)
            media_geracao_rodada.append(calcula_media([ p['fitness'] for p in population]))
            selected = selection(population)
            population = crossover(selected)
    #        new_population = crossover(selected,roundedBy=rounderNumber)
    #        population = elitsm(new_population,population)
            iteration += 1

        rodada += 1

        historico_media_fitness.append(media_geracao_rodada)

        population = sorted(population,key=lambda item: item['fitness'],reverse=True)
        print(population[0])
        historico_melhor_fitness.append(population[0])

    line_plot(data=historico_melhor_fitness,
                _x=range(0,len(historico_melhor_fitness)),
                _y=lambda y: y['fitness'],
                xlabel="Repetições do algoritmo",
                ylabel="Melhor Fitness alcançado",
                ylim=(0.95,1),
                title="Histórico melhor fitness",
                output_file="exercicio02-historico-melhor-fitness.png"
            )

    ax1 = line_plot(data=historico_media_fitness[5],
                _x=range(0,len(historico_media_fitness[0])),
                _y=lambda y: y,
                xlabel="Gerações",
                ylabel="Média do fitness",
                title="Média do fitness por geração",
                output_file="exercicio02-media-fitness-por-geracao.png"
            )