import numpy as np

from particle import Particle

class SearchSpace():

    def __init__(self,costFunction,nroParticles,maxIteration,dimensions,bounds):
        # assegurando o passagem do tipo de dado certo
        assert type(nroParticles) is int
        assert type(maxIteration) is int
        assert type(dimensions) is int
        assert callable(costFunction), "costFunction precisa ser uma função"
        assert type(bounds) is list

        # somente atribuição de variáveis passadas para o construtor
        self.NroParticles = nroParticles
        self.MaxIteration = maxIteration
        self.bounds = bounds
        self.dimensions = dimensions
        self.costFunction = costFunction
        
        # somente declaração de variáveis
        self.gbest = None
        self.particles = None

        self.__setup()

    def __setup(self):
        self.particles = self.__generate_particles()
    
    def __generate_particles(self):
        
        bounds = self.bounds
        tmp_particles = list() # lista temporária

        for _ in range(0,self.NroParticles):
            position = np.random.uniform(*bounds,size=self.dimensions)
            velocity = np.zeros(shape=self.dimensions)
            tmp_particles.append(Particle(position,velocity))
            if (self.gbest is None) or (self.fitness(position) < self.fitness(self.gbest)):
                self.gbest = position
        
        return tmp_particles

    
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