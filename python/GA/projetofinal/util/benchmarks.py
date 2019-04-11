import numpy as np

def dejong_sphere(variables):
        return np.sum(np.power(variables,2))

def quadratic_noise(variables):
    random_vector = np.random.uniform(0,1,size=len(variables))    
    return np.sum(np.power(variables,4) + random_vector)

def rastrigin_function(variables):
    return np.sum((np.power(variables,2)) - (10 * np.cos(2*np.pi*variables) + 10))

def griewank_function(variables):
    const = 1/4000
    indices = np.arange(1,len(variables)+1,1,dtype=np.int16)

    somatorio = np.sum(indices * np.power(variables,2))
    produtorio = np.prod(np.cos(np.divide(variables,np.sqrt(indices)))+1)

    return const * somatorio * produtorio