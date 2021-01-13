#include<stdio.h>
struct vehicle
{
 int price;
 int wheels;
 float engineSize;
};
void swap(struct vehicle * v1, struct vehicle * v2)
{
 struct vehicle v3 = * v1;
 * v1 = * v2;
 * v2 = v3;
}
void bubbleSort(struct vehicle * vs, int size)
{
 int changed = 1;
 while(changed)
 {
 changed = 0;
 for(int i = 0; i < size - 1; i++)
 if(vs[i].price > vs[i+1].price)
 {
 swap(&vs[i],&vs[i+1]);
 changed = 1;
 }
 }
}
int main()
{
 struct vehicle vehicles[5];

 struct vehicle v1 = {1000,2,1.0};
 struct vehicle v2 = {5000,4,1.5};
 struct vehicle v3 = {8000,4,0.8};
 struct vehicle v4 = {2500,6,2.1};
 struct vehicle v5 = {3500,3,3.0};
 vehicles[0] = v1;
 vehicles[1] = v2;
 vehicles[2] = v3;
 vehicles[3] = v4;
 vehicles[4] = v5;
 bubbleSort(vehicles,5);
 for(int i = 0; i < 5; i++)
 printf("vehicle %i has price: %i, wheels: %i and engine:%f\n",i,vehicles[i].price, vehicles[i].wheels,vehicles[i].engineSize);
 return 0;
}