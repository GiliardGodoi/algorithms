/*
    Árvore N-árias

    Árvores binárias não são boas se com uma quantidade grande de dados (nós). Expandir em altura.


    Definição 1. Uma árvore que pode ter até N filhos.
    Def. 2. árvore que pode ter número arbitrario de filhos.

    Estrutura básica:

    {
        chave
        filho (primogênito)
        irmão 
    }    
*/
#include<stdlib.h>
#include<stdio.h>
#include <windows.h>
#define true 1
#define false 0

typedef int bool;
typedef int TIPOCHAVE;

typedef struct no {
    TIPOCHAVE chave;
    struct no *primFilho;
    struct no *proxIrmao;
}NO;

typedef NO* PONT;

// cria um novo no
PONT criaNO(TIPOCHAVE chave){
    PONT novo = (PONT) malloc(sizeof(NO));
    novo->primFilho = NULL;
    novo->proxIrmao = NULL;
    novo->chave = chave;

    return novo;
}

//inicialização;
PONT inicializa(TIPOCHAVE chave){
    return (criaNO(chave));
}
// busca
PONT buscaChave(TIPOCHAVE chave, PONT raiz){
    if(raiz == NULL){
        return NULL;
    }
    if(raiz->chave == chave){
        return raiz;
    }
    PONT p = raiz->primFilho;
    while(p){
        PONT resp = buscaChave(chave,p);
        if(resp){
            return resp;
        }
        p = p->proxIrmao;
    }
    return NULL;
}
// inserção;
bool insere(PONT raiz, TIPOCHAVE novaChave, TIPOCHAVE chavePai){
    PONT pai = buscaChave(chavePai,raiz);
    if(!pai){
        return false;
    }
    PONT filho = criaNO(novaChave);
    PONT p = pai->primFilho;
    if(!p){
        pai->primFilho = filho;
    }else{
        while(p->proxIrmao){
            p = p->proxIrmao;
        }
        p->proxIrmao = filho;
    }
    return true;
}

// exibir

void exibirArvore(PONT raiz){
    if(raiz==NULL){
        return; // retorna com void, putz!!
    }
    printf("%d(",raiz->chave);
    PONT p = raiz->primFilho;
    while(p){
        exibirArvore(p);
        p = p->proxIrmao;
    }
    printf(")");
}

int main(){
    exit(0);
}