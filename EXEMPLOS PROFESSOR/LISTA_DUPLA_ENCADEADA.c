#include <stdio.h>
#include <stdlib.h>

typedef struct lista
{
    int info;
    struct lista *ant;
    struct lista *prox;
}Lista;

//Prototipos de funcoes lista duplamente encadeada
Lista* insereFim(Lista *L,int info);
Lista* insereInicio(Lista *L,int info);
void Mostrar_lista(Lista *L);
Lista* Liberar_lista(Lista *L);
Lista* removerLista(Lista *L, int info);

//funcoes lista dublamente encadeada
Lista* insereFim(Lista *L,int info)
{
    Lista *novo,*aux;
    novo=(Lista*)malloc(sizeof(Lista));
    novo->ant=NULL;
    novo->prox=NULL;
    novo->info=info;
    if(L==NULL)
        return novo;
    else
    {
        aux=L;
        while(aux->prox!=NULL)
            aux=aux->prox;
        aux->prox=novo;
        novo->ant=aux;
    }
    return L;
}

Lista* insereInicio(Lista *L,int info)
{
    Lista *novo;
    novo=(Lista*)malloc(sizeof(Lista));
    novo->ant=NULL;
    novo->prox = NULL;
    novo->info = info;
    if(L == NULL)
        return novo;
    else
    {
        novo->prox=L;
        L->ant=novo;
        return novo;
    }
}

Lista* removerLista(Lista *L, int info)
{
    Lista *aux=L,*ant=NULL;
    while((aux!=NULL)&&(aux->info!=info))
    {
        ant=aux;
        aux=aux->prox;
    }
    if(aux==NULL)
       return L;

    if(ant==NULL)
    {
        L=aux->prox;
        if(L!=NULL)
          L->ant=NULL;
        free(aux);
    }
    else
        if(aux->prox==NULL)
        {
            ant->prox=NULL;
            free(aux);
        }
        else
        {
            ant->prox=aux->prox;
            aux->prox->ant=ant;
            free(aux);
        }
    return L;
}

void Mostrar_lista(Lista *L)
{
    Lista *aux=L;
    if(L==NULL){
        printf("Lista Vazia.\n");
    }else{
        while(aux!=NULL){
            printf("%d ",aux->info);
            aux=aux->prox;
        }
    }
    printf("\n");
}

Lista* Liberar_lista(Lista *L)
{
    Lista *aux;
    while(L!=NULL)
    {
        aux=L->prox;
        free(L);
        L=aux;
    }
    printf("\nLista Liberada!!!\n");
    return NULL;
}

int main()
{

    Lista *L=NULL;

    L=insereInicio(L, 10);
    L=insereFim(L, 20);
    L=insereInicio(L, 30);

    Mostrar_lista(L);

    L = removerLista(L, 10);
    L = removerLista(L, 30);

    Mostrar_lista(L);

    L = removerLista(L, 20);


    L=Liberar_lista(L);

    return 0;
}
