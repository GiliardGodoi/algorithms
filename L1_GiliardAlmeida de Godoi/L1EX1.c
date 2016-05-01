/*  UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - Campus de Cornélio Procópio

    ALUNO: Giliard Almeida de Godoi - RA 1581597
    DISCIPLINA: IF53B - ESTRUTURA DE DADOS - TURMA - N13
    Prof. Danilo Sipoli Sanches

    LISTA DE EXERCÍCIOS REFERENTE À APS 1 -
    DATA DA ENTREGA: 04/05/2015
*/

/* QUESTÃO 1 -
        Faça uma função que receba uma lista encadeada L1 e retorne uma nova lista do tipo
    duplamente encadeada LD1 com os elementos pares existentes em L1;

*/
#include<stdio.h>
#include<stdlib.h>
//DECLARANDO OS REGISTROS PARA AS LISTAS
typedef struct listaSimples{
    int info;
    struct listaSimples* prox;
}simplesLista;

typedef struct duplaLista{
    int info;
    struct duplaLista* ant;
    struct duplaLista* prox;
}duplaLista;

//DEFINIÇÃO DAS FUNÇÕES BÁSICAS

// funções para lista simples
simplesLista* simples_InsereInicio(simplesLista* L, int num){
    simplesLista* novo;
    novo = (simplesLista*) malloc(sizeof(simplesLista));
    novo->info = num;
    if(L == NULL){
        novo->prox = NULL;
        return novo;
    }
    novo->prox = L;
    return novo;
}

simplesLista* simples_LiberaLista(simplesLista * L){
    simplesLista* aux = L;
    while(aux!=NULL){
        L = L->prox;
        free(aux);
        aux = L;
    }
    return aux;
}

void simples_Imprime(simplesLista *aux){
    printf("\n");
    while(aux != NULL){
        printf("%d   ",aux->info);
        aux = aux->prox;
    }
    printf("\n");
}

// funções para lista duplamente encadeadas

duplaLista* dupla_InsereFim(duplaLista * L,int valor){
    duplaLista *novo, *aux = L;
    novo = (duplaLista*) malloc(sizeof(duplaLista));
    novo->info = valor;
    novo->prox = NULL;

    if(L == NULL){
        novo->ant = NULL;
        return novo;
    }else{
        while(aux->prox!=NULL){
            aux = aux->prox;
    }
        aux->prox = novo;
        novo->ant = aux;
    }
    return L;
}

void dupla_Imprime(duplaLista* L){
    duplaLista* aux = L;
    printf("\n");
    while(aux != NULL){
       printf("%d\t",aux->info);
       aux = aux->prox;
    }
    printf("\n");
}

duplaLista* dupla_LiberaLista(duplaLista* L){
    duplaLista* aux = L;
    while(aux!=NULL){
        L = L->prox;
        if(L != NULL)
            L->ant = NULL;
        free(aux);
        aux = L;
    }
    return aux;
}

/** FUNÇÃO COMO RESPOSTA AO ENUNCIADO DA QUESTÃO

        Esta função retorna uma lista duplamente encadeada, com todos os elementos pares de uma lista simples
        que recebe como parâmetro da função.

        O retorno é uma LISTA DUPLAMENTE ENCADEADA com todos os elementos pares.*/
duplaLista* dupla_converteElementosPares(simplesLista* aux){
    duplaLista* novaDupla = NULL; // tipo, nova dupla sertaneja?
    while( aux != NULL){
        if((aux->info)%2 == 0){
            novaDupla = dupla_InsereFim(novaDupla, aux->info);
        }
        aux = aux->prox;
    }
    return novaDupla;
}

// PRINCIPAL
int main(){
    simplesLista* L1 = NULL;
    duplaLista* LD1 = NULL;
    int i = 0, tam, num;
    /*
    for(i = 10; i > 0; i--){
        L1 = simples_InsereInicio(L1, i);
    }*/
    printf("Insira o numero de celulas da sua lista simples: ");
    scanf("%d",&tam);

    while(i < tam){
        printf("Valor da célula %d := ", i+1);
        scanf("%d",&num);
        L1 = simples_InsereInicio(L1, num);
        i++;
    }

    printf("\n\nLista Simples :\n");
    simples_Imprime(L1);

    LD1 = dupla_converteElementosPares(L1);

    printf("\n\nLista Duplamente Encadeada Somente com Numeros Pares: \n");
    dupla_Imprime(LD1);

    LD1 = dupla_LiberaLista(LD1);
    L1 = simples_LiberaLista(L1);

    system("PAUSE");
    return 0;
}



