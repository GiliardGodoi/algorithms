#include<stdlib.h>
#include<stdio.h>

typedef struct lista{
    int info;
    struct lista* prox;
}Lista;

Lista* insereInicio(Lista* L, int num){
    Lista* novo;
    novo = (Lista*) malloc(sizeof(Lista));
    novo->info = num;
    if(L == NULL){
        novo->prox = NULL;
        return novo;
    }
    novo->prox = L;
    return novo;
}

Lista* insereFim(Lista *L, int num){
    Lista *novo, *aux;
    aux = L;
    novo = (Lista*) malloc(sizeof(Lista));
    novo->info = num;
    novo->prox = NULL;

    if(L == NULL){
        return novo;
    }else{
       while(aux->prox!=NULL){
            aux = aux->prox;
       }
       aux->prox = novo;
       return L;
    }
}

Lista* insereAlternado(Lista* L1, Lista* L2){
    Lista *aux1, *aux2, *aux3;
    Lista *L3;
    int cont = 4;
    L3 = L1;
    aux1 = L1->prox;
    aux2 = L2;
    aux3 = L3;
    while(aux1!=NULL || aux2!= NULL){
        if((cont%2)==1){
            aux3->prox = aux1;
            aux1 = aux1->prox;
            aux3 = aux3->prox;
            if(aux2==NULL){
                cont = 3;
            }else{
                cont = 4;
            }
        }
        if((cont%2)==0){
            aux3->prox = aux2;
            aux2 = aux2->prox;
            aux3 = aux3->prox;
            if(aux1==NULL){
                cont = 4;
            }else{
                cont = 3;
            }
        }
    }
    return L3;
}

Lista* inserePos(Lista* L, int pos, int valor){
    Lista *aux = L;
    Lista* ant = NULL, *novo;
    int cont = 1;
    while(aux!=NULL && cont < pos ){
        ant = aux;
        aux = aux->prox;
        cont++;
    }
    if(aux == NULL){
        return L;
    }else{
        novo = (Lista*) malloc(sizeof(Lista));
        novo->info = valor;
        ant->prox = novo;
        novo->prox = aux;
    }
    return L;

}
Lista* apagarCel(Lista *L, int valor){
    Lista* aux = L;
    Lista* ant = NULL;
    while(aux != NULL && aux->info!= valor){
        ant = aux;
        aux = aux->prox;

    }
    if(aux == NULL){
        return L;
    }
    if(ant == NULL){
         L = aux->prox;
    }else{
        ant->prox = aux->prox;
    }
    free(aux);
    return L;
}

Lista* apagarPos(Lista* L, int pos){
    Lista *aux = L, *ant = NULL;
    int cont = 1;
    if(pos <= 0){
        return L;
    }
    while(aux != NULL && cont < pos){
        ant = aux;
        aux = aux->prox;
        cont++;
    }
    if(aux == NULL){
        return L;
    }
    if(ant == NULL){
        L = aux->prox;
    }else{
        ant->prox = aux->prox;
    }
    free(aux);
    return L;
}

Lista* apagarImpar(Lista* L){
    Lista* aux = L;
    while(aux != NULL){
        if((aux->info%2)!= 0){
            printf("\nIMPAR: %d",aux->info);
            L = apagarCel(L, aux->info);
            aux = L;
        }else{
            aux = aux->prox;
        }
    }
    return L;
}

Lista* apagarLista(Lista * L){
    Lista* aux = L;
    while(aux!=NULL){
        L = L->prox;
        free(aux);
        aux = L;
    }
    return aux;
}

void imprimeLista(Lista *aux){
    printf("\n");
    while(aux != NULL){
        printf("\t%d",aux->info);
        aux = aux->prox;
    }
    printf("\n");
}
/*
Lista* listaInverte(Lista* L){
    Lista *novo = NULL;
    Lista *aux = L;
    while(aux!=NULL){
        novo = insereInicio(novo,aux->info);
        aux = aux->prox;
    }
    L = apagarLista(L);
    return novo;
}
*/
Lista* listaInverte(Lista * L){
    Lista* novo = NULL;
    Lista* aux = L;
    int pos = 1;
    while(aux!=NULL){
        novo = insereInicio(novo, aux->info);
        aux = apagarPos(aux,pos);
    }
    return novo;
}

Lista* inverteLista(Lista* aux){
    Lista *L1, *tmp;
    L1 = aux;
    aux = aux->prox;
    L1->prox = NULL;
    while(aux != NULL){
        tmp = aux;
        aux = aux->prox;
        tmp->prox = L1;
        L1 = tmp;
    }

    return L1;

}
int retornaMaior(Lista* L){
    if(L == NULL){
        return 0;
    }
    int maior = L->info;
    Lista* aux = L;
    while(aux!=NULL){
        if(maior < aux->info){
            maior = aux->info;
        }
        aux = aux->prox;
    }
    return maior;
}

int retornaMenor(Lista* L){
    if(L == NULL){
        return 0;
    }
    int menor = L->info;
    Lista* aux = L;
    while(aux != NULL){
        if(menor > aux->info){
            menor = aux->info;
        }
        aux = aux->prox;
    }
    return menor;
}

Lista* deslocaMaiorFim(Lista* L){
    int maior;
    maior = retornaMaior(L);
    L = apagarCel(L,maior);
    L = insereFim(L,maior);
    return L;
}

int main(){
    Lista *L1 = NULL;
    Lista *L2 = NULL;
    int i = 1;
    for(i = 1; i < 10; i++){
            if(i%2==1)
                L1 = insereFim(L1,i);
            if(i%2==0)
                L2 = insereFim(L2, i);
    }


    L1 = inserePos(L1, 3, 50);
    L1 = listaInverte(L1);
    L1 = inverteLista(L1);
    imprimeLista(L1);
    imprimeLista(L2);
    L1 = insereAlternado(L1,L2);
    L1 = insereInicio(L1, 101);
    L1 = deslocaMaiorFim(L1);
    //L1 = apagarLista(L1);
    //L1 = insereInicio(L1,40);
    //L1 = inverteLista(L1);
    imprimeLista(L1);
    printf("\nMAIOR = %d", retornaMaior(L1));
    printf("\nMENOR = %d", retornaMenor(L1));
   // imprimeLista(L1);
    /*
    L1 = apagarCel(L1, 7);
    imprimeLista(L1);
    L1 = inverteLista(L1);
    imprimeLista(L1);
    L1 = apagarImpar(L1);
    imprimeLista(L1);*/
    return 0;
}
