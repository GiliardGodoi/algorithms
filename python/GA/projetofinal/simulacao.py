from pso import SearchSpace
from util.benchmarks import rastrigin_noncontinuous as fitness
from util.visualization import line_plot
import matplotlib.pyplot as plt
import numpy as np
import time

if __name__ == "__main__":
    
    pso = SearchSpace(costFunction=fitness,
                        nroParticles=100,
                        maxIteration=1000,
                        dimensions=50,
                        bounds=[-1.28,1.28],
                        velocityStrategy="CONSTRICTION"
                    )

    pso.set_updateStrategiesParams(c1=2.05,c2=2.05,kappa=1,w=0.5)
    pso.setup() # Inicilaiza as particulas e as estratégias

    MAX_ITERATION =  5
    iteration = 0
    DATA = list()

    inicio = time.time()
    while iteration < MAX_ITERATION:
        pso.initialize_particles()
        print(f'Iteration: {iteration}', end='\r')
        pso.run()
        DATA.append(fitness(pso.get_gbest()))
        iteration += 1
    
    fim = time.time()

    line_plot(data=DATA,
                _x=range(1,len(DATA)+1),
                title="G_best",
                xlabel="iteracao",
                ylabel="g_best fitness",
                output_file="simulacao.png"
            )
    print(f'Tempo de Execução {(fim-inicio)}')
    print(DATA)
    print(np.mean(DATA))