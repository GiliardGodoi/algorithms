# Tips and Tricks about functions in Python(R)

```python
    def funcao_hello(nome,**kwargs):
        saudacao = f'Hello {nome}'

        if not len(kwargs) :
            print(saudacao)
        else:
            complemento = bar(kwargs.get('idade'),kwargs)
            print(saudacao,complemento)


    def bar(idade,kwords,**kwargs):

        dos = kwords.get('dos', None)

        if not dos is None:
            return f'{idade} anos, nascido em {dos}'
        else :
            return f'{idade} anos, nascimento desconhecido'


    if __name__ == "__main__":

        funcao_hello('Giliard',idade=28,dos='25 de abril')
```