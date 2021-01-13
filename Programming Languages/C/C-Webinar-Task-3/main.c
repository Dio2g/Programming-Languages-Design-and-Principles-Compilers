#include <stdio.h>
#include <string.h>

int main(void) {

  char input[] = "";
  int letters = 0;
  int numbers = 0;

  int i;
  for (i = 0; i < strlen(input); i++){
    if (input[i] >= 'a' && input[i] <= 'z') {
      letters++;
    }else if (input[i] >= '0' && input[i] <= '9') {
      numbers++;
    }
  }

  if(letters > numbers){
    printf("letters");
  }else if (numbers > letters){
    printf("numbers");
  }else if (letters == numbers){
    printf("equal");
  }

  return 0;
}
