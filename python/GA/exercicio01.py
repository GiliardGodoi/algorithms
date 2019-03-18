from random import randint
from random import random

Z = 52

def f(x,y,w):
    return (x**2 + 2*y + w)

def fitness(gene):
    x,y,w = translate_gene(gene)

    return abs((Z - f(x,y,w)))

# binary = bin(5) # 0b101
# integer = int(binary,2)
def bit2number(bitString):

    tmp = [ base * (2**int(indice)) for indice,base in enumerate( map(int,bitString[::-1])) ]
    return sum(tmp)

def translate_gene(gene,gene_size=9):
    if not gene_size == len(gene):
        return
    
    x_ = bit2number(gene[:3])
    y_ = bit2number(gene[3:6])
    w_ = bit2number(gene[6:])

    return x_,y_,w_


def generate_random_population(size):

    population = list()

    for _ in range(0,size):
        gene = [randint(0,1) for _ in range(0,9)]
        population.append(gene)
    
    return population

def crossing_genes(gene1, gene2):
    chop1, chop2 = cutting_points()

    newGeneOne = gene1[:chop1] + gene2[chop1:chop2] + gene1[chop2:]
    newGeneTwo = gene2[:chop1] + gene1[chop1:chop2] + gene2[chop2:]

    return newGeneOne, newGeneTwo


 
def cutting_points():
    geneSize = 9
    chop1 = randint(1,geneSize)
    chop2 = randint(1,geneSize)
    if chop1 > chop2 :
        chop1, chop2 = chop2, chop1
    elif chop1 == chop2 :
        chop1, chop2 = cutting_points()

    return chop1, chop2


def selection():
    pass

def crossover():
    pass

def mutation(gene, probability=0.1):
    
    for i,g in enumerate(gene):
        p = random() 
        if p < probability:
            # print('indice: ',i)
            gene[i] = 1 if g == 0 else 0
    
    return gene


if __name__ == "__main__":
    print('Starting GA algorithm')

    population = generate_random_population(20)

    for p in population :
        fit = fitness(p)
        print(fit, '  <-  ', p)
