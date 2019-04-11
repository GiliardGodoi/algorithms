import numpy as np

class VelocityUpdateStrategy():
    
    def update(self,particle,gbest,**kwargs):
        raise NotImplementedError()

class DefaultVelocityUpdate(VelocityUpdateStrategy):

    def __init__(self,c1,c2,w):
        self.C1 = c1
        self.C2 = c2
        self.W = w

    def update(self,particle,gbest,**kwargs):
        position = particle.position
        velocity = particle.velocity
        pbest = particle.pbest_position

        r1 = np.random.uniform(0,1,size=len(position))
        r2 = np.random.uniform(0,1,size=len(position))

        c1 = self.C1
        c2 = self.C2
        w = self.W

        cognitive = c1 * r1 * (pbest - position)
        social = c2 * r2 * (gbest - position)

        particle.velocity = w * velocity + cognitive + social
    

class ConstrictionFactor(VelocityUpdateStrategy):

    def __init__(self,c1,c2,kappa):
        self.KAPPA = kappa
        self.C1 = c1
        self.C2 = c2
        self.PHI = c1 + c2

    def update(self,particle,gbest,**kwargs):
        position = particle.position
        velocity = particle.velocity
        pbest = particle.pbest_position
        
        kappa = self.KAPPA
        phi = self.PHI
        c1 = self.C1
        c2 = self.C2

        chi = (2 * kappa) / abs((2 - phi - np.sqrt(pow(phi,2) - 4 )))

        r1 = np.random.uniform(0,1,size=len(position))
        r2 = np.random.uniform(0,1,size=len(position))

        cognitive = c1 * r1 * (pbest - position)
        social = c2 * r2 * (gbest - position)

        particle.velocity = chi * (velocity + cognitive + social)


class LinearReduction(VelocityUpdateStrategy):

    def __init__(self,w_min,w_max,c1,c2,max_iteration):
        assert type(max_iteration) is int

        self.K_MAX = max_iteration
        self.W_MAX = w_max
        self.W_MIN = w_min
        self.C1 = c1
        self.C2 = c2

    def update(self,particle,gbest,**kwargs):
        position = particle.position
        velocity = particle.velocity
        pbest = particle.pbest_position

        k_max = self.K_MAX
        w_max = self.W_MAX
        w_min = self.W_MIN
        c1 = self.C1
        c2 = self.C2

        k = kwargs.get('iteration')

        W_i = w_max - (k * ( (w_max - w_min) / k_max))

        r1 = np.random.uniform(0,1,size=len(position))
        r2 = np.random.uniform(0,1,size=len(position))

        cognitive = c1 * r1 * (pbest - position)
        social = c2 * r2 * (gbest - position)

        particle.velocity = W_i * velocity + cognitive + social