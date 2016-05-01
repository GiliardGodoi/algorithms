#include<stdlib.h>
#include<stdio.h>

typedef struct lista{
    int info;
    struct lista* prox;
    struct lista* ant;

}Lista;
Lista* insereInicio(Lista* L, int valor){
    Lista* novo;
    novo = (Lista*) malloc(sizeof(Lista));
    novo->info = valor;
    novo->prox = L;
    novo->ant = NULL;
    if(L == NULL){
        return novo;
    }else{
        L->ant = novo;
        return novo;
    }
}

Lista* insereFim(Lista* L, int valor){
    Lista *novo, *aux = L;
    novo = (Lista*) malloc(sizeof(Lista));
    novo->info = valor;
    novo->prox = NULL;

    if(L == NULL){
        novo->ant = NULL;
        return novo;
    }
    while(aux->prox!=NULL){
        aux = aux->prox;
    }
    aux->prox = novo;
    novo->ant = aux;

    return L;
}
Lista* liberaLista(Lista* L){
    Lista* aux = L;
    while(aux!=NULL){
        aux = aux->prox;
        free(aux->ant);
        aux->ant = NULL;

    }

}
/*





    6 -  Vc ainda quer apagar este último elemento?
 */
Lista* apagarLista(Lista* L, int valor){
    Lista *aux = L;

    while(aux!= NULL && aux->info!= valor){
        aux = aux->prox;
    }
    /* 1 - Lista é vazia? */
    if(aux == NULL){
        return aux;
    }
    /* 2 - O elemento procurado existe na lista? */
    if(aux->info == valor){
        /* 3 - Lista possui somente um elemento?*/
        if(aux->ant == NULL && aux->prox == NULL){
            free(aux);
            aux = NULL;
            return aux;
        }
        /* 4 - O elemento a ser apagado é o primeiro? */
        if(aux->ant==NULL){
            L = L->prox;
            free(L->ant);
            L->ant = NULL;
            return L;
        }
        /* 5 - O elemento a ser apagado é o último? */
        if(aux->prox==NULL){
            aux->ant->prox = NULL;
            free(aux);
            aux = NULL;
            return L;
        }
        aux->ant->prox = aux->prox;
        free(aux);
        aux = NULL;
        return L;
    }


}

void imprimeLista(Lista* L){
    Lista* aux;
    aux = L;
    printf("\n");
    while(aux!=NULL){
        printf("%d\t",aux->info);
        aux = aux->prox;
    }
}

int main(){
    Lista* L = NULL;
  /*  L = (Lista*) malloc(sizeof(Lista));
    L->info = 10;
    L->prox = NULL;
    L->ant = NULL;
    printf("\n%d",L->info);

    Lista* novo;
    novo = (Lista*) malloc(sizeof(Lista));
    novo->info = 20;
    novo->prox = NULL;
    novo->ant = L;
    L->prox = novo;
    printf("\n%d\t%d\t%d",L->info,L->prox->info,L->prox->ant->info);*/

    L = insereFim(L, 30);
    L = insereFim(L, 40);
    L = insereInicio(L, 50);

    imprimeLista(L);

}
