#include <stdio.h>
#include <math.h>

float funcao (float x)
{
  float y;
  y = exp(x) + (x/2.0);
  return y;
}

float dicotomia(float xa, float xb, float precisao)
{
  float xc, anterior;
  anterior = xb;
  xc = xa;
  while ( fabs(xc - anterior) > precisao) {
    anterior = xc;
    xc = (xa + xb) / 2.0;
    if(funcao(xa) * funcao(xc) < 0.0) xb = xc;
    else
    if(funcao(xb) * funcao(xc) < 0.0) xa = xc;
  }

  return xc;
}

int main(int argc, char* argv[])
{
  float raiz;
  raiz = dicotomia(-0.9,-0.8, 0.0001);
  printf("raiz = %g\n", raiz);
  
  return 0;
}
