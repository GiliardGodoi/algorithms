/*  UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - Campus de Cornélio Procópio

    DISCIPLINA: IF53B - ESTRUTURA DE DADOS - TURMA - N13
    Prof. Dr. Danilo Sipoli Sanches
    ALUNO: Giliard Almeida de Godoi - RA 1581597

    2015-05-18 - arvore
*/
#include<stdlib.h>
#include<stdio.h>

typedef struct arv{
    int info;
    struct arv* sae;
    struct arv* sad;
}Arv;

Arv* criaNo(){
    Arv* novo;
    novo = (Arv*) malloc(sizeof(Arv));
    novo->sad = NULL;
    novo->sae = NULL;

    return novo;
}

void imprime(Arv* v){
    if(v!=NULL){
        printf("%d  ",v->info);
        imprime(v->sae);
        imprime(v->sad);
    }
}

Arv* insereAB(Arv* sae, Arv* sad, int num){
    Arv* novo;
    novo = (Arv*) malloc(sizeof(Arv));
    novo->info = num;
    novo->sae = sae;
    novo->sad = sad;

    return novo;
}
/*
int contarNo(Arv* v){
    int x = 0;
    if(v != NULL){
        x = 1;
        x = x + contarNo(v->sae);
        x = x + contarNo(v->sad);

    }else{
        return 0;
    }
    return x;
}
*/

int contarNo(Arv* v){
    int x = 0;
    if(v!= NULL){
        x += contarNo(v->sae);
        x += contarNo(v->sad);
        x++;
    }

    return x;
}

int main(){

    Arv* r;
    r = insereAB( insereAB(
                           insereAB(NULL, NULL, 6),
                           insereAB(NULL, NULL, 7) ,8),
                           insereAB(insereAB(NULL, NULL, 13),
                           insereAB(NULL, NULL, 15) ,10),
                           5);

    imprime(r);

    printf("\n\n  -> %d ", contarNo(r));


}
