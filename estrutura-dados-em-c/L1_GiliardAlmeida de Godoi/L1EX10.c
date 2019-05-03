/*  UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - Campus de Cornélio Procópio

    ALUNO: Giliard Almeida de Godoi - RA 1581597
    DISCIPLINA: IF53B - ESTRUTURA DE DADOS - TURMA - N13
    Prof. Danilo Sipoli Sanches

    LISTA DE EXERCÍCIOS REFERENTE À APS 1 -
    DATA DA ENTREGA: 04/05/2015
*/

/* QUESTÃO 10 -
        Faça uma função que receba uma pilha P1 e retorne ESSA MESMA PILHA com os elementos
    invertidos.
*/
#include<stdlib.h>
#include<stdio.h>
typedef struct lista{
    int info;
    struct lista *prox;
}Lista;

typedef struct fila{
    Lista* ini;
    Lista* fim;
}Fila;

typedef struct pilha{
    Lista* topo;
}Pilha;

Pilha* criaPilha(){
    Pilha* P;
    P = (Pilha*) malloc(sizeof(Pilha));
    P->topo = NULL;
    return P;
}
Fila* fila_criaPonteiro(){
    Fila* f;
    f = (Fila*) malloc(sizeof(Fila));
    f->ini = NULL;
    f->fim = NULL;

    return f;
}

void push(Pilha* P, int valor){ //empilha
    Lista* novo;
    novo = (Lista*) malloc(sizeof(Lista));
    novo->info = valor;
    novo->prox = P->topo;
    P->topo = novo;
}
Lista* pop(Pilha* P){ // desempilha
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
}
void pilha_imprime(Pilha* P){
    Lista* aux = P->topo;
    printf("\n");
    while(aux!=NULL){
            printf("%d  ",aux->info);
            aux = aux->prox;
    }
    printf("\n");
}

void fila_insere(Fila* f, int valor){
    Lista* novo;
    novo = (Lista*) malloc(sizeof(Lista));
    novo->info = valor;
    novo->prox = NULL;

    if(f->ini == NULL){
        f->ini = novo;
        f->fim = novo;
    }else{
        f->fim->prox = novo;
        f->fim = novo;
    }

}
Lista* fila_retira(Fila* f){
    Lista* aux = NULL;

    if(f->ini != NULL){
        aux = f->ini;
        f->ini = f->ini->prox; // não precisa verificar se é elemento único para executar essa linha, porque f->ini->prox pode ser igual a NULL
        if(f->ini == NULL){ // mas se a fila ficou vazia (f->ini == NULL) precisamos atualizar o ponteiro de f->fim para NULL
            f->fim = NULL;
        }
        aux->prox = NULL;
    }

    return aux;
}

void fila_apagaElemento(Fila* f){
    Lista* aux = fila_retira(f);
    if(aux!=NULL){
        free(aux);
        aux = NULL;
    }
}

void fila_libera(Fila* f){
    while(f->ini != NULL){
        fila_apagaElemento(f);
    }
}
int fila_vazia(Fila* f){
    return (f->ini == NULL);
}

/** RESPOSTA AO ENUNCIADO DO PROBLEMA */
// corrigir essa função e implementar com uma fila
Pilha* pilha_inverte(Pilha* P){
    if(pilha_vazia(P)){
        return P;
    }
    Lista* aux = NULL;
    Fila* f = fila_criaPonteiro();

    while(!(pilha_vazia(P))){
        aux = pop(P);
        fila_insere(f,aux->info);
        free(aux);
    }
    while(!(fila_vazia(f))){
        aux = fila_retira(f);
        push(P, aux->info);
        free(aux);
    }
    return P;
}

// FUNÇÃO PRINCIPAL
int main(){
    Pilha* p1;
    p1 = criaPilha();

    int i = 0, tam, num;

    printf("Insira o tamanho para a pilha := ");
    scanf("%d",&tam);

    while(i < tam){
        printf("Insira o %d.o elemento: ", i+1);
        scanf("%d",& num);
        push(p1, num);
        i++;
    }
    pilha_imprime(p1);
    p1 = pilha_inverte(p1);
    pilha_imprime(p1);

}
