Código Fonte - Fila representada por lista encadeada

#include <stdio.h>
#include <stdlib.h>

typedef struct lista{
   int info;
   struct lista* prox;
}Lista;

typedef struct fila{
   Lista* ini;
   Lista* fim;
}Fila;

void imprime(Fila* F){
    Lista* aux = F->ini;
    while(aux!=NULL){
        printf("%d\n",aux->info);
        aux=aux->prox;
    }
}

void insereFila(Fila* F, int valor){
    Lista* novo;
    novo=(Lista*) malloc(sizeof(Lista));
    novo->info=valor;
    novo->prox=NULL;
    if(F->ini==NULL){
        F->ini=novo;
        F->fim=novo;
    }else{
        F->fim->prox=novo;
        F->fim = novo;
    }
}

void removeFila(Fila* F){
    Lista* aux=F->ini;

    if(aux!=NULL){
        F->ini = aux->prox;
        free(aux);

        if(F->ini==NULL)
           F->fim=NULL;
    }
}



main(){
    Fila* F = (Fila*) malloc(sizeof(Fila));
    F->ini = NULL;
    F->fim = NULL;
    insereFila(F, 10);
    insereFila(F, 20);
    insereFila(F, 30);
    imprime(F);
    removeFila(F);
    imprime(F);
}
