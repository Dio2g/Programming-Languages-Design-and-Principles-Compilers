#include <stdio.h>
#include <string.h>

void swap2(int *num1, int *num2)
  {
    int temp;
    temp = *num1;
    *num1 = *num2;
    *num2 = temp;
  }

int main(void) 
{ 
  int num1 = 69;
  int num2 = 420;
  swap2(&num1, &num2);
  printf("\n%i", num1);
  printf("\n%i", num2);
} 


