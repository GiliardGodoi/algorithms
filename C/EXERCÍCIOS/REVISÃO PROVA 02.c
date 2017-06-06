/*
    EXERCÍCIOS DE REVISÃO
    2) Faça uma função que receba uma Pilha e retorne esta Pilha sem os elementos ímpares.
*/
#include<stdlib.h>
#include<stdio.h>

typedef struct lista{
    int valor;
    struct lista* prox;
}Lista;

typedef struct pilha{
    Lista* topo;
}Pilha;

Pilha* pilha_criaPonteiro(){
    Pilha* p;
    p = (Pilha*) malloc(sizeof(Pilha));
    p->topo = NULL;

    return p;
}

void pilha_push(Pilha* p, int valor){
    Lista* L = (Lista*) malloc(sizeof(Lista));
    L->valor = valor;
    L->prox = p->topo;
    p->topo = L;
}

Lista* pilha_pop(Pilha* p){
    Lista* aux = p->topo;
    if(aux!= NULL){
        p->topo = p->topo->prox;
        aux->prox = NULL;
    }
    return aux;
}

void lista_imprime(Lista* aux){
    while(aux!=NULL){
        printf("%d  ",aux->valor);
        aux = aux->prox;
    }
}

void pilha_imprime(Pilha* p){
    Lista* aux = p->topo;
    lista_imprime(aux);
}

void pilha_somentePares(Pilha* p){
    Lista* aux = pilha_pop(p);
    Pilha* t = pilha_criaPonteiro();
    int num = 0;

    while(aux!=NULL){
        num = aux->valor;
        if((num%2)==0){
            pilha_push(t,num);
        }
        free(aux);
        aux = pilha_pop(p);
    }

    aux = pilha_pop(t);
    while(aux!=NULL){
        pilha_push(p,aux->valor);
        free(aux);
        aux = pilha_pop(t);
    }
}

int main(){
    Pilha* p = pilha_criaPonteiro();
    int i = 1;
    for(i=1; i< 11; i++){
        pilha_push(p,i);
    }
    pilha_imprime(p);
    printf("\n\n");

    pilha_somentePares(p);

    pilha_imprime(p);
}
