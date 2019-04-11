import numpy as np

class Particle(object):

    def __init__(self,position,velocity,**kwargs):
        assert len(position) == len(velocity), "Position and velocity must have the same dimension"
        self.__position = np.array(position)
        self.__velocity = np.array(velocity)
        self.pbest_position = np.array(self.position)
        self.__dimension = len(self.__velocity)

    def __str__(self):
        return f'{self.__position}'

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.__dimension)

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