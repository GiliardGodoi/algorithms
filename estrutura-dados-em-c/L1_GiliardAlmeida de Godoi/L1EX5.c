/*  UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - Campus de Cornélio Procópio

    ALUNO: Giliard Almeida de Godoi - RA 1581597
    DISCIPLINA: IF53B - ESTRUTURA DE DADOS - TURMA - N13
    Prof. Danilo Sipoli Sanches

    LISTA DE EXERCÍCIOS REFERENTE À APS 1 -
    DATA DA ENTREGA: 04/05/2015
*/

/* QUESTÃO 5 -
        Faça uma lista duplamente encadeada circular e implemente as seguintes funções para ela:
            a-)Insere
            b-)Remove
            c-)Imprime
*/
#include<stdlib.h>
#include<stdio.h>

typedef struct lista{
    int info;
    struct lista* prox;
    struct lista* ant;
}Lista;

int circular_dupla_verificaVazia(Lista* L){
    return ( L == NULL);
}

Lista* circular_dupla_insere(Lista* L, int info){
    Lista *novo, *aux;
    aux = L;
    novo = (Lista*) malloc(sizeof(Lista));
    novo->info = info;
    if(circular_dupla_verificaVazia(L)){
        novo->prox = novo;
        novo->ant = novo;
        L = novo;
    }else{
        novo->prox = L;
        L->ant = novo;
        while(aux->prox!=L){
            aux = aux->prox;
        }
        aux->prox = novo;
        novo->ant = aux;
    }
    return L;
}
Lista* circular_dupla_removeValor(Lista* L, int valor){
    Lista* aux = L;
    /* verifica se a lista é vazia */
    if(circular_dupla_verificaVazia(L)){
        printf("\nLista vazia!!\n");
        return L;
    }
    /* verifica se o elemento é o primeiro */
    if(aux->info == valor){ // aqui aux ainda está apontando para L, primeiro elemento da lista
        /* verifica se é o único elemento */
        if(aux->prox == L && aux->ant == L ){ //bastaria fazer aux->prox == L para determinar se é o elemento único
            free(L);
            aux = NULL;
            L = NULL;
        }else{
            L = L->prox;
        }
    }else{
        do{
            aux = aux->prox;
        }while(aux != L && aux->info != valor);
    }
        /* verifica se encontrou o elemento */
        if(aux != L){
            /* retira o elemento da lista */
            aux->ant->prox = aux->prox;
            aux->prox->ant = aux->ant;
            free(aux);
            aux = NULL;
        }
        return L;
}

Lista* circular_dupla_liberaLista(Lista* L){
    while(!(circular_dupla_verificaVazia(L))){
        L = circular_dupla_removeValor(L,L->info);
    }
    return L;
}

void circular_dupla_imprime(Lista* L){
    Lista* aux = L;
    printf("\n");
    if(!(circular_dupla_verificaVazia(L))){
        do{
            printf("%d   ",aux->info);
            aux = aux->prox;
        }while(aux!=L);
    }
    printf("\n");
}

// FUNÇÃO PRINCIPAL
int main(){
    Lista* L = NULL;
    int i = 0, tam, num;

    printf("\nTamanho da lista := ");
    scanf("%d",&tam);
    while(i < tam){
        printf("Insira o valor para a %d.o posicao := ", i+1);
        scanf("%d",&num);
        L = circular_dupla_insere(L, num);
        i++;
    }
    circular_dupla_imprime(L);
    printf("\n1T -> remover valor valido ");
    scanf("%d",&num);
    L = circular_dupla_removeValor(L, num);
    circular_dupla_imprime(L);
    printf("\n2T -> remover primeira posicao ");
    scanf("%d",&num);
    L = circular_dupla_removeValor(L, num);
    circular_dupla_imprime(L);
    printf("\n3T -> remover ultimo valor ");
    scanf("%d",&num);
    L = circular_dupla_removeValor(L, num);
    circular_dupla_imprime(L);
    printf("\n4T -> tentar remover valor invalido ");
    scanf("%d",&num);
    L = circular_dupla_removeValor(L, num);
    circular_dupla_imprime(L);

    L = circular_dupla_liberaLista(L);

    circular_dupla_imprime(L);

    system("PAUSE");
    return 0;
}


