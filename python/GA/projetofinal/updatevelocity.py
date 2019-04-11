import numpy as np

class VelocityUpdateStrategy():
    
    def update(self,particle,gbest,**kwargs):
        raise NotImplementedError()

class DefaultVelocityUpdate(VelocityUpdateStrategy):

    def update(self,particle,gbest,**kwargs):
        position = particle.position
        velocity = particle.velocity
        pbest = particle.pbest_position

        r1 = np.random.uniform(0,1,size=len(position))
        r2 = np.random.uniform(0,1,size=len(position))

        c1 = kwargs.get('c1')
        c2 = kwargs.get('c2')
        w = kwargs.get('w')

        cognitive = c1 * r1 * (pbest - position)
        social = c2 * r2 * (gbest - position)

        particle.velocity = w * velocity + cognitive + social
    

class ConstrictionFactor(VelocityUpdateStrategy):

    def update(self,particle,gbest,**kwargs):
        position = particle.position
        velocity = particle.velocity
        pbest = particle.pbest_position
        
        kappa = kwargs.get('kappa')
        phi = kwargs.get('phi')

        c1 = kwargs.get('c1')
        c2 = kwargs.get('c2')

        chi = (2 * kappa) / abs((2 - phi - np.sqrt(pow(phi,2) - 4 )))

        r1 = np.random.uniform(0,1,size=len(position))
        r2 = np.random.uniform(0,1,size=len(position))

        cognitive = c1 * r1 * (pbest - position)
        social = c2 * r2 * (gbest - position)

        particle.velocity = chi * (velocity + cognitive + social)


class LinearReduction(VelocityUpdateStrategy):

    def __init__(self,max_iterarion,w_max,w_min):
        assert type(max_iterarion) is int
        assert type(w_max) is int
        assert type(w_min) is int

        self.K_MAX = max_iterarion
        self.W_MAX = w_max
        self.W_MIN = w_min

    def update(self,particle,gbest,**kwargs):
        position = particle.position
        velocity = particle.velocity
        pbest = particle.pbest_position

        k_max = self.K_MAX
        w_max = self.W_MAX
        w_min = self.W_MIN

        k = kwargs.get('iterarion')
        c1 = kwargs.get('c1')
        c2 = kwargs.get('c2')

        W = w_max - (k * ( (w_max - w_min) / k_max)
)
        r1 = np.random.uniform(0,1,size=len(position))
        r2 = np.random.uniform(0,1,size=len(position))

        cognitive = c1 * r1 * (pbest - position)
        social = c2 * r2 * (gbest - position)

        position.velocity = W * velocity + cognitive + social