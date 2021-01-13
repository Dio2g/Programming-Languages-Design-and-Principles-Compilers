#include <stdio.h>

int main(void) 
{ 
  int x = 5;
  int f = 1;
  for(int i = 1; i < x+1; i++)
  {
   f = f*i;
   printf("\n%i", f);
  }
}