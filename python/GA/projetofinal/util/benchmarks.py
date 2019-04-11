import numpy as np

def dejong_sphere(variables):
        return sum(map(lambda i: pow(i,2),variables))


def quadratic_random():
    rand = np.random.rand
    zeta = lambda nro: pow(nro,4) + rand()

    def core_funtion(variables):
        return sum(map(zeta,variables))
    
    return core_funtion

def cosine_complicate():
    
    zeta = lambda x: pow(x,2) - 10*np.cos(2*np.pi*x) + 10
    
    def core(variables):
        return sum(map(zeta,variables))

    return core

def other_complicate():
    const = 1/4000
    zeta = lambda i,x: i*pow(x,2)
    beta = lambda i,x: np.cos(x/np.sqrt(i)) + 1

    def core(variables):
        
        _x = [zeta(i+1,x) for i,x in enumerate(variables)]
        _y = [beta(i+1,x) for i,x in enumerate(variables)]

        return const * np.sum(_x) + np.prod(_y)

    return core