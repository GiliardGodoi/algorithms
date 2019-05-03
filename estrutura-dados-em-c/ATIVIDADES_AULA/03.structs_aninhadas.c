/*  UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - Campus de Cornélio Procópio

    DISCIPLINA: IF53B - ESTRUTURA DE DADOS - TURMA - N13
    Prof. Dr. Danilo Sipoli Sanches
    ALUNO: Giliard Almeida de Godoi - RA 1581597

    ATV 2015-03-03 - Structs Aninhadas.
*/
#include<stdio.h>
#include<stdlib.h>

typedef struct Nota {
    float P1;
    float P2;
    float APS;
    int faltas;
} Nota;

typedef struct Aluno {
    char nome[40];
    int RA;
    Nota *nota;
}Aluno;

int main(){

    Aluno *A1;
    A1 = (Aluno *) malloc(sizeof(Aluno));
    A1->nota = (Nota *) malloc(sizeof(Nota));

    printf("Digite o nome:  ");
    scanf("%[^\n]s", &A1->nome);
    printf("Digite o RA: ");
    scanf("%d", &A1->RA);
    printf("Digite a nota da P1: ");
    scanf("%f", &A1->nota->P1);
    printf("Digite a nota da P2: ");
    scanf("%f", &A1->nota->P2);
    printf("Digite a nota da APS: ");
    scanf("%f", &A1->nota->APS);
    printf("Digite o n�mero de faltas: ");
    scanf("%d", &A1->nota->faltas);

    printf("\n\n%s", A1->nome);
    printf("\n%d", A1->RA);
    printf("\n%f", A1->nota->P1);
    printf("\n%f", A1->nota->P2);
    printf("\n%f", A1->nota->P2);
    printf("\n%f", A1->nota->APS);
    printf("\n%d", A1->nota->faltas);

    free(A1->nota);
    free(A1);
    return 0;
}
