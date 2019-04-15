import numpy as np
from pso import SearchSpace
from util.benchmarks import dejong_sphere
from util.benchmarks import quadratic_noise
from util.benchmarks import rastrigin_function
from util.benchmarks import griewank_function

if __name__ == "__main__":
    
    pso = SearchSpace(costFunction=dejong_sphere,
                        nroParticles=100,
                        maxIteration=1000,
                        dimensions=10,
                        bounds=[-5.12,5.12],
                        velocityStrategy="CONSTRICTION",
                    )

    pso.set_updateStrategiesParams(c1=2.05,c2=2.05,c3=0.5,kappa=1,w=0.5,w_min=0.4,w_max=0.9)
    
    pso.run()

    print(pso.get_gbest())
    print('\n\n')
    gebest1 = pso.fitness(pso.gbest)
    print(gebest1)

    pso.initialize_particles()
    # pso.set_updateStrategiesParams(c1=2.05,c2=2.05,c3=0.5,kappa=1,w=0.5,w_min=0.4,w_max=0.9)
    pso.run()

    print(pso.get_gbest())
    print('\n\n')
    gebest2 = pso.fitness(pso.gbest)
    print(gebest2)