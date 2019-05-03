/*  UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - Campus de Cornélio Procópio

    ALUNO: Giliard Almeida de Godoi - RA 1581597
    DISCIPLINA: IF53B - ESTRUTURA DE DADOS - TURMA - N13
    Prof. Danilo Sipoli Sanches

    LISTA DE EXERCÍCIOS REFERENTE À APS 1 -
    DATA DA ENTREGA: 04/05/2015
*/

/* QUESTÃO 11 -
            Considere uma lista duplamente encadeada para armazenar números inteiros. Implemente uma
    função que receba como parâmetros uma lista com seus elementos ordenados em ordem
    crescente e um número inteiro x, e insira um novo nó na lista com o valor x, preservando a
    ordenação da lista.

*/
#include<stdlib.h>
#include<stdio.h>
typedef struct listaDulpla{
    int info;
    struct listaDulpla* ant;
    struct listaDulpla* prox;
}ListaDupla;

ListaDupla* dupla_cria(){
    ListaDupla* novo;
    novo = (ListaDupla*) malloc(sizeof(ListaDupla));
    novo->ant = NULL;
    novo->prox = NULL;

    return novo;
}
ListaDupla* dupla_insereEmOrdem(ListaDupla* L, int valor){
    ListaDupla* novo = dupla_cria();
    novo->info = valor;
    ListaDupla* aux = L;
    if(aux == NULL){ // verifica se a lista é vazia
        return novo;
    }
    while(aux->prox!=NULL && valor > aux->info){ // percorre lista
        aux = aux->prox;
    }
    if(aux->prox == NULL && valor > aux->info){ //insere fim
        aux->prox = novo;
        novo->ant = aux;

    }else if(aux->ant == NULL && valor < aux->info){ // insere inicio
        novo->prox = aux;
        aux->ant = novo;
        return novo;
    }else { // insere no meio
        aux->ant->prox = novo;
        novo->ant = aux->ant;
        novo->prox = aux;
        aux->ant = novo;
    }
        return L;

}

ListaDupla* dupla_apaga(ListaDupla* L){
    ListaDupla* aux = L;
    if(aux==NULL){ // verifica se é vazia
        return NULL;
    }else if(L->prox == NULL){ // verifica se é elemento único
        free(L);
        L = NULL;
    }else{ //retira do inico
        L = L->prox;
        L->ant = NULL;
        aux->prox = NULL;
    }

    return L;
}

ListaDupla* dupla_apagaValor(ListaDupla* L, int valor){
    ListaDupla* aux = L;
    if(aux == NULL){ // verifica se a lista é vazia
        return aux;
    }
    while(aux!=NULL && aux->info!=valor){ // percorre a lista a procura do valor
        aux = aux->prox;
    }
    if(aux == NULL){ // não encontrou o valor
        return L;
    }else if(aux->ant == NULL && aux->info == valor){ // retirar o primeiro elemento
        L = L->prox;
        L->ant = NULL;
        aux->prox = NULL;
    }else if(aux->prox == NULL && aux->info == valor){ //retirar o último elemento
        aux->ant->prox = NULL;
        aux->ant = NULL;
    }else{ // retira elemento no meio da lista
        aux->ant->prox = aux->prox;
        aux->prox->ant = aux->ant;
        aux->prox = NULL;
        aux->ant = NULL;
    }
    free(aux);
    return L;
}

ListaDupla* dupla_liberaLista(ListaDupla* L){
    while(L != NULL){
        L = dupla_apaga(L);
    }
}

void dupla_imprime(ListaDupla* L){
    if(L == NULL){
        printf("Lista vazia!!");
    }
    while(L != NULL){
        printf("%d   ",L->info);
        L = L->prox;
    }
}

int main(){
    int i = 0;
    ListaDupla* L = NULL;

    L = dupla_insereEmOrdem(L, 10);
    L = dupla_insereEmOrdem(L, 5);
    L = dupla_insereEmOrdem(L, 20);
    L = dupla_insereEmOrdem(L, 15);
    L = dupla_insereEmOrdem(L, 30);
    L = dupla_insereEmOrdem(L, 1);

    L = dupla_apagaValor(L, 1);
    L = dupla_apagaValor(L,30);
    L = dupla_apagaValor(L,15);

    dupla_imprime(L);

    L = dupla_liberaLista(L);


    return 0;
}
