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

    def update(self,particle,gbest,**kwargs):
        position = particle.position
        velocity = particle.velocity
        pbest = particle.pbest_position

        k = kwargs.get('iterarion')
        k_max = kwargs.get('max_iterarion')
        w_max = kwargs.get('w_max')
        w_min = kwargs.get('w_min')

        c1 = kwargs.get('c1')
        c2 = kwargs.get('c2')

        W = w_max - k * ( (w_max - w_min) / k_max)

        r1 = np.random.rand()
        r2 = np.random.rand()

        cognitive = c1 * r1 * (pbest - position)
        social = c2 * r2 * (gbest - position)

        position.velocity = W * velocity + cognitive + social