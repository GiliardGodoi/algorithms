import argparse
from argparse import ArgumentParser

parser = ArgumentParser(
		description="Descrição do programa",
		prog='Utils', # Nome do programa
		epilog="Texto exibido no final da Ajuda", # opcional
	)

# Define um argumento posicional obrigatório (a ordem importa)
parser.add_argument('name', help='Seu nome')

if __name__ == "__main__":

	args = parser.parse_args()
	print(type(args))
	print(f'Olá {args.name}! Seja bem-vindo')

