/*  UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - Campus de Cornélio Procópio

    DISCIPLINA: IF53B - ESTRUTURA DE DADOS - TURMA - N13
    Prof. Dr. Danilo Sipoli Sanches
    ALUNO: Giliard Almeida de Godoi - RA 1581597

    ATV 2015-03-10 funcao imprimir lista
*/
#include<stdio.h>
#include<stdlib.h>

typedef struct lista{
  int info;
  struct lista* prox;
}Lista;

void imprimirLista(Lista *list);
void insereFim(Lista *list, int x);

int main(){
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
     * O ponteiro L2 ficar� livre para
     * armazenar outro endere�o
     */
    L1->prox=L2;

    /*Cria o terceiro elemento*/
    L2 = (Lista*) malloc(sizeof(Lista));
    L2->info=30;
    L2->prox=NULL;

    /* Liga o segundo elemento com L2
     * O ponteiro L2 ficar� livre novamente
     */
    L1->prox->prox=L2;
    int num;
    scanf("%d", &num);
    insereFim(L1, num);

    imprimirLista(L1);

    scanf("%d", &num);
    insereFim(L1, num);

    imprimirLista(L1);

    return 0;
}

void imprimirLista(Lista *list){
    while(list != NULL){
        printf("%d\t",list->info);
        list = list->prox;
    }
}

void insereFim(Lista *L, int x){
    Lista *novo;

    novo = (Lista *) malloc(sizeof(Lista));
    novo->info = x;
    novo->prox = NULL;


    while( L->prox != NULL){
        L = L->prox;
    }

    L->prox = novo;
}
