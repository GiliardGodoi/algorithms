#include <stdio.h>
#include <stdlib.h>

typedef struct Aluno{
   char nome[40];
   int RA;
   float P1;
   float P2;
   float T;
   float APS;
}Aluno;

typedef struct Lista{
   Aluno *aluno;
   struct Lista *prox;
}Lista;

Lista* lst_cria(void);
void lst_libera(Lista* l);
Lista* lst_insere(Lista* l);
void lst_insereFim(Lista* l);
Lista* lst_retira(Lista* l, int v);
int lst_vazia(Lista* l);
Lista* lst_busca(Lista* l, int v);
void lst_imprime(Lista* l);


/* funcao de criacao: retorna uma lista vazia */
Lista* lst_cria(void)
{
   return NULL;
}


int contaNotas(Lista* l){
  int cont=0;
  if(l==NULL)
    return 0;

  while(l!=NULL){
      if((l->aluno->P1*0.4 +
          l->aluno->P2*0.4 +
          l->aluno->T*0.1  +
          l->aluno->APS*0.1) <6)
          cont++;

       l=l->prox;
  }
  return cont;
}

void lst_libera(Lista* l)
{
    Lista* p = l;
    while (p != NULL) {
        Lista* t = p->prox;
        free(p->aluno);
        free(p);
        p = t;
    }
}

/*funcao insere no inicio da lista*/
Lista* lst_insere(Lista* l)
{
    setbuf(stdin, NULL); //Limpa o buffer do teclado
    Lista* novo = (Lista*) malloc(sizeof(Lista));
    Aluno* aluno = (Aluno*) malloc(sizeof(Aluno));
    printf("Entre com o nome do Aluno: ");
    scanf("%[^\n]s",aluno->nome);
    printf("Entre com o RA do Aluno: ");
    scanf("%d", &aluno->RA);
    printf("Entre com a Nota 1 do Aluno: ");
    scanf("%f", &aluno->P1);
    printf("Entre com a Nota 2 do Aluno: ");
    scanf("%f", &aluno->P2);
    printf("Entre com a Nota do Trabalho do Aluno: ");
    scanf("%f", &aluno->T);
    printf("Entre com a Nota da APS do Aluno: ");
    scanf("%f", &aluno->APS);
    novo->aluno = aluno;
    novo->prox = l;
    return novo;
}

/*função insere no final da lista*/
void lst_insereFim(Lista* l)
{
    Lista *p =l;
    while (p->prox !=NULL){
        p=p->prox;
    }
    setbuf(stdin, NULL); //Limpa o buffer do teclado
    Lista* novo = (Lista*) malloc(sizeof(Lista));
    Aluno* aluno = (Aluno*) malloc(sizeof(Aluno));
    printf("Entre com o nome do Aluno: ");
    scanf("%[^\n]s",aluno->nome);
    printf("Entre com o RA do Aluno: ");
    scanf("%d", &aluno->RA);
    printf("Entre com a Nota 1 do Aluno: ");
    scanf("%f", &aluno->P1);
    printf("Entre com a Nota 2 do Aluno: ");
    scanf("%f", &aluno->P2);
    printf("Entre com a Nota do Trabalho do Aluno: ");
    scanf("%f", &aluno->T);
    printf("Entre com a Nota da APS do Aluno: ");
    scanf("%f", &aluno->APS);
    novo->aluno = aluno;
    novo->prox=NULL;
    p->prox = novo;
}

/* funcao retira: retira aluno da lista */
Lista* lst_retira(Lista* l, int v)
{
    /* ponteiro para elemento anterior*/
    Lista* ant = NULL;
    Lista* p = l;
    /* ponteiro para percorrer a lista */
    /* procura elemento na lista, guardando anterior */
    while (p != NULL && p->aluno->RA != v)
    {
        ant = p;
        p = p->prox;
    }

    /* verifica se achou elemento */
    if (p == NULL)
    /* não achou: retorna lista original*/
    return l;

    if (ant == NULL) { l = p->prox; }
    else { ant->prox = p->prox; }
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
        if (p->aluno->RA == v)
        return p;
    }
    /* não achou o elemento */
    return NULL;
}

void lst_imprime(Lista* l)
{
    Lista* p;
    for (p = l; p != NULL; p = p->prox){
    printf("%s\n%d\n%.2f\n%.2f\n%.2f\n%.2f\nMedia: %.2f\n",
            p->aluno->nome, p->aluno->RA, p->aluno->P1,
            p->aluno->P2, p->aluno->T, p->aluno->APS,
            (p->aluno->P1*0.4 +
            p->aluno->P2*0.4 +
            p->aluno->T*0.1  +
            p->aluno->APS*0.1)
           );
    }
}


int main(){

    /* declara uma lista nao iniciada*/
    Lista* l,*aux;
    /* inicia lista vazia*/
    l = lst_cria();
    l = lst_insere(l);
      l = lst_insere(l);
      lst_insereFim(l);
      lst_insereFim(l);
    lst_imprime(l);

    /*
        * Retorna a quantidade de alunos com media inferior a 6
        */
    printf("\n qtde: %d\n",contaNotas(l));


       /*
        * Encontra o aluno com a pior media
        */
       int tempRA, tempMedia=10;
       aux=l;
       while(aux!=NULL){
        if((aux->aluno->P1*0.4 +
            aux->aluno->P2*0.4 +
            aux->aluno->T*0.1  +
            aux->aluno->APS*0.1)<tempMedia)
            {
              tempMedia = aux->aluno->P1*0.4 + aux->aluno->P2*0.4 + aux->aluno->T*0.1  + aux->aluno->APS*0.1;
              tempRA = aux->aluno->RA;
            }
            aux=aux->prox;
    }

       /*
        * Remove o aluno com a pior media
        */
       l = lst_retira(l,tempRA);

    lst_imprime(l);

    lst_libera(l);

    return 0;
}
