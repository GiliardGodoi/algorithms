#include<stdlib.h>
#include<stdio.h>
#define true 1
#define false 0

typedef int bool
typedef int TIPOCHAVE

typedef struct aux{
    TIPOCHAVE chave;
    struct aux *esq, *dir;
}NO;

typedef NO* PONT;

PONT inicializa(){
    return NULL;
}

PONT adiciona(PONT raiz, PONT no){
    if(raiz == NULL){
        return no;
    }
    if(no->chave < raiz->chave){
        raiz->esq = adiciona(raiz->esq, no);
    }else if(no-chave > raiz->chave){
        raiz->dir = adiciona(raiz-dir, no);
    }

    return raiz;
}

PONT criarNo(TIPOCHAVE chave){
    PONT novoNo = (PONT) malloc(sizeof(NO));
    novoNo->esq = NULL;
    novoNo->dir = NULL;
    novoNo->chave = chave;
    return novoNo;
}

int main(){
    
}