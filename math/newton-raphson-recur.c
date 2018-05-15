#include<stdio.h>
#include<math.h>

// funcao a ser resolvida
float funcao (float x)
{
    float y;
    y = exp(x) + x / 2.0;
    return y;
}

float derivada_funcao(float x) 
{
    float y;
    y = exp(x) + 0.5;
    return y;
}

float NewtonRaphson(float x0, float precisao)
{
    float x1;
    x1 = x0 - (funcao(x0) / derivada_funcao(x0) );
    if(fabs(x0 - x1) > precisao)
        x1 = NewtonRaphson(x1, precisao);
    return x1;
}

int main(int argc, char* argv[]) 
{
    float raiz;
    raiz = NewtonRaphson(-0.85, 0.0001);
    printf("raiz = %g\n", raiz);
    return 0;
}