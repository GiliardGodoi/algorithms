#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Implementa o método da dicotomia para encontrar o zero de funções.
'''
import math
class MetodoDicotomia():
    '''
    Implementa o método da dicotomia para encontrar as raízes de uma função.

    '''
    def dicotomia(self, funcao, xa, xb, precisao=0.1):
        '''
        Recebe como parâmetro uma função, um valores iniciais xa e xb e a precisão desejada.
        Precisão default é de 0.1
        '''
        anterior = xb
        xc = xa
        while abs(xc-anterior) > precisao:
            anterior = xc
            xc = (xa + xb) / 2.0
            if funcao(xa) * funcao(xc) < 0.0:
                xb = xc
            elif funcao(xb) * funcao(xc) < 0.0:
                xa = xc
        return xc

if __name__ == "__main__":
    def funcaoExponencial(x):
        '''
        E^x + x/2
        '''
        return math.exp(x) + (x / 2.0)

    Dicotomia = MetodoDicotomia()
    RAIZ = Dicotomia.dicotomia(funcaoExponencial, -0.9, -0.8, precisao=0.000000001)
    print("Raiz igual a =", RAIZ)
    print("f(raiz) ==", funcaoExponencial(RAIZ))

    def crazyFunction(x):
        return x - 3 - math.pow(x,-x)
    RAIZ = Dicotomia.dicotomia(crazyFunction, 2, 6, precisao=0.0000000000001)
    print("Raiz igual a =", RAIZ)
    print(crazyFunction(RAIZ))
