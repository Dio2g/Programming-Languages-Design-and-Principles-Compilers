#include <stdio.h>

int main(void) 
{
  int x = 5;
  int y = 10;

  if(x > y)
     printf("x is greater\n");
  else
    printf("y is greater\n");

  for(int i = 5; i >= 1; i--)
  {
    int j = 1;
    while(j <= i)
    {
      j++;
      printf("X ");
    }
    printf("\n");
  }

  return 0;
}