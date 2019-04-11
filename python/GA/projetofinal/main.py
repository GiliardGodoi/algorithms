import numpy as np
from pso import SearchSpace
from util.benchmarks import dejong_sphere

if __name__ == "__main__":
    
    pso = SearchSpace(dejong_sphere,100,1000,20,[-5,5])

    pso.run()

    print(pso.get_gbest())
    print('\n\n')
    print(pso.fitness(pso.gbest))

