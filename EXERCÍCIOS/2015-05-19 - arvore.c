#include<stdlib.h>
#include<stdio.h>

typedef struct arv{
    int info;
    struct arv* sae;
    struct arv* sad;
}Arv;

Arv* criaNo(int num){
    Arv* novo;
    novo = (Arv*) malloc(sizeof(Arv));
    novo->sad = NULL;
    novo->sae = NULL;
    novo->info = num;

    return novo;
}

int contarNo(Arv* v){
    int x = 0;
    if(v!= NULL){
        x += contarNo(v->sae);
        x += contarNo(v->sad);
        x++;
    }

    return x;
}

void imprime(Arv* v){
    if(v!=NULL){
        printf("%d  ",v->info);
        imprime(v->sae);
        imprime(v->sad);
    }
}

Arv* insereABB(Arv* A, int num){
    if(A==NULL){
        A = criaNo(num);
    }else if(A->info > num){
        A->sad = insereABB(A->sad, num);
    }else if(A->info < num){
        A->sae = insereABB(A->sae, num);
    }
    return A;
}

int main(){

    Arv* R = NULL;
    int i = 0;
    int num;

    for(i = 0; i < 50; i++){
        num = rand()%500;
        R = insereABB(R, num);
    }

    imprime(R);

    printf("NUMERO DE NOS -> %d ",contarNo(R));

}
