from pso import SearchSpace
from util.benchmarks import quadratic_noise as fitness
from util.visualization import line_plot
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    pso = SearchSpace(costFunction=fitness,
                        nroParticles=50,
                        maxIteration=10000,
                        dimensions=50,
                        bounds=[-1.28,1.28],
                        positionStrategy="AVG_VELOCITY"
                    )

    pso.set_updateStrategiesParams(c1=0.1,c2=0.1,c3=-0.4,w=0.5)
    pso.setup() # Inicilaiza as particulas e as estratégias

    MAX_ITERATION =  2
    iteration = 0
    DATA = list()

    while iteration < MAX_ITERATION:
        print(f'Iteration: {iteration}', end='\r')
        pso.run()
        DATA.append(fitness(pso.get_gbest()))
        pso.initialize_particles()
        iteration += 1

    line_plot(data=DATA,
                _x=range(1,len(DATA)+1),
                title="G_best",
                xlabel="iteracao",
                ylabel="g_best fitness",
                output_file="simulacao.png"
            )

    print(DATA)
    print(np.mean(DATA))