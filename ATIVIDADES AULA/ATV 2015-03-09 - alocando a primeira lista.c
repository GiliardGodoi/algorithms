#include<stdio.h>
#include<stdlib.h>

typedef struct lista{
    int info;
    struct lista *prox;
}Lista;


int main(){
    Lista *L1;

    L1 = (Lista *) malloc(sizeof(Lista));
    L1->info = 10;
    L1->prox = NULL;

    /*CRIA O SEGUNDO ELEMENTO*/
    Lista *L2;

    L2 = (Lista *) malloc(sizeof(Lista));
    L2->info = 20;
    L2->prox = NULL;

    L1->prox = L2;

    printf("%d\t%d\n\n",L1->info, L2->info);
    /*CRIA O TERCEIRO ELEMENTO*/
    L2 = (Lista *) malloc(sizeof(Lista));
    L2->info = 30;
    L2->prox = NULL;
    L1->prox->prox = L2;

   // printf("%d\t%d\t%d",L1->info, L1->prox->info, L1->prox->prox->info);
   Lista* aux;
   aux = L1;
   while(aux != NULL){
        printf("%d\t", aux->info);
        aux = aux->prox;
   }

    return 0;
}
