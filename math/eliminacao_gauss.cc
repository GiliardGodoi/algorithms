/**
 * Resolve um sistema de equações lineares com método de Triangularização  Gaussiana
 * 
 * CONDIÇÕES: A matriz A de coeficientes deve ser uma matriz quadrada NxN, 
 * cujo tamanho representa a Ordem do Sistema.
 */
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int N;
float b[30];
float x[30];
float a[30][30];

/** 
 * esta funcao mostra o estado das matrizes A e B 
 * */
void Show()
{
	int i, j;
	printf("Ordem do sistema: n= %d\n\n\n", N);
	for(i = 0; i < N ; i++)
	{
		for(j = 0; j < N ; j++)
			printf("    %10.6f", a[i][j]);
		printf("  |  %10.6f\n", b[i]);
	}
	printf("\n\n<ENTER>");
	getchar();
}

/**
 * Esta funcao le via teclado a ordem do sistema,
 * as linhas da matriz de coeficientes A,
 * e a matriz de resultados B
 * */
void LeMatriz()
{
	int i, j;
	printf("Ordem do sistema: n=");
	scanf("%d", &N);

	printf("\n\nDigite os valores separados por espacos.\n");
	for(i = 0; i < N; i++)
	{
		printf("Linha %3d:\n", i+1);
		for(j = 0; j < N; j++)
			scanf("%f", &a[i][j]);
		printf("B = ");
		scanf("%f",&b[i]);
	}
}

/**
 * Calcula o determinante de uma matriz 2x2
 */
int det(float a, float b, float c, float d)
{
	return (a*d) - (b*c);
}


/**
 *  Faz a triangularizacao do sistema pelo metodo de Gauss
 */
void Triang()
{
	int i, j, k;
	for (k = 0; k < (N-1); k++)
	{
		for(i = k+1; i < N; i++)
		{
			for( j = k+1; j < N; j++)
			{
				a[i][j] = det(a[k][k], a[i][k], a[k][j],a[i][j]);
//				Show();
			}
			b[i] = det(a[k][k], a[i][k],b[k],b[i]);
			a[i][k] = 0;
			Show();
		}
	}
}

/**
 * Calcula a matriz das solucoes do sistema ja triangularizado
 */
void CalcSolucao()
{
	int k, j;
	float s;
	x[N-1] = b[N-1] / a[N-1][N-1];
	for( k = N-2; k >=0; k--)
	{
		s = 0;
		for(j =k+1; j < N; j++)
			s += a[k][j] * x[j];
		x[k] = (b[k]-s) / a[k][k];
	}
}

/** 
 * Mostra o resultado da matriz de solucoes
 */
void ShowSolucao()
{
	int i;
	printf("\n\nSolucao do Sistema Linear de Ordem N=%d\n\n", N);
	for(i = 0; i < N; i++)
		printf("x(%3d) = %10.6g\n", i+1, x[i]);
	printf("\n\n\nProblema encerrado.\n");
}

int main(int argc, char* argv[])
{
	LeMatriz();
	Show();
	Triang();
	CalcSolucao();
	ShowSolucao();

	return 1;
}
