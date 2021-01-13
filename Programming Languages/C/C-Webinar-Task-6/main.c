#include <stdio.h>
#include <string.h>

struct Person {
  char name[20];
  float height;
  int age;
};

void printPerson(struct Person * person)
{
  printf("name = %s\n"  ,person->name);
  printf("height = %f\n",person->height);
  printf("age = %i\n"     ,person->age);
}

void birthday(struct Person * person){
  person->age = person->age + 1;
}

int main(void) {

  struct Person p1 = {.name   = "Matt", 
                      .height = 1.75,
                      .age    = 31};

  struct Person p2 = {.name   = "Aubrey Monk", 
                      .height = 1.75,
                      .age    = 20};                    

  printPerson(&p1);

  //birthday(&p2);

  strcpy(p1.name,"Matthew Shardlow");
  p1.height = 1.8;
  p1.age = 32;

  printPerson(&p1);

  struct Person people[3];

  strcpy(people[0].name,"Joe Bloggs");
  people[0].height = 1.9;
  people[0].age = 25;

  //...

  struct Person pArray[] = {p1, p2};
  for(int i = 0; i < (sizeof(pArray)/sizeof(pArray[0])); i++)
  {
    printPerson(&pArray[i]);
  }
}