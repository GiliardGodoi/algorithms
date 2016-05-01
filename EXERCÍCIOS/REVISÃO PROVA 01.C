/*
    Exercícios para revisão para a prova

    1) Faça uma função receba uma Fila
    e retorne esta Fila com todos os elementos invertidos.
    Dica: Para inverter a ordem dos elementos utilize uma Pilha auxiliar
*/
#include<stdlib.h>
#include<stdio.h>
typedef struct lista{
    int valor;
    struct lista* prox;
}Lista;

typedef struct fila{
    Lista* ini;
    Lista* fim;
}Fila;

typedef struct pilha{
    Lista* topo;
}Pilha;

Fila* fila_criaPonteiro(){
    Fila* f;
    f = (Fila*) malloc(sizeof(Fila));
    f->ini = NULL;
    f->fim = NULL;

    return f;
}

Pilha* pilha_criaPonteiro(){
    Pilha* p;
    p = (Pilha*) malloc(sizeof(Pilha));
    p->topo = NULL;

    return p;
}

void fila_insere(Fila* f, int valor){
    Lista* novo;
    novo = (Lista*) malloc(sizeof(Lista));
    novo->valor = valor;
    novo->prox = NULL;

    if(f->ini == NULL){
        f->ini = novo;
        f->fim = novo;
    }else{
        f->fim->prox = novo;
        f->fim = novo;
    }
}

Lista* fila_retira(Fila* f){
    Lista* aux;

    if(f->ini == NULL){
        return NULL;
    }
     aux = f->ini;
     if(f->fim == aux){
        f->fim = NULL;
     }
     f->ini = f->ini->prox;
     aux->prox = NULL;

     return aux;
}

void fila_apaga(Fila* f){
    Lista* aux = NULL;
    aux = fila_retira(f);
    if(aux != NULL){
        free(aux);
        aux = NULL;
    }
}

void fila_libera(Fila* f){
    while(f->ini != NULL){
        fila_apaga(f);
    }
}

void pilha_push(Pilha* p, Lista* L){
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

void fila_imprime(Fila* f){
    Lista* aux = f->ini;
    lista_imprime(aux);
}

void pilha_imprime(Pilha* p){
    Lista* aux = p->topo;
    lista_imprime(aux);
}


void fila_inverte(Fila* f){
    Lista* aux = fila_retira(f);
    Pilha* p = pilha_criaPonteiro();
    if(f->ini!=NULL){
        while(aux!=NULL){
            pilha_push(p,aux);
            aux = fila_retira(f);
        }
        aux = pilha_pop(p);
        while(aux!=NULL){
            fila_insere(f,aux->valor);
            aux = pilha_pop(p);
        }
    }
}

int main(){
    Fila* f = fila_criaPonteiro();
    int i = 0;
    for(i = 0; i < 10; i++){
        fila_insere(f, i*10);
    }

    fila_imprime(f);
    printf("\n\n");
    fila_inverte(f);

    fila_imprime(f);

}



