#include<stdio.h>
#include<stdlib.h>

typedef struct lista{
  int info;
  struct lista* prox;
}Lista;

main(){
    Lista* L1, *L2;
    /*Cria o primeiro elemento*/
    L1 = (Lista*) malloc(sizeof(Lista));
    L1->info=10;
    L1->prox=NULL;

    /*Cria o segundo elemento*/
    L2 = (Lista*) malloc(sizeof(Lista));
    L2->info=20;
    L2->prox=NULL;

    /* Liga L1 com L2
     * O ponteiro L2 ficará livre para
     * armazenar outro endereço
     */
    L1->prox=L2;

    /*Cria o terceiro elemento*/
    L2 = (Lista*) malloc(sizeof(Lista));
    L2->info=30;
    L2->prox=NULL;

    /* Liga o segundo elemento com L2
     * O ponteiro L2 ficará livre novamente
     */
    L1->prox->prox=L2;

    printf("%d %d %d\n",L1->info,L1->prox->info,L1->prox->prox->info);

    /*
     * Imprimindo com laço de repetição
     */
     Lista* aux=L1;
     while(aux!=NULL){
         printf("%d ",aux->info);
         aux=aux->prox;
    }
    printf("\n");



}
