#include <stdio.h>

int main(void) 
{ 
  for(int i = 1; i <= 101; i++)
  {
   if(i%15==0){
     printf("\nFizzBuzz");
   }else if(i%3==0){
     printf("\nFizz");
   }else if(i%5==0){
     printf("\nBuzz");
   }else{
     printf("\n%i",i);
   }
  }
}