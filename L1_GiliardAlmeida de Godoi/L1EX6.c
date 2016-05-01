/*  UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - Campus de Cornélio Procópio

    ALUNO: Giliard Almeida de Godoi - RA 1581597
    DISCIPLINA: IF53B - ESTRUTURA DE DADOS - TURMA - N13
    Prof. Danilo Sipoli Sanches

    LISTA DE EXERCÍCIOS REFERENTE À APS 1 -
    DATA DA ENTREGA: 04/05/2015
*/

/* QUESTÃO 6 -
        Construa uma função para remover todos os elementos pares de uma lista duplamente
encadeada circular. Obs: implementar as funções necessárias para inserção, remoção e
impressão da lista duplamente encadeada circular.
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
            L = L->prox; /** Se é o primeiro elemento que vai ser eliminado,
                            o ponteiro que marca o início da lista vai para o próximo elemento,
                            como se a lista andasse no sentido horário.
                            Isto vai influenciar no comportamento da função para remover números pares. */
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
    if(circular_dupla_verificaVazia(L)){
        printf("Lista vazia!!");
    }
    if(!(circular_dupla_verificaVazia(L))){
        do{
            printf("%d   ",aux->info);
            aux = aux->prox;
        }while(aux!=L);
    }
    printf("\n");
}
/** RESPOSTA AO ENUNCIADO DA QUESTÃO

    A função os elementos pares da Lista Duplamente Encadeada Circular, que recebe como parâmetro.

    A função retorna uma nova lista com todos os valores ímpares ou então retorna NULL.
*/
Lista* circular_dupla_removePares(Lista* L){
    Lista* aux = L;
    if(circular_dupla_verificaVazia(L)){
        return L;
    }
    do{
        if((aux->info)%2 == 0){
            aux = aux->ant;
            L = circular_dupla_removeValor(L, aux->prox->info);
        }else{
            aux = aux->ant;
        }
    }while(aux!=L);
    /* é necessário mais essa verificação para se garantir que todos os elementos foram verificados
        Se L não foi atualizado, isto é, o primeiro elemento é ímpar, vamos verificar a célula de inicio novamente.
        Se L foi atualizado, ou seja, o primeiro elemento é par, vamos garantir a verificação de todos os elementos. */
    if((aux->info)%2 == 0){
        L = circular_dupla_removeValor(L, aux->info);
    }

    return L;

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

    // insira o novo código de testes aqui
    L = circular_dupla_removePares(L);

    circular_dupla_imprime(L);

    L = circular_dupla_liberaLista(L);

    //circular_dupla_imprime(L);

    system("PAUSE");
    return 0;
}



