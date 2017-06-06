#include <stdio.h>
#include <stdlib.h>

typedef struct Lista
{
    int elem;
    struct Lista *prox;
}Lista;

Lista* lst_cria(void);
void lst_libera(Lista* l);
Lista* lst_insere(Lista* l, int i);
Lista* lst_insereFim(Lista* l, int i);
Lista* lst_inserePos(Lista *l, int i, int pos);
Lista* lst_retira(Lista* l, int v);
int lst_vazia(Lista* l);
Lista* lst_busca(Lista* l, int v);
void lst_imprime(Lista* l);


/* função de criação: retorna uma lista vazia */
Lista* lst_cria(void)
{
    return NULL;
}


void lst_libera(Lista* l)
{
    Lista* p = l->prox;
    while(p->prox!=l){
      Lista* t = p->prox;
      free(p);
      p = t;
    }
    free(p);
}

/*função insere no inicio da lista*/
Lista* lst_insere(Lista* l, int i)
{
    if(l==NULL){
       Lista* novo = (Lista*) malloc(sizeof(Lista));
       novo->elem = i;
       novo->prox = novo;
       return novo;
    }else{
       Lista *p =l;
       while (p->prox !=l){
             p=p->prox;
       }
       Lista* novo = (Lista*) malloc(sizeof(Lista));
       novo->elem = i;
       novo->prox = l;
       p->prox=novo;
       return novo;
    }
}

/*função insere no final da lista*/
Lista* lst_insereFim(Lista* l, int i)
{
    if(l==NULL){
       Lista* novo = (Lista*) malloc(sizeof(Lista));
       novo->elem = i;
       novo->prox = novo;
       return novo;
    }else{
       Lista *p =l;
       while (p->prox !=l){
             p=p->prox;
       }

       Lista* novo = (Lista*) malloc(sizeof(Lista));
       novo->elem = i;
       p->prox = novo;
       novo->prox = l;
       return l;
    }
}

/*
* Insere em qualquer posicao da lista
*/
Lista* lst_inserePos(Lista *L,int i, int pos)
{
    Lista *novo=NULL,*ant=NULL,*aux=NULL;
    novo=(Lista*)malloc(sizeof(Lista));
    novo->prox=NULL;
    novo->elem=i;
    if(lst_vazia(L))
        return novo;
    aux=L;
    while((aux!=NULL)&&(aux->elem!=pos))
    {
        ant=aux;
        aux=aux->prox;
    }
    if(aux==NULL)//Insere no fim
    {
       ant->prox=novo;
       novo->prox = L;
    }
    else
        if(ant==NULL) //Insere na primeira posicao
        {
            novo->prox=aux;
            Lista *p =L;
            while (p->prox !=L){
                    p=p->prox;
            }
            p->prox=novo;
            L=novo;
        }
        else //Insere no meio da lista
        {
            ant->prox=novo;
            novo->prox=aux;
        }
    return L;
}
/* função retira: retira elemento da lista */
Lista* lst_retira(Lista* l, int v)
{
    /* ponteiro para elemento anterior*/
    Lista* ant = NULL;
    Lista* p = l;
    /* ponteiro para percorrer a lista */
    /* procura elemento na lista, guardando anterior */
    while (p->prox != l && p->elem != v)
    {
        ant = p;
        p = p->prox;
    }

    /* verifica se achou elemento */
    if (p == NULL)
    /* não achou: retorna lista original*/
    return l;

    if (ant == NULL) {
        Lista *aux =l;
        while (aux->prox !=l){
                  aux=aux->prox;
        }
        l = p->prox; //Inicio da Lista
        aux->prox=l;
    }else {
        ant->prox = p->prox;
    }
    free(p);
    return l;
}

/*função vazia: retorna 1 se vazia ou 0 se não vazia */
int lst_vazia(Lista* l)
{
    return (l == NULL);
}

/*função busca: busca um elemento na lista */
Lista* busca(Lista* l, int v)
{
    Lista* p;
    for (p=l; p!=NULL; p = p->prox) {
        if (p->elem == v)
        return p;
    }
    /* não achou o elemento */
    return NULL;
}

void lst_imprime(Lista* l)
{
    Lista* p=l;
    if(!lst_vazia(l))do{
     printf("info = %d\n", p->elem);
     p=p->prox;
    }while(p!=l);
}


int main(){
    Lista* L=NULL;

    L = lst_insereFim(L,20);
     L = lst_insereFim(L,30);
     L = lst_insereFim(L,40);
     L = lst_insere(L,5);
     L = lst_insere(L,1);

    lst_imprime(L);

    lst_libera(L);

    return 0;
}
