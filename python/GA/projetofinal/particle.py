import numpy as np

class Particle(object):

    def __init__(self,position,velocity,**kwargs):
        self.__position = np.array(position)
        self.__velocity = np.array(velocity)
        self.pbest_position = np.array(self.position)

    def __str__(self):
        return f'{self.__position}'

    def __repr__(self):
        return self.__str__()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self,value):
        assert len(value) == len(self.__position), f'dimensões necessária: {len(self.__position)}'
        if not type(value) is np.ndarray:
            value = np.array(value)
        self.__position = value

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self,value):
        assert len(value) == len(self.__velocity), f'dimensões necessária: {len(self.__velocity)}'
        if not type(value) is np.ndarray:
            value = np.array(value)
        self.__velocity = value