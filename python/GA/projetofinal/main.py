import numpy as np
from pso import SearchSpace
from util.benchmarks import dejong_sphere
from util.benchmarks import quadratic_noise
from util.benchmarks import rastrigin_function
from util.benchmarks import griewank_function

if __name__ == "__main__":
    
    pso = SearchSpace(costFunction=dejong_sphere,
                        nroParticles=100,
                        maxIteration=500,
                        dimensions=10,
                        bounds=[-5.12,5.12],
                        velocityStrategy="CONSTRICTION",
                        )

    pso.run()

    print(pso.get_gbest())
    print('\n\n')
    print(pso.fitness(pso.gbest))
