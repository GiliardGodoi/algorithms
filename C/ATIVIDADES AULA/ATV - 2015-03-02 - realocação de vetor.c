#include<stdio.h>
#include<stdlib.h>

int main(){
    int *vetor;
    int i, m = 5;

    vetor = (int *) malloc(m*sizeof(int));
    if(vetor == NULL){
        exit(0);
    }
    for(i = 0; i < m; i++){
        vetor[i] = rand()%10;
    }
    for(i = 0; i < m; i++){
        printf("%d\t", vetor[i]);
    }
    m++;
    vetor = (int *) realloc(vetor, m*sizeof(int));
    vetor[m-1] = 0;
    for(i = 0; i < 5 ; i++){
        vetor[m-1] += vetor[i];
    }
    printf("\n\nTOTAL = %d",vetor[m-1]);

    free(vetor);
    return 0;

}
