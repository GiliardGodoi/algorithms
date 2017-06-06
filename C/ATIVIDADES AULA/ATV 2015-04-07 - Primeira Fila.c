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
