#include<stdio.h>
#include<stdlib.h>
#define TAM 2

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

float calcMedia(Aluno *a, int qtd);
int calcFaltas(Aluno * a, int qtd);
void imprime(Aluno *a, int qtd);

int main(){
    // Declaração das variáveis
    Aluno *turma;
    int i;
    float media;

    //Alocação da memória
    turma = (Aluno *) malloc(TAM*sizeof(Aluno));
    for(i = 0; i < TAM; i++){
        turma[i].nota = (Nota *) malloc(sizeof(Nota));
    }
    for(i = 0; i < TAM; i++){
        fflush(stdin);
        printf("Digite o nome do aluno %d:  ", i+1);
        scanf("%[^\n]s", &turma[i].nome);
        printf("Digite o RA: ");
        scanf("%d", &turma[i].RA);
        printf("Digite a nota da P1: ");
        scanf("%f", &turma[i].nota->P1);
        printf("Digite a nota da P2: ");
        scanf("%f", &turma[i].nota->P2);
        printf("Digite a nota da APS: ");
        scanf("%f", &turma[i].nota->APS);
        printf("Digite o numero de faltas: ");
        scanf("%d", &turma[i].nota->faltas);
    }


    for(i = 0; i < TAM; i++){
        free(turma[i].nota);
    }
    free(turma);
    return 0;
}

float calcMedia(Aluno *a, int qtd);
int calcFaltas(Aluno * a, int qtd);
void imprime(Aluno *a, int qtd);
