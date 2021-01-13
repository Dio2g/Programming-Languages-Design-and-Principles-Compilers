#include <stdio.h>
#include <stdlib.h>

int main(void) {

  int num;
  printf("Enter size of array\n");
  scanf("%i",&num);

  //int num = 3;
  printf("Enter %i numbers\n", num);

  int *myArray = malloc(num * sizeof *myArray);

  for(int i = 0; i < num; i++)
  {
    scanf("%i",&myArray[i]);
  }

  for(int i = 0; i < num; i++)
  {
    printf("element %i = %i\n", i, myArray[i]);
  }

  return 0;
}