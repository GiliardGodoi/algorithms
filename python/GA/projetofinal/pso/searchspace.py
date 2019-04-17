import numpy as np

from pso.particle import Particle
from pso.updateposition import DefaultPositionUpdate, AverageVelocityBased
from pso.updatevelocity import DefaultVelocityUpdate, LinearReduction, ConstrictionFactor

class SearchSpace():

    def __init__(self,
            costFunction,
            nroParticles,
            maxIteration,
            dimensions,
            bounds,
            **kwargs
        ):
        # assegurando o passagem do tipo de dado certo
        assert type(nroParticles) is int
        assert type(maxIteration) is int
        assert type(dimensions) is int
        assert callable(costFunction), "costFunction precisa ser uma função"
        assert type(bounds) is list

        # somente atribuição de variáveis passadas para o construtor
        self.costFunction = costFunction
        self.NroParticles = nroParticles
        self.MaxIteration = maxIteration
        self.dimensions = dimensions
        self.bounds = bounds
        self.velocityStrategyName = kwargs.get("velocityStrategy","default")
        self.positionStrategyName = kwargs.get("positionStrategy","default")
        
        # somente declaração de variáveis
        self.is_setup = False
        self.gbest = None
        self.particles = None
        self.velocityUpdateStrategy = None
        self.positionUpdateStrategy = None


    def setup(self):
        self.initialize_particles()
        self.velocityUpdateStrategy = self.__define_velocityUpdadeStrategy(self.velocityStrategyName)
        self.positionUpdateStrategy = self.__define_positionUpdateStrategy(self.positionStrategyName)
        
        self.is_setup = True
    
    def set_updateStrategiesParams(self,**kwargs):
        if kwargs.get('c1'): 
            self._C1 = kwargs.get('c1')
        if kwargs.get('c2'):
            self._C2 = kwargs.get('c2')
        if kwargs.get('c3'):
             self._C3 = kwargs.get('c3')
        if kwargs.get('w'):
            self._W = kwargs.get('w')
        if kwargs.get('w_min'):
            self._W_MIN = kwargs.get('w_min')
        if kwargs.get('w_max'):
            self._W_MAX = kwargs.get('w_max')
        if kwargs.get('kappa'):
            self._KAPPA = kwargs.get('kappa')

        if self.is_setup :
            self.is_setup = False

    def __define_velocityUpdadeStrategy(self,strategy="default"):
        strategy = strategy.upper()
        print(f'Velocity Update Strategy: {strategy}',end='\n')
        if strategy == "CONSTRICTION":
            return ConstrictionFactor(c1=self._C1,c2=self._C2,kappa=self._KAPPA)
        elif strategy == "LINEAR":
            return LinearReduction(w_min=self._W_MIN,w_max=self._W_MAX,c1=self._C1,c2=self._C2,max_iteration=self.MaxIteration)
        else :
            return DefaultVelocityUpdate(c1=self._C1,c2=self._C2,w=self._W)

    def __define_positionUpdateStrategy(self,strategy="default"):
        strategy = strategy.upper()
        print(f'Position Update Strategy: {strategy}',end='\n')
        if strategy == "AVG_VELOCITY":
            return AverageVelocityBased(c3=self._C3)
        else:
            return DefaultPositionUpdate()


    def initialize_particles(self):
        
        bounds = self.bounds
        del self.particles
        self.particles = list() # lista temporária
        self.gbest = None

        for _ in range(0,self.NroParticles):
            position = np.random.uniform(*bounds,size=self.dimensions)
            velocity = np.zeros(shape=self.dimensions)
            self.particles.append(Particle(position,velocity))
            if (self.gbest is None) or (self.fitness(position) < self.fitness(self.gbest)):
                self.gbest = position

    def __update_particle(self,particle,**kwargs):
        iteration = kwargs.get('iteration')

        self.positionUpdateStrategy.update(particle)
        self.velocityUpdateStrategy.update(particle,self.gbest,iteration=iteration)

        lower_b = self.bounds[0]
        upper_b = self.bounds[1]

        np.place(particle.position, particle.position > upper_b, upper_b)
        np.place(particle.position, particle.position < lower_b, lower_b)

    def get_gbest(self):
        return self.gbest

    def fitness(self,position):
        return self.costFunction(position)

    def run(self):
        if not self.is_setup:
            self.setup()

        iteration = 0

        while iteration < self.MaxIteration:
            # print(f'Iteration: {iteration}',end='\r')
            for p in self.particles:
                if self.fitness(p.position) < self.fitness(p.pbest_position) :
                    p.pbest_position = p.position

                    if (self.fitness(p.position) < self.fitness(self.gbest)):
                        self.gbest = p.position
            
            for p in self.particles:
                self.__update_particle(p,iteration=iteration)

            iteration += 1