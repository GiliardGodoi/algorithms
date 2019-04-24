from pso import SearchSpace
from util.benchmarks import dejong_sphere

pso = SearchSpace(costFunction=dejong_sphere,
                    nroParticles=50,
                    maxIteration=10000,
                    dimensions=50,
                    bounds=[-5.12,5.12],
                )

# x = 1.4645669291338583
# y = -0.6141732283464567
# z = -0.6141732283464567

# x,y,z = 1.653543307086614, -0.6141732283464567, -1.1811023622047245
# x,y,z = 1.5,1.5,0.5
x, y, z = 1.8740157480314958, 1.84251968503937, -1.779527559055118

pso.set_updateStrategiesParams(c1=x,c2=y,w=z)
pso.setup()
pso.initialize_particles()
pso.run()

print(pso.get_gbest())
print(dejong_sphere(pso.get_gbest()))