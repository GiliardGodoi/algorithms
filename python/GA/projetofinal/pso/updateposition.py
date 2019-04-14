import numpy as np

class DefaultPositionUpdate():

    def update(self,particle,**kwargs):
        particle.position = particle.velocity + particle.position

class AverageVelocityBased():

    def __init__(self,c3):
        self.C3 = c3

    def update(self,particle,**kwargs):
        position = particle.position
        # mean_velocity = particle.mean_velocity if hasattr(particle,'mean_velocity') else self.particle_mean_velocity(particle)
        mean_velocity = self.particle_mean_velocity(particle)

        c3 = self.C3
        r1 = np.random.uniform(0,1,size=len(position))

        componete = c3 * r1 * (position - mean_velocity)

        particle.position = (particle.position + particle.velocity + componete)

    def particle_mean_velocity(self,particle):
        particle.mean_velocity = np.mean(particle.velocity)
        particle.mad_velocity = np.mean(np.absolute(particle.velocity - particle.mean_velocity))

        return particle.mean_velocity