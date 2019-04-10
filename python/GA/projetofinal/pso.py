import numpy as np

from particle import Particle

class SearchSpace():

    def __init__(self,costFunction,nroParticles,maxIteration,dimensions,bounds):
        assert type(nroParticles) is int
        assert type(maxIteration) is int
        assert type(dimensions) is int
        assert callable(costFunction), "costFunction precisa ser uma função"

        self.NroParticles = nroParticles
        self.MaxIteration = maxIteration
        self.bounds = bounds
        self.dimensions = dimensions
        self.costFunction = costFunction
        
        self.gbest = None
        self.particles = self.__generate_particles()


    def __generate_particles(self):
        
        bounds = self.bounds
        tmp = list()

        for _ in range(0,self.NroParticles):
            position = np.random.uniform(*bounds,size=self.dimensions)
            velocity = np.zeros(shape=self.dimensions)
            tmp.append(Particle(position,velocity))
            if (self.gbest is None) or (self.fitness(position) < self.fitness(self.gbest)):
                self.gbest = position
        
        return tmp

    
    def get_gbest(self):
        return self.gbest

    def fitness(self,position):
        return self.costFunction(position)

    def run(self):

        iteration = 0

        while iteration < self.MaxIteration:
            for p in self.particles:
                if self.fitness(p.position) < self.fitness(p.pbest_position) :
                    p.pbest_position = p.position

                    if (self.fitness(p.position) < self.fitness(self.gbest)):
                        self.gbest = p.position
            
            for p in self.particles:
                p.update_velocity(self.gbest,w=0.8,c1=1,c2=1)
                p.update_position()

            iteration += 1


if __name__ == "__main__":
    
    def dejong_sphere(variables):
        return sum(map(lambda i: pow(i,2),variables))

    def quadratic_random():
        rand = np.random.rand
        zeta = lambda nro: pow(nro,4) + rand()

        def core_funtion(variables):
            return sum(map(zeta,variables))
        
        return core_funtion

    def cosine_complicate():
        
        zeta = lambda x: pow(x,2) - 10*np.cos(2*np.pi*x) + 10
        
        def core(variables):
            return sum(map(zeta,variables))

        return core

    def other_complicate():
        const = 1/4000
        zeta = lambda i,x: i*pow(x,2)
        beta = lambda i,x: np.cos(x/np.sqrt(i)) + 1

        def core(variables):
            
            _x = [zeta(i+1,x) for i,x in enumerate(variables)]
            _y = [beta(i+1,x) for i,x in enumerate(variables)]

            return const * np.sum(_x) + np.prod(_y)

        return core

    pso = SearchSpace(cosine_complicate(),100,1000,20,[-5,5])

    pso.run()

    print(pso.get_gbest())
    print('\n\n')
    print(pso.fitness(pso.gbest))