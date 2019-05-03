/*
    EXERCÍCIOS DE REVISÃO
    3) Faça uma função que receba uma Pilha e remova o maior elemento desta Pilha.
*/
#include<stdlib.h>
#include<stdio.h>

ypedef struct lista{
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
int pilha_maiorElemento(Pilha* p){
    Lista* aux = p->topo;
    int resultado = 0;
    if(aux!=NULL){

    }
}

void pilha_apagaMaior(Pilha* p){


}
