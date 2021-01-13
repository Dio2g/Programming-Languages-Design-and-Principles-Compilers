#include <stdio.h>

void increment(int *num)
{
  *num = *num + 1;
  printf("%i\n", *num);
  
  return;
}

int main(void) {
  int myNum = 5;
  increment(&myNum);

  printf("%i\n",myNum);

  return 0;
}


