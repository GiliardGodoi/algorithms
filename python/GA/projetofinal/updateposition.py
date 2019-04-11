import numpy as np

class DefaultPositionUpdateStrategy():

    def update(self,particle,**kwargs):
        particle.position = particle.velocity + particle.position

class PositionUpdateStrategy():

    def update(self,particle,mean_velocity,**kwargs):
        
        c3 = kwargs.get('c3')
        position = particle.position
        r1 = np.random.rand()

        componete = c3 * r1 * (position - mean_velocity)

        particle.position = (particle.position + particle.velocity + componete)