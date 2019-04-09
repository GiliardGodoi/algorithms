import numpy as np
import math

class Particle(object):

    def __init__(self,position,velocity,**kwargs):
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.pbest_position = np.array(self.position)
        self.best_error = -1
        self.velocityUpdateStrategy = DefaultVelocityUpdate()

    def __str__(self):
        return f'{self.position}'

    def __repr__(self):
        return self.__str__()

    def update_velocity(self,gbest,**kwargs):
        
        self.velocity = self.velocityUpdateStrategy.update(self,gbest,*kwargs)
    
    def update_position(self):
        self.position = self.position + self.velocity


class VelocityUpdateStrategy():
    def update(self,particle, gbest,**kwargs):
        raise NotImplementedError()

class DefaultVelocityUpdate(VelocityUpdateStrategy):

    def update(self,particle,gbest,**kwargs):
        r1 = np.random.rand()
        r2 = np.random.rand()

        c1 = kwargs.get('c1')
        c2 = kwargs.get('c2')
        w = kwargs.get('w')

        cognitive = c1 * r1 * (particle.pbest_position - particle.position)
        social = c2 * r2 * (gbest - particle.position)

        velocity = w * particle.velocity + cognitive + social

        return velocity
    

class ConstrictionFactor(VelocityUpdateStrategy):

    def update(self,particle,gbest,**kwargs):
        kappa = kwargs.get('kappa')
        phi = kwargs.get('phi')

        c1 = kwargs.get('c1')
        c2 = kwargs.get('c2')

        X = (2 * kappa) / abs((2 - phi - math.sqrt(pow(phi,2) - 4 )))

        r1 = np.random.rand()
        r2 = np.random.rand()

        cognitive = c1 * r1 * (particle.pbest_position - particle.position)
        social = c2 * r2 * (gbest - particle.position)

        velocity = X * (particle.velocity + cognitive + social)

        return velocity


class LinearReduction(VelocityUpdateStrategy):

    def update(self,particle,gbest,**kwargs):
        k = kwargs.get('iterarion')
        k_max = kwargs.get('max_iterarion')
        w_max = kwargs.get('w_max')
        w_min = kwargs.get('w_min')

        c1 = kwargs.get('c1')
        c2 = kwargs.get('c2')

        W = w_max - k * ( (w_max - w_min) / k_max)

        r1 = np.random.rand()
        r2 = np.random.rand()

        cognitive = c1 * r1 * (particle.pbest_position - particle.position)
        social = c2 * r2 * (gbest - particle.position)

        velocity = W * particle.velocity + cognitive + social

        return velocity


class DefaultPositionUpdateStrategy():

    def update(self,particle,**kwargs):
        return particle.velocity + particle.velocity


class PositionUpdateStrategy():

    def update(self,particle,**kwargs):
        avg_velocity = kwargs.get('avg_velocity')
        c3 = kwargs.get('c3')

        r1 = np.random.rand()

        componete = c3 * r1 * (particle.position - avg_velocity)

        return particle.velocity + particle.velocity + componete