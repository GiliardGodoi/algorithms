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

void imprime(Arv* r){
    if(r!=NULL){
        printf("%d  ",r->info);
        if(r->sad!=NULL){
            imprime(r->sad);
        }
        if(r->sae!=NULL){
            imprime(r->sae);
        }
    }
}

int main(){

    Arv* R;
    R = criaNo();
    R->info = 5;

    Arv* V;
    V = criaNo();
    V->info = 8;

    Arv* A;

    A = criaNo();
    A->info = 10;

    R->sad = V;
    R->sae = A;

   /* printf("%d  ",R->info);
    printf("%d  ",R->sae->info);
    printf("%d  ",R->sad->info); */

    imprime(R);

}
