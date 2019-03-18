/**
 *  Verifica se um sistema de N equacoes lineares satisfaz
 * o criterio de convergencia do metodo iterativo de gauss-seidel.
 * 
 * Criterio: que a soma dos elementos de uma linha (exceto o elemento da diagonal principal)
 * seja menor que o próprio elemento da diagonal principal.
 */
#include<stdio.h>
#include<math.h>

int N;
float B[30];
float A[30][30];

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

void ShowMatriz()
{
    int i, j;
    for( i = 0; i < N; i++)
    {
        for( j = 0; j < N; j++)
            printf("%10.6f", A[i][j]);
        printf("\n");
    }
}

int criterio()
{
    int i, j;
    float s;
    for(i = 0; i < N; i++)
    {
        s = 0.0;
        for(j = 0; j < N; j++)
        {
            if( i != j)
            {
                s += fabs(A[i][j]);
            }
        }
        if(s >= fabs(A[i][i])) return 0;
    }
    return 1;                                                       
}

int main(int argc, char* argv[])
{
    int teste;
    LeMatriz();
    ShowMatriz();
    teste = criterio();
    if(teste){
        printf("O criterio e satisfeito!\n");
    } else {
        printf("O criterio nao e satisfeito!\n");
    }
    printf("Teste = %d", teste);
    return 0;
}