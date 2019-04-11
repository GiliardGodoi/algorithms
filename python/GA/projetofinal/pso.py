import numpy as np

from particle import Particle
from updateposition import DefaultPositionUpdate
from updateposition import AverageVelocityBased
from updatevelocity import DefaultVelocityUpdate
from updatevelocity import LinearReduction
from updatevelocity import ConstrictionFactor

class SearchSpace():

    def __init__(self,
            costFunction,
            nroParticles,
            maxIteration,
            dimensions,
            bounds
        ):
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
        self.is_setup = False
        self.gbest = None
        self.particles = None
        self.velocityUpdateStrategy = None
        self.positionUpdateStrategy = None

        self.__setup()

    def __setup(self):
        self.particles = self.__generate_particles()
        self.velocityUpdateStrategy = self.__define_velocityUpdadeStrategy("LINEAR")
        self.positionUpdateStrategy = self.__define_positionUpdateStrategy("AVG_VELOCITY")

        self.is_setup = True
    
    def __define_velocityUpdadeStrategy(self,strategy="default"):
        strategy = strategy.upper()
        print(f'Velocity Update Strategy: {strategy}')
        if strategy is "CONSTRICTION":
            return ConstrictionFactor()
        elif strategy is "LINEAR":
            return LinearReduction(max_iterarion=self.MaxIteration,w_max=10,w_min=-10)
        else :
            return DefaultVelocityUpdate()

    def __define_positionUpdateStrategy(self,strategy="default"):
        strategy = strategy.upper()
        print(f'Position Update Strategy: {strategy}')
        if strategy is "AVG_VELOCITY":
            return AverageVelocityBased()
        else:
            return DefaultPositionUpdate()


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

    def __update_particle(self,particle,**kwargs):
        iteration = kwargs.get('iteration')

        self.positionUpdateStrategy.update(particle)
        self.velocityUpdateStrategy.update(particle,self.gbest,w=0.5,c1=1,c2=1,c3=1,iteration=iteration)

        lower_b = self.bounds[0]
        upper_b = self.bounds[1]

        np.place(particle.position, particle.position > upper_b, upper_b)
        np.place(particle.position, particle.position < lower_b, lower_b)

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
                self.__update_particle(p,iteration=iteration)

            iteration += 1