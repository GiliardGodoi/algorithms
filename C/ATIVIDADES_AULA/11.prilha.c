/*  UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - Campus de Cornélio Procópio

    DISCIPLINA: IF53B - ESTRUTURA DE DADOS - TURMA - N13
    Prof. Dr. Danilo Sipoli Sanches
    ALUNO: Giliard Almeida de Godoi - RA 1581597

    ATV 2015-04-14 - PILHA
*/
#include<stdlib.h>
#include<stdio.h>

typedef struct lista{
    int info;
    struct lista* prox;
}Lista;

typedef struct pilha{
    Lista* topo;
}Pilha;

void push(Pilha* P, int valor){ // empilha
    if(P!=NULL){
        Lista* novo;
        novo = (Lista*) malloc(sizeof(Lista));
        novo->info = valor;
        if(P->topo!=NULL){
            //escreva o seu c�digo aqui
            novo->prox = P->topo;
            P->topo = novo;
        }else{
            novo->prox = NULL;
            P->topo = novo;
        }

    }

}
void pop(Pilha*P){ // desempilha
    if(P!=NULL){
        if(P->topo!=NULL){
                Lista* aux;
                aux = P->topo->prox;
                free(P->topo);
                P->topo = aux;
        }
    }

}
void imprimePilha(Pilha* P){
    Lista* aux;
    if(P!=NULL){
        aux = P->topo;
        while(aux!= NULL){
            printf("\t%d",aux->info);
            aux = aux->prox;
        }
    }

}

int main(){
    Pilha* p;
    p = (Pilha*)malloc(sizeof(Pilha));
    p->topo = NULL;
    int i;
    push(p,20);
/*
    Lista* novo;
    novo = (Lista*) malloc(sizeof(Lista));
    novo->info = 10;
    novo->prox = NULL;
    p->topo = novo;

  //  printf("%d\n\n",p->topo->info);

    Lista* L2;
    L2 = (Lista*)malloc(sizeof(Lista));
    L2->info = 20;
    L2->prox = p->topo;
    p->topo = L2;
*/
    for(i=1; i<7;i++){
        push(p,i*10);
    }
    imprimePilha(p);
    printf("\n\n");
    for(i=1;i<3;i++){
        pop(p);
    }
    imprimePilha(p);
}
