#include<stdlib.h>
#include<stdio.h>

void imprima(int s[], int k){
    int i  = 1;
    for(i = 1; i <= k; i++){
            printf("%d ", s[i]);
    }
    printf("\n");

}

void subseqLex( int n)
{
   int *s, k;
   s = (int*) malloc((n+1)*sizeof(int));
   s[0] = 0;
   k = 0;

   while (1) {
      if (s[k] < n) {
         s[k+1] = s[k] + 1;
         k += 1;
      } else {
         s[k-1] += 1;
         k -= 1;
      }
      if (k == 0) break;
      imprima(s, k);
   }
   free(s);
}


int main(){
    subseqLex(4);
}
