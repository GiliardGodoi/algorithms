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
        self.velocity = self.velocityUpdateStrategy.update(self.position,self.velocity,self.pbest_position,gbest,kwargs)
    
    def update_position(self):
        self.position = self.position + self.velocity


class VelocityUpdateStrategy():
    
    def update(self,position,velocity,pbest, gbest,kwords,**kwargs):
        raise NotImplementedError()

class DefaultVelocityUpdate(VelocityUpdateStrategy):

    def update(self,position,velocity,pbest, gbest,kwords,**kwargs):
        r1 = np.random.uniform(0,1,size=len(position))
        r2 = np.random.uniform(0,1,size=len(position))

        c1 = kwords.get('c1')
        c2 = kwords.get('c2')
        w = kwords.get('w')

        cognitive = c1 * r1 * (pbest - position)
        social = c2 * r2 * (gbest - position)

        velocity = w * velocity + cognitive + social

        return velocity
    

class ConstrictionFactor(VelocityUpdateStrategy):

    def update(self,position,velocity,pbest, gbest,kwords,**kwargs):
        
        kappa = kwords.get('kappa')
        phi = kwords.get('phi')

        c1 = kwords.get('c1')
        c2 = kwords.get('c2')

        chi = (2 * kappa) / abs((2 - phi - math.sqrt(pow(phi,2) - 4 )))

        r1 = np.random.uniform(0,1,size=len(position))
        r2 = np.random.uniform(0,1,size=len(position))

        cognitive = c1 * r1 * (pbest - position)
        social = c2 * r2 * (gbest - position)

        velocity = chi * (velocity + cognitive + social)

        return velocity


class LinearReduction(VelocityUpdateStrategy):

    def update(self,position,velocity,pbest, gbest,kwords,**kwargs):
        k = kwords.get('iterarion')
        k_max = kwords.get('max_iterarion')
        w_max = kwords.get('w_max')
        w_min = kwords.get('w_min')

        c1 = kwords.get('c1')
        c2 = kwords.get('c2')

        W = w_max - k * ( (w_max - w_min) / k_max)

        r1 = np.random.rand()
        r2 = np.random.rand()

        cognitive = c1 * r1 * (pbest - position)
        social = c2 * r2 * (gbest - position)

        velocity = W * velocity + cognitive + social

        return velocity


class DefaultPositionUpdateStrategy():

    def update(self,particle, velocity,**kwargs):
        return velocity + particle


class PositionUpdateStrategy():

    def update(self,position, velocity,**kwargs):
        avg_velocity = kwargs.get('avg_velocity')
        c3 = kwargs.get('c3')

        r1 = np.random.rand()

        componete = c3 * r1 * (position - avg_velocity)

        return velocity + position + componete