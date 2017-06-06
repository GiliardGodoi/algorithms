#include<stdlib.h>
#include<stdio.h>

typedef struct lista{
    int info;
    struct lista *prox;
}Lista;

Lista* insereFim(Lista* no, int valor){
    Lista* novo, *aux = no;
    novo = (Lista*) malloc(sizeof(Lista));
    novo->info = valor;
    novo->prox = NULL;
    if(no==NULL){
        return novo;
    }else{
        while(aux->prox != NULL){
            aux = aux->prox;
        }
        aux->prox = novo;
        return no;
    }
}

Lista* insereInicio(Lista* no, int valor){
    Lista *novo;
    novo = (Lista*) malloc(sizeof(Lista));
    novo->info = valor;
    novo->prox = no;
    return novo;
}

void imprimirLista(Lista *list){
    while(list != NULL){
        printf("%d\t",list->info);
        list = list->prox;
    }
}

void removeLista(Lista* L){
    Lista *aux = L;
    while(aux!=NULL){
        L = L->prox;
        free(aux);
        aux = L;
    }
}

int main(){
    Lista* L = NULL;
    L = insereInicio(L,5);
    L = insereFim(L,10);
    L = insereInicio(L, 20);

    imprimirLista(L);

    return 0;

}
