import sys
import random

def random_error():
    nro = random.randint(0,100)
    if nro % 2 :
        raise ValueError('mensagem personalizada')
    else :
        raise TypeError('type error example')

def other_function(param):
    print('param: {0}'.format(param))
    print('funcao entra em execuçao')


def some_important_operation(param = None):
    try:
        valor = 10
        if not param :
            random_error()
        other_function(param)
    except ValueError as error:
        print('vish rolou um erro')
        return 55
        print('esta linha nao ira ser impressa. por causa do return')
    except TypeError as err :
        raise err
        print('linha que nao sera impressa!')
    else :
        print('nada de ruim aconteceu')
        return valor
        print('nadica de nada')
    finally :
        print('este codigo sera executado de qualquer jeito')
        return 100
        print('esta linha nao ira ser impressa.')

if __name__ == '__main__':
    pato = 8
    try:
        pato = sys.argv[1]
    except IndexError as e :
        print("Mais Facil é Pedir Perdao do que Permissao")
    if len(sys.argv) == 3 :
        print("pense duas vezes antes de agir")
    nome_do_arquivo = sys.argv[0]
    b = some_important_operation(pato)
    print('valor de b: {0}'.format(b))
    print(nome_do_arquivo)