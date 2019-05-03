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

PONT criarNo(TIPOCHAVE chave){
    PONT novoNo = (PONT) malloc(sizeof(NO));
    novoNo->esq = NULL;
    novoNo->dir = NULL;
    novoNo->chave = chave;
    return novoNo;
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

PONT contem(TIPOCHAVE chave, PONT raiz){
    if(raiz == NULL){
        return NULL;
    }else if(raiz->chave == chave){
        return raiz;
    }else if(chave < raiz->chave){
        return contem(raiz->esq);
    }else if(chave > raiz->chave){
        return contem(raiz->dir);
    }
}

//inorder transversal
int numeroNos(PONT raiz){
    if(!raiz){
        return 0;
    }
    return (numeroNos(raiz->esq) + 1 + numeroNos(raiz->dir));
}

int exibirArvore(PONT raiz){

}

/*
    Busca binária não recursiva. Devovle o ponteiro do nó buscado.
    Abastece o pai com o ponteiro para o nó pai deste.
*/
PONT buscaNo(PONT raiz, TIPOCHAVE chave, PONT *pai){
    PONT atual = raiz;
    *pai = NULL;

    while(atual){
        if(atual->chave == chave){
            return atual;
        }
        *pai = atual;
        if(chave < atual->chave){
            atual = atual->esq;
        }else{
            atual = atual->dir;
        }
        return NULL;
    }

}

int removeNo(PONT raiz, chave){
    PONT pai, no, p, q;
    no = buscaNo(raiz,chave,&pai);
    if(no==NULL){
        return raiz;
    }

    if(!no->esq || !no->dir){
        if(!no->esq){
            q = no->dir;
        }else{
            q = no->esq;
        }
    }else{
        p = no;
        q = no->esq;
        while(q->dir){
            p = q;
            q = q->dir;
        }

        if( p != no){
            p->dir = q->esq;
            q->esq = no->esq;
        }
        q->dir = no->dir;
    }
    if(!pai){
        free(no);
        return q;
    }

    if(chave < pai->chave){
        pai->esq = q;
    }else{
        pai->dir = q;
    }
    free(no);
    return raiz;
}
int main(){

}