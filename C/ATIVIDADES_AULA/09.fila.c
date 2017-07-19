/*  UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - Campus de Cornélio Procópio

    DISCIPLINA: IF53B - ESTRUTURA DE DADOS - TURMA - N13
    Prof. Dr. Danilo Sipoli Sanches
    ALUNO: Giliard Almeida de Godoi - RA 1581597

    ATV 2015-04-07 - Primeira Fila
*/
#include<stdio.h>
#include<stdlib.h>

typedef struct lista{
    int info;
    struct lista * prox;
}Lista;

typedef struct fila{
    struct lista* ini;
    struct lista* fim;
}Fila;

int main(){
    Fila* F;
    F = (Fila*) malloc(sizeof(Fila));
    F->ini = NULL;
    F->fim = NULL;

    Lista* novo;
    novo = (Lista*) malloc(sizeof(Lista));

    novo->info = 50;
    novo->prox = NULL;

    F->ini = novo;
    F->fim = novo;

    printf("%d",F->ini->info);

}
