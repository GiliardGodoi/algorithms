#include <stdio.h>
#include <stdlib.h>

typedef struct lista{
 int info;
 struct lista* prox;
}Lista;

typedef struct pilha{
  Lista* topo;
}Pilha;

void imprime(Pilha* P){
    Lista* aux=P->topo;
    while(aux!=NULL){
        printf("%d ",aux->info);
        aux=aux->prox;
    }
    printf("\n");
}

void push(Pilha* p, int valor){
    Lista* novo;
    novo=(Lista*) malloc(sizeof(Lista));
    novo->info = valor;
    novo->prox=p->topo;
    p->topo = novo;
}

void pop(Pilha* p){
    Lista* aux=p->topo;
    if(aux!=NULL){
        p->topo = p->topo->prox;
        free(aux);
    }
}


main()
{
    Lista* novo;
    Pilha* P = (Pilha*) malloc(sizeof(Pilha));
    P->topo=NULL;

    /*
     * Insere o elemento 10 na base
     */
    novo=(Lista*) malloc(sizeof(Lista));
    novo->info=10;
    novo->prox=NULL;
    P->topo=novo;

    /*
     * Insere o elemento 20 no topo
     */
    novo=(Lista*) malloc(sizeof(Lista));
    novo->info=20;
    novo->prox=P->topo;
    P->topo=novo;

    //printf("%d %d\n",P->topo->info, P->topo->prox->info);

    imprime(P);

    push(P,40);
    push(P,50);

    imprime(P);

    pop(P);

    imprime(P);

}
