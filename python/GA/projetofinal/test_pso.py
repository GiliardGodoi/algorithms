import numpy as np
from pso import SearchSpace
from util.benchmarks import dejong_sphere as costFitness
# from util.benchmarks import quadratic_noise as costFitness
# from util.benchmarks import rastrigin_function as costFitness
# from util.benchmarks import griewank_function as costFitness
# import time

if __name__ == "__main__":
    
    pso = SearchSpace(costFunction=costFitness,
                        nroParticles=50,
                        maxIteration=2000,
                        dimensions=20,
                        bounds=[-5.12,5.12]
                    )

    pso.set_updateStrategiesParams(c1=1,c2=2,w=0.5)
    pso.initialize_particles()
    
    print(pso.gbest,pso.gbest.fitness)

    pso.run()

    print(pso.gbest,pso.gbest.fitness)


