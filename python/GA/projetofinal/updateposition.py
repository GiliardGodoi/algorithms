import numpy as np

class DefaultPositionUpdate():

    def update(self,particle,**kwargs):
        particle.position = particle.velocity + particle.position

class AverageVelocityBased():

    def update(self,particle,**kwargs):
        position = particle.position
        mean_velocity = particle.mean_velocity if hasattr(particle,'mean_velocity') else self.particle_stats(particle)

        c3 = kwargs.get('c3')
        r1 = np.random.rand()

        componete = c3 * r1 * (position - mean_velocity)

        particle.position = (particle.position + particle.velocity + componete)

    def particle_stats(self,particle):
        particle.mean_velocity = np.mean(particle.velocity)
        particle.mad_velocity = np.mean(np.absolute(particle.velocity - particle.mean_velocity))

        return particle.mean_velocity