#include<stdio.h>
#include<stdlib.h>
#include <math.h>

using namespace std;

int N;
float B[30], x0[30], x1[30];
float A[30][30];
float Maxdif;

/**
 * Esta funcao le via teclado a ordem do sistema,
 * as linhas da matriz de coeficientes A,
 * e a matriz de resultados B
 * */
void LeMatriz()
{
	int i, j;
	printf("Ordem do sistema: n = ");
	scanf("%d", &N);

	printf("\n\nDigite os valores separados por espacos.\n");
	for(i = 0; i < N; i++)
	{
		printf("Linha %3d:\n", i+1);
		for(j = 0; j < N; j++)
			scanf("%f", &(A[i][j]));
		printf("B = ");
		scanf("%f",&(B[i]));
	}
}

void Inicializa()
{
    for(int i = 0; i < N; i++) x0[i] = 0.0;
}

/**
 * Calcula a maior diferença entre X0 e X1
 */
float Maximo()
{
    int i;
    float d, max = 0;
    for(i = 0; i < N; i++)
    {
        d = fabs(x1[i] - x0[i]);
        if(d > max) max = d;
    }
    return max;
}

void Imprime(float *X, int k, int p)
{
    int i;
    printf("Solucao para o sistema linear\n\n");
    for(i = 0; i < N; i++)
    {
        printf("x(%3d) = %10.6g\n",i,X[i]);
    }
    if(k > 0) printf("\n\nIteracao: %d\tMaxDif: %g\n\n",k,Maximo());
    if(p == 0) printf("Problema encerrado.\n");
    printf("<ENTER>");
    getchar();
}

void iteracao(int k)
{
    int i,j;
    for(i = 0; i < N; i++) x1[i] = x0[i];
    for(i = 0; i < N; i++)
    {
        x1[i] = B[i];
        for(j = 0; j < N; j++)
        {
            if( i != j)
            {
                x1[i] -= A[i][j] * x1[j];
            }
        }
        x1[i] /= A[i][i];
    }
    Imprime(x1,k+1,1);
}

int main(int argc, char* argv[])
{
    int i, k = 0;
    
    LeMatriz();
    Inicializa();
    Imprime(x0,k,1);

    do {
        iteracao(k);
        Maxdif = Maximo();
        for(i = 0; i < N; i++) x0[i] = x1[i];
        k++;
    } while (Maxdif > 1.0e-8);

    Imprime(x1,k,0);

    return 0;
}