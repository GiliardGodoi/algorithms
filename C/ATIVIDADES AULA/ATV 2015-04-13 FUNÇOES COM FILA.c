#include<stdlib.h>
#include<stdio.h>

typedef struct lista{
    int info;
    struct lista* prox;
}Lista;

typedef struct fila{
    Lista* ini;
    Lista* fim;
}Fila;

Fila* ponteiroFila(){
    Fila *F = NULL;
    F = (Fila*) malloc(sizeof(Fila));
    F->ini = NULL;
    F->fim = NULL;

    return F;
}

void insereElementoFila(Fila* F, int valor){
    Lista *novo;
    novo = (Lista*) malloc(sizeof(Lista));
    novo->info = valor;
    novo->prox = NULL;
    if(F->ini == NULL){
        F->ini = novo;
    }else{
        F->fim->prox = novo;
    }
        F->fim = novo;
}

void apagaElementoFila(Fila* F){
    Lista *aux;
    if(F->ini!= NULL){ //condição de Fila vazia
        aux = F->ini;
        if(F->ini == F->fim){ //
            F->ini = NULL;
            F->fim = NULL;
        }else{
            F->ini = aux->prox;
        }
        free(aux);
        aux = NULL;
    }
}

/*
void removeFila(Fila* F){
    Lista *aux = F->ini;
    if(aux!=NULL){
        F->ini = F->ini->prox;
        free(aux);
        aux= NULL;
    }
    if(F->ini == NULL){
        F->fim = NULL;
    }
}


*/

void apagaTodosElementosFila(Fila* F){
    while(F->ini!= NULL && F->fim!=NULL){
        apagaElementoFila(F);
    }

}

int quantidadeElementoFila(F){

}

void imprimeFila(Fila* F){
    Lista* aux = NULL;
    if(F->ini != NULL){
        aux = F->ini;
        while(aux!=NULL){
            printf("%d\t",aux->info);
            aux = aux->prox;
        }
    }else{
        printf("\nFila vazia!!\n");
    }
}


int main(){
    Fila *F;
    F = ponteiroFila();
    int i;
    imprimeFila(F);
    for(i=0; i <10; i++){
        insereElementoFila(F,i*10);
    }
    imprimeFila(F);
    apagaElementoFila(F);
    imprimeFila(F);
    apagaTodosElementosFila(F);
    imprimeFila(F);


}
