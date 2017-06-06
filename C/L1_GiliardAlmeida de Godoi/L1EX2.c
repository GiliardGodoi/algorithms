/*  UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ - Campus de Cornélio Procópio

    ALUNO: Giliard Almeida de Godoi - RA 1581597
    DISCIPLINA: IF53B - ESTRUTURA DE DADOS - TURMA - N13
    Prof. Danilo Sipoli Sanches

    LISTA DE EXERCÍCIOS REFERENTE À APS 1 -
    DATA DA ENTREGA: 04/05/2015
*/

/* QUESTÃO 2 -
        Uma estrutura DEQUE é um TAD Fila em que elementos podem ser inseridos e retirados de
ambas as extremidades da estrutura (estática ou dinâmica) APENAS. Outros tipos de inserção e
remoção (em outras posições) não são válidos. Escreva um programa com as funções
necessárias para implementar um DEQUE representado por uma lista duplamente encadeada.

*/
#include<stdio.h>
#include<stdlib.h>

typedef struct listaDupla{
    int info;
    struct listaDupla* prox;
    struct listaDupla* ant;
}Lista_Dupla;

typedef struct deque{
    Lista_Dupla* ini;
    Lista_Dupla* fim;
}Deque;

Deque* deque_criarDeque(){
    Deque* f;
    f = (Deque*) malloc(sizeof(Deque));
    f->ini = NULL;
    f->fim = NULL;

    return f;
}
int deque_verificaVazia(Deque* f){
    return (f->ini == NULL);
}
void deque_insereInicio(Deque* f, int valor){
    Lista_Dupla* novo;
    novo = (Lista_Dupla*) malloc(sizeof(Lista_Dupla));
    novo->info = valor;
    novo->ant = NULL;
    novo->prox = NULL;

    if(deque_verificaVazia(f)){
        f->ini = novo;
        f->fim = novo;
    }else{
        f->ini->ant = novo;
        novo->prox = f->ini;
        f->ini = novo;

    }
}
void deque_insereFim(Deque* f, int valor){
    Lista_Dupla* novo;
    novo = (Lista_Dupla*) malloc(sizeof(Lista_Dupla));
    novo->info = valor;
    novo->ant = NULL;
    novo->prox = NULL;

    if(deque_verificaVazia(f)){
        f->ini = novo;
        f->fim = novo;
    }else{
        f->fim->prox = novo;
        novo->ant = f->fim;
        f->fim = novo;
    }
}
Lista_Dupla* deque_retiraInicio(Deque* f){
    Lista_Dupla* aux = NULL;
    if(deque_verificaVazia(f)){
        return NULL;
    }else{
        aux = f->ini;
        f->ini = aux->prox;
        aux->prox = NULL;
        if(f->ini == NULL){ /* verifica se a fila ficou vazia */
            f->fim = NULL;
        }else{
            f->ini->ant = NULL;
        }
    }
    return aux;
}
Lista_Dupla* deque_retiraFim(Deque* f){
    Lista_Dupla* aux = NULL;
    if(deque_verificaVazia(f)){
        return NULL;
    }
    aux = f->fim;
    f->fim = aux->ant;
    aux->ant = NULL;

    if(f->fim == NULL){ /* verifica se a fila ficou vazia */
        f->ini = NULL;
    }else{
        f->fim->prox = NULL;
    }
    return aux;
}

void deque_apagaInicio(Deque* f){
    Lista_Dupla *aux = NULL;
    aux = deque_retiraInicio(f);
    if(aux!=NULL){
        free(aux);
        aux = NULL;
    }
}

void deque_apagaFim(Deque* f){
    Lista_Dupla* aux= NULL;
    aux = deque_retiraFim(f);
    if(aux!=NULL){
        free(aux);
        aux = NULL;
    }
}

void deque_imprime(Deque* f){
    Lista_Dupla* aux;
    aux = f->ini;
    if(deque_verificaVazia(f)){
        printf("\nFILA DEQUE VAZIA!! ... ");
    }
    printf("\n");
    while(aux!=NULL){
        printf("%d   ",aux->info);
        aux = aux->prox;
    }
    printf("\n");
}

void deque_liberaFila(Deque* f){
    while(!(deque_verificaVazia(f))){
        deque_apagaInicio(f);
    }
}
/** Função para popular a Fila Deque */
void deque_populaDeque(Deque* f){
    int i = 0, tam, num;
    if(deque_verificaVazia(f)){
        printf("\nTamanho da lista := ");
        scanf("%d",&tam);
        printf("\n");
        while(i < tam){
            printf("Insira o valor para a %d.o posicao := ", i+1);
            scanf("%d",&num);
            deque_insereInicio(f, num);
            i++;
    }
    }else{
        printf("\nJ\205 existe elementos na Fila Deque...");
    }
}

// FUNÇÃO PRINCIPAL
int main(){
    Deque* f = NULL;
    f = deque_criarDeque();
    char continuar = 's';
    int op = 0, num = 0;
    do{

            printf("\n                   ** ESCOLHA UMA OPCAO **\n \
                   1 - Popular Deque\n \
                   2 - Inserir Elemento no INICIO\n \
                   3 - Inserir Elemento no FIM\n \
                   4 - Apagar Elemento do INICIO\n \
                   5 - Apagar Elemento do FIM\n \
                   6 - IMPRIMIR FILA DEQUE\n \
                   7 - Liberar FILA DEQUE.\n \
                   -> ");
            scanf("%d",&op);
            switch(op){
                case 1:
                    deque_populaDeque(f);
                    break;
                case 2:
                    printf("\nInsira o valor := ");
                    scanf("%d",&num);
                    deque_insereInicio(f, num);
                    break;
                case 3:
                    printf("\nInsira o valor := ");
                    scanf("%d",&num);
                    deque_insereFim(f,num);
                    break;
                case 4:
                    deque_apagaInicio(f);
                    printf("\nINICIO APAGADO");
                    break;
                case 5:
                    deque_apagaFim(f);
                    printf("\nFIM APAGADO");
                    break;
                case 6:
                    deque_imprime(f);
                    break;
                case 7:
                    deque_liberaFila(f);
                    printf("\nFILA DEQUE LIBERADA");
                    break;
                default :
                    printf("Opcao invalida!!\nOu digite n para sair");
            }
            setbuf(stdin,NULL);
            printf("\nDeseja continuar? Digite s para sim... ");
            scanf("%c",&continuar);
    }while(continuar == 's');
    deque_liberaFila(f);
    system("PAUSE");
    return 0;
}
