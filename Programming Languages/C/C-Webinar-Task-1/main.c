#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
  int number = 5;
  number = number * 10;
  number = number / 2;
  number = number + 5;
  number = number - 1;
  printf("Number = %i\n", number);

  float numberArray[15] = {0.123,1.543,2.543,3.38,4.786,5.123,6.654,7.8765,8.564,9,10,11,12,13,14.765};
  printf("Last element = %f\n", numberArray[14]);
  
  char string[] = "Hello " "World";
  printf("\"%s\"\n", string);

  return 0;
}