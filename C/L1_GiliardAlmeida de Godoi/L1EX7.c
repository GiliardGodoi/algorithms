/*  UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - Campus de Cornélio Procópio

    ALUNO: Giliard Almeida de Godoi - RA 1581597
    DISCIPLINA: IF53B - ESTRUTURA DE DADOS - TURMA - N13
    Prof. Danilo Sipoli Sanches

    LISTA DE EXERCÍCIOS REFERENTE À APS 1 -
    DATA DA ENTREGA: 04/05/2015
*/

/* QUESTÃO 7 -
       Construa uma função que retorne a quantidade de números primos em uma lista duplamente
       encadeada. Obs: implementar as funções necessárias para inserção, remoção e impressão da
       lista duplamente encadeada.

*/
#include<stdio.h>
#include<stdlib.h>

typedef struct listadupla{
    int info;
    struct listadupla* ant;
    struct listadupla* prox;
}ListaDupla;

int lstDupla_verificaVazia(ListaDupla* L){
    return (L == NULL);
}

ListaDupla* lstDupla_criaNo(int valor){
    ListaDupla* novo;
    novo = (ListaDupla*) malloc(sizeof(ListaDupla));
    novo->info = valor;
    novo->ant = NULL;
    novo->prox = NULL;

    return novo;
}

ListaDupla* lstDupla_insere(ListaDupla* L, int valor, int pos){
    int i = 1;

    ListaDupla* novo = lstDupla_criaNo(valor);
    ListaDupla* aux = L;
    if(L == NULL){ // verifica condição de lista vazia
        return novo;
    }
    if(pos == 1){ // inserir no inicio
        novo->prox = L;
        if(L != NULL){
            L->ant = novo;
        }
        L = novo;
        return L;
    }
    pos--;
    while(aux->prox != NULL && i!= pos){
        aux = aux->prox;
        i++;
    }
    if(aux->prox == NULL){// inserir no fim
        aux->prox = novo;
        novo->ant = aux;
    }else{ //insere no meio
        aux->prox->ant = novo;
        novo->prox = aux->prox;
        novo->ant = aux;
        aux->prox = novo;
    }
    return L;
}

ListaDupla* lstDupla_retira(ListaDupla* L, int valor){
    ListaDupla* aux = L;
    while(aux!=NULL && aux->info != valor){
        aux = aux->prox;
    }
    if(aux == NULL){ // valor não encontrado
        return L;
    }
    if(aux->ant == NULL){ // retirar do início
        L = L->prox;
        if(L!=NULL){
            L->ant = NULL;
        }
    }else if(aux->prox == NULL){ // retirar do fim
        aux->ant->prox = NULL;

    }else {
        aux->ant->prox = aux->prox;
        aux->prox->ant = aux->ant;
    }
    free(aux);

    return L;

}
void lstDupla_imprime(ListaDupla* aux){
    while(aux!=NULL){
        printf("%d  ",aux->info);
        aux = aux->prox;
    }
}

int verifica_NumPrimo(int valor){
    // em teoria dos números, prova-se que, para verificar se um número 'n' é primo
    // é suficiente testar se 'n' NÂO é divisivel por todos os números até o número inteiro q mais próximo da raiz quadrada de n
    // mas o algoritmo abaixo é bem rápido até para testar números primos como 999983
    int i = 2;
    int resultado = 0; // falso
    while(valor%i != 0 && i < valor){
        i++;
    }
    if( i == valor){
        resultado = 1; // verdadeiro
    }
    return resultado;
}
/** Função que verifica a quantidade de números primos numa lista duplamente encadeada. */
int lstDupla_quantNumPrimos(ListaDupla* aux){
    int quant = 0;

    while(aux!=NULL){
        if(verifica_NumPrimo(aux->info)){
            quant++;
        }
        aux = aux->prox;
    }

    return quant;
}

int main(){
    ListaDupla* L = NULL;

    L = lstDupla_insere(L, 2, 2);
    L = lstDupla_insere(L, 3, 2);
    L = lstDupla_insere(L, 5, 1);
    L = lstDupla_insere(L, 7, 4);
    L = lstDupla_insere(L, 11, 4);
    L = lstDupla_insere(L, 40, 4);
    L = lstDupla_insere(L, 100, 100);

    lstDupla_imprime(L);

    printf("\n\nQuantidade de  numeros primo? %d", lstDupla_quantNumPrimos(L));
}


