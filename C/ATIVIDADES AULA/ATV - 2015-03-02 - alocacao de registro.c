#include<stdio.h>
#include<stdlib.h>

typedef struct{
    char nome[40];
    int RA;
    float P1, P2, T, APS;
}ALUNO;

void imprime(ALUNO *aluno){
    printf("\n\n%s\n%.2f\n%.2f\n%.2f\n%.2f",aluno->nome,aluno->P1, aluno->P2, aluno->T, aluno->APS);
}

int main(){
    ALUNO *aluno;
    int i, qtd;


    aluno = (ALUNO *) malloc(sizeof(ALUNO));
    if(aluno == NULL){
        exit(0);
    }
    fflush(stdin);
    scanf("%[^\n]s", aluno->nome);
    scanf("%d", &aluno->RA);
    scanf("%f", &aluno->P1);
    scanf("%f", &aluno->P2);
    scanf("%f", &aluno->T);
    scanf("%f", &aluno->APS);

    imprime(aluno);

    free(aluno);
    return 0;
}
