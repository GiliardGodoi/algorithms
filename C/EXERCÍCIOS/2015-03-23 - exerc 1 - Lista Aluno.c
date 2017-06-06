#include<stdlib.h>
#include<stdio.h>
#include<string.h>

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

Lista* insereFim(Lista* L);
float calculaMedia(Lista * aux);
int retornaQuantAbaixoMedia(Lista* L);
void removePiorMedia(Lista *L);

int main(){
    Lista *L = NULL;
    int i;
    for(i= 0; i < 5; i++){
      L = insereFim(L);
    }
    printf("A media do primeiro aluno: %f", calculaMedia(L));



    return 0;
}
Lista* insereFim(Lista* L){
    Lista *novo, *aux;
    aux = L;
    novo = (Lista *) malloc(sizeof(Lista));
    novo->prox = NULL;
    novo->aluno = (Aluno *) malloc(sizeof(Aluno));
    //char nome[40];
    //int RA;
    //float notaAux;
    printf("\n**  INSERIR ALUNO NOVO  **");
    fflush(stdin);
    printf("\nDigite o nome: ");
    scanf("%[^\n]s",novo->aluno->nome);
    //strcpy(novo->aluno->nome, nome);
    printf("Digite o RA: ");
    scanf("%d", &novo->aluno->RA);
    //novo->aluno->RA = RA;
    printf("Digite a nota P1: ");
    scanf("%f",&novo->aluno->P1);
    //novo->aluno->P1 = notaAux;
    printf("Digite a nota P2: ");
    scanf("%f",&novo->aluno->P2);
    //novo->aluno->P2 = notaAux;
    printf("Digite a nota Trabalho: ");
    scanf("%f",&novo->aluno->T);
    //novo->aluno->T = notaAux;
    printf("digite a nota da APS: ");
    scanf("%f",&novo->aluno->APS);
    //novo->aluno->APS = notaAux;

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

Lista* insereInicio(Lista *L){
    Lista *novo;
    novo->aluno = (Aluno*) malloc(sizeof(Aluno));
    printf("\n**  INSERIR ALUNO NOVO  **");
    fflush(stdin);
    printf("\nDigite o nome: ");
    scanf("%[^\n]s",novo->aluno->nome);
    //strcpy(novo->aluno->nome, nome);
    printf("Digite o RA: ");
    scanf("%d", &novo->aluno->RA);
    //novo->aluno->RA = RA;
    printf("Digite a nota P1: ");
    scanf("%f",&novo->aluno->P1);
    //novo->aluno->P1 = notaAux;
    printf("Digite a nota P2: ");
    scanf("%f",&novo->aluno->P2);
    //novo->aluno->P2 = notaAux;
    printf("Digite a nota Trabalho: ");
    scanf("%f",&novo->aluno->T);
    //novo->aluno->T = notaAux;
    printf("digite a nota da APS: ");
    scanf("%f",&novo->aluno->APS);
    //novo->aluno->APS = notaAux;

}


float calculaMedia(Lista * aux){
    float media;
    media = (aux->aluno->P1*0.4) + (aux->aluno->P2*0.4) + (aux->aluno->T*0.1) + (aux->aluno->APS*0.1);
    return media;

}

int retornaQuantAbaixoMedia(Lista* aux){
    int cont = 0;
    while(aux != NULL){
        if( calculaMedia(aux) < 6){
            cont++;
        }
        aux = aux->prox;
    }
    return cont;
}
/*
void removePiorMedia(Lista *L){
    float media = 0.0, piorMed;
    Lista *aux, *piorAluno;
    aux = L;

    while(aux!= NULL){
            media = calculaMedia(aux);
            if()



    }
}
*/
