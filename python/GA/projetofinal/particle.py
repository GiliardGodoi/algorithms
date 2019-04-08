import numpy as np

class Particle(object):

    def __init__(self,position,velocity,**kwargs):
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.pbest_position = self.position
        self.best_error = -1

    def __str__(self):
        return f'{self.position}'

    def __repr__(self):
        return self.__str__()

    def update_velocity(self,gbest,**kwargs):
        pass
    
    def update_position(self):
        self.position = self.position + self.velocity