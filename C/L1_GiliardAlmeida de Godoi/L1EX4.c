/*  UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - Campus de Cornélio Procópio

    ALUNO: Giliard Almeida de Godoi - RA 1581597
    DISCIPLINA: IF53B - ESTRUTURA DE DADOS - TURMA - N13
    Prof. Danilo Sipoli Sanches

    LISTA DE EXERCÍCIOS REFERENTE À APS 1 -
    DATA DA ENTREGA: 04/05/2015
*/

/* QUESTÃO  4 -
    Faça um programa para testar se duas pilhas (representadas por lista encadeadas) P1 e P2 são
iguais;

*/
#include<stdio.h>
#include<stdlib.h>
typedef struct lista{
    int info;
    struct lista *prox;
}Lista;

typedef struct pilha{
    Lista* topo;
}Pilha;

Pilha* criaPilha(){
    Pilha* P;
    P = (Pilha*) malloc(sizeof(Pilha));
    P->topo = NULL;
    return P;
}
void push(Pilha* P, int valor){
    Lista* novo;
    novo = (Lista*) malloc(sizeof(Lista));
    novo->info = valor;
    novo->prox = P->topo;
    P->topo = novo;
}
Lista* pop(Pilha* P){
    if(pilha_vazia(P)){
        return NULL;
    }
    Lista* aux;
    aux = P->topo;
    P->topo = P->topo->prox;
    aux->prox = NULL;
    return aux;
    // aqui a ordem das instruções alternam o resultado sim!!
}
int pilha_vazia(Pilha* P){
    return (P->topo == NULL);
    // retorna UM para verdadeiro
    // ZERO para falso
}
void pilha_imprime(Pilha* P){
    Lista* aux = P->topo;
    printf("\n");
    while(aux!=NULL){
            printf("%d  ",aux->info);
            aux = aux->prox;
    }
    printf("\n");
}

/** RESPOSTA AO ENUNCIADO DO PROBLEMA

    A fução verifica se duas pilhas são iguais, isto é, se os elementos de posições correspondentes
    são iguais.

    A função retorna UM  para o caso de verdadeiro e  ZERO para o caso ser de a condição não ser
    satisfeita, isto é, for falso
    */
int pilha_VerificarIguais(Pilha* P1, Pilha* P2){
    int resultado = 1;
    int controle = 1;
    if(pilha_vazia(P1) || pilha_vazia(P2)){
        return 0;
    }
    Lista* aux1 = P1->topo;
    Lista* aux2 = P2->topo;
    while(controle){
        if(aux1->info != aux2->info){
            controle = 0;
            resultado = 0;
        }
        aux1 = aux1->prox;
        aux2 = aux2->prox;
        if(aux1 == NULL && aux2 == NULL){ // as duas listas chegaram ao fim
            controle = 0;
        }else if(aux1 == NULL && aux2!=NULL){ // a primeira lista chegou ao fim e a outra não
            controle = 0;
            resultado = 0;
        }else if(aux1 != NULL && aux2 == NULL){ // a segunda chegou ao fim a outra não
            controle = 0;
            resultado = 0;
        }
    }
    return resultado;
}

// FUNÇÃO PRINCIPAL
int main(){
Pilha *p1, * p2;
    p1 = criaPilha();
    p2 = criaPilha();
    int i = 0, tam, num;

    printf("Insira o tamanho para a PRIMEIRA pilha := ");
    scanf("%d",&tam);

    while(i < tam){
        printf("Insira o %d.o elemento: ", i+1);
        scanf("%d",& num);
        push(p1, num);
        i++;
    }
    i = 0;

    printf("Insira o tamanho para a SEGUNDA pilha := ");
    scanf("%d",&tam);

    while(i < tam){
        printf("Insira o %d.o elemento: ", i+1);
        scanf("%d",& num);
        push(p2, num);
        i++;
    }
    printf("PRIMEIRA PILHA");
    pilha_imprime(p1);

    printf("SEGUNDA PILHA");
    pilha_imprime(p2);

    printf("RESULTADO\n\tZERO -> diferente\n\tUM -> iguais\n\t:= %d", pilha_VerificarIguais(p1,p2));



}

