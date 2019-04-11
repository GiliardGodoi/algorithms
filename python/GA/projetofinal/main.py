import numpy as np
from pso import SearchSpace
from util.benchmarks import dejong_sphere
from util.benchmarks import quadratic_noise
from util.benchmarks import rastrigin_function
from util.benchmarks import griewank_function

if __name__ == "__main__":
    
    pso = SearchSpace(griewank_function,100,1000,10,[-100,100])

    pso.run()

    print(pso.get_gbest())
    print('\n\n')
    print(pso.fitness(pso.gbest))
