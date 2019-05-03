/*
    Uma trie (retrieval) é uma árvore N-ária projetada para recuperação rápida de chaves de busca.

    - Não armazena nenhuma chave explicitamente. Chaves são codificadas nos caminhos a partir da raiz.

*/
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include <windows.h>
#define true 1
#define false 0
#define N_ALFABETO 26

typedef int bool;
typedef bool TIPORET;

typedef struct no {
    TIPOCHAVE chave;
    struct no *filhos[N_ALFABETO];
    TIPORET fim;
}NO;

PONT criaNO(){
    PONT p = NULL;
    p = (PONT) malloc(sizeof(NO));
    if(p){
        p->fim = false;
        int i;
        for(i = 0; i < N_ALFABETO; i++){
            p->filhos[i] = NULL;
        }
    }
    return p;
}


PONT inicializa(){
    return criaNO();
}

int mapearIndice(char c){
    return ( (int) c - (int) 'a');
}

void inserir(PONT raiz, char *chave){
    int nivel;
    int comprimento = strlen(chave);
    int i;

    PONT p = raiz;
    for(nivel=0; nivel < comprimento; nivel++){
        i = mapearIndice(chave[nivel]);
        if(!p->filhos[i]){
            p->filhos[i] = criaNO();
        }
        p = p->filhos[i];
    }
    p->fim = true;
}
TIPORET busca(PONT raiz, char *chave){
    int nivel;
    int comprimento = strlen(chave);
    int i;

    PONT p = raiz;
    for(nivel=0; nivel < comprimento; nivel++){
        i = mapearIndice(chave[nivel]);
        if(!p->filhos[i]){
            return false;
        }
        p = p->filhos[i];
    }
    return(p->fim);
}

int main(){
    exit(0);
}