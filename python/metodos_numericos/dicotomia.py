'''
    Implementa o método da dicotomia para encontrar o zero de funções.
'''
import math

def funcao(x):
    return math.exp(x) + (x / 2.0)

def metodo_dicotomia(xa,xb,precisao = 0.1):
    anterior = xb
    xc = xa
    while ( abs(xc-anterior) > precisao ):
        anterior = xc
        xc = (xa + xb ) / 2.0
        if ( funcao(xa) * funcao(xc) < 0.0 ) :
            xb = xc
        elif (funcao(xb) * funcao(xc) < 0.0 ) :
            xa = xc
    
    return xc

if __name__ == "__main__" :
    
    raiz = metodo_dicotomia(-0.9,-0.8,precisao=0.0001)
    print("raiz igual a =", raiz)
    print("Y ==", funcao(raiz))
