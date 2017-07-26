/*
    FUNÇÕES RECURSISVAS

    1 - Critério de parada;
    2 - A função tem algum retorno??;


*/
#include<stdlib.h>
#include<stdio.h>

typedef struct lista{
    int info;
    struct lista* prox;
}Lista;

Lista* insereFim(Lista* L, int valor ){
    if(L == NULL){
        Lista* novo;
        novo = (Lista*) malloc(sizeof(Lista));
        novo->info = valor;
        novo->prox = NULL;
        L = novo;
    }else{
        L->prox = insereFim(L->prox, valor);
    }
    return L;
}
void imprime(Lista* L){
    if(L!=NULL){
        printf("%d  ",L->info);
        imprime(L->prox);
    }
}

int maiorElemento(Lista* L){
    if(L == NULL){
        return 0;
    }
    if(L->prox == NULL){
        return L->info;
    }
    int maior;
    maior = maiorElemento(L->prox);

    if(maior < L->info){
        maior = L->info;
    }
    return maior;
}


int main(){
    Lista* L = NULL;
    int maior;

    L = insereFim(L, 5);
    L = insereFim(L, 10);
    L = insereFim(L, 15);
    L = insereFim(L, 20);
    L = insereFim(L, 0);
    L = insereFim(L, 45);
    L = insereFim(L, 25);
    L = insereFim(L, 30);

    imprime(L);

    maior = maiorElemento(L);

    printf("\n\nMaior Elemento: %d \n\n",maior);
    system("PAUSE");

    return 0;
}
