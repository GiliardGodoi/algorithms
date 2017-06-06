/*  UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - Campus de Cornélio Procópio

    ALUNO: Giliard Almeida de Godoi - RA 1581597
    DISCIPLINA: IF53B - ESTRUTURA DE DADOS - TURMA - N13
    Prof. Danilo Sipoli Sanches

    LISTA DE EXERCÍCIOS REFERENTE À APS 1 -
    DATA DA ENTREGA: 04/05/2015
*/

/* QUESTÃO 8 -
        Faça uma função que receba uma lista encadeada L1 e retorne a lista L1 com os elementos
invertidos. Para isso, deverá ser utilizada uma pilha. Exemplo: Lista1 = {1,2,3}, após passar
pela função a Lista1 ficará: Lista1 = {3,2,1}.
*/
#include<stdio.h>
#include<stdlib.h>
typedef struct lista{
    int info;
    struct lista *prox;
}Lista;

typedef struct pilha{
    Lista* topo;
}Pilha;


// funções sobre lista
Lista* lista_InsereFim(Lista* L, int num){
    Lista* novo, *aux = L;
    novo = (Lista*) malloc(sizeof(Lista));
    novo->info = num;
    novo->prox = NULL;
    if(L == NULL){
        L = novo;
    }else{
        while(aux->prox!=NULL){
            aux = aux->prox;
        }
        aux->prox = novo;

    }

    return L;
}

void lista_Imprime(Lista* aux){
    printf("\n");
    while(aux!= NULL){
        printf("%d  ", aux->info);
        aux = aux->prox;
    }
    printf("\n");
}

// funções sobre pilha
Pilha* criaPilha(){
    Pilha* P;
    P = (Pilha*)malloc(sizeof(Pilha));
    P->topo = NULL;
    return P;
}
void push(Pilha* P, int valor){
    Lista* novo;
    novo = (Lista*) malloc(sizeof(Lista));
    novo->info = valor;
    novo->prox = P->topo;
    P->topo = novo;
}
Lista* pop(Pilha* P){
    if(pilha_vazia(P)){
        return NULL;
    }
    Lista* aux;
    aux = P->topo;
    P->topo = P->topo->prox;
    aux->prox = NULL;
    return aux;
    // aqui a ordem das instruções alternam o resultado sim!!
}
int pilha_vazia(Pilha* P){
    return (P->topo == NULL);
    /* Em C os valores lógicos verdadeiro e falso são implementados como o sendo 0 ZERO para falso,
        e qualquer outro número para verdadeiro. Então essa função vai retornar 1 se a comparação
        for verdadeira. */
}

/** RESPOSTA AO ENUNCIADO DO PROBLEMA
    Função inverte os elementos de uma lista, usando uma pilha na sua implementação.
    Recebe como parâmetro uma lista e retorna a os elementos invertidos.
    */
Lista* lista_Inverte(Lista* L){
    Pilha* P;
    P = criaPilha();
    Lista* aux;
    while(L != NULL){
        push(P,L->info);
        L = L->prox;
    }

    while(!(pilha_vazia(P))){
        aux = pop(P);
        L = lista_InsereFim(L,aux->info);
        free(aux);
    }
    return L;
}

//FUNÇÃO PRINCIPAL
int main(){
    Lista* L = NULL;
    int i = 0, tam, num;

    printf("Numero de elementos da LISTA := ");
    scanf("%d",&tam);

    while(i < tam){
        printf("Insira o %d.o valor := ", i+1);
        scanf("%d",&num);
        L = lista_InsereFim(L , num);
        i++;
    }
    lista_Imprime(L);
    L = lista_Inverte(L);
    lista_Imprime(L);

}

