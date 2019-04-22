import numpy as np

from pso.particle import Particle

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
        
        # somente declaração de variáveis
        self.is_setup = False
        self.gbest = None
        self.particles = None


    def setup(self):
        
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

    def fitness(self,particle):
        return self.costFunction(particle.position)

    def run(self):
        if not self.is_setup:
            self.setup()

        iteration = 0

        while iteration < self.MaxIteration:
            # print(f'Iteration: {iteration}',end='\r')
            for p in self.particles:
                self.updateVelocity(p,self.gbest.position)
                self.updatePosition(p)
                self.fitness(p)

            for p in self.particles:
                if self.fitness(p.position) < self.fitness(p.pbest_position) :
                    p.pbest_position = p.position

                    if (self.fitness(p.position) < self.fitness(self.gbest)):
                        self.gbest = p.position
            

            iteration += 1

    def updatePosition(self,particle):
        particle.position =  np.add(particle.velocity,particle.position)

    def updateVelocity(self,particle,gbest):
        position = particle.position
        velocity = particle.velocity
        pbest = particle.pbest_position

        r1 = np.random.uniform(0,1,size=len(position))
        r2 = np.random.uniform(0,1,size=len(position))

        w = self._W
        c1 = self._C1
        c2 = self._C2

         ## cognitive = c1 * r1 * (pbest - position)
        cognitive = np.multiply(c1,r1,np.subtract(pbest,position),dtype=np.float64)
        ## social = c2 * r2 * (gbest - position)
        social = np.multiply(c2,r2,np.subtract(gbest,position),dtype=np.float64)

        ##particle.velocity = w * velocity + cognitive + social
        particle.velocity = np.add(np.multiply(w,velocity),cognitive,social,dtype=np.float64)