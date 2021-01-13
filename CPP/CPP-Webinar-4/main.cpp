#include <iostream>

class Bicycle
{
  private:
    int wheels;
    int gears;
    float price;
  public :
    Bicycle(int wheels, int gears, float price)
    {
      this->wheels = wheels;
      this->gears = gears;
      this->price = price;
    }  

    int getWheels(){
      return wheels;
    }

    int getGears(){
      return gears;
    }

    float getPrice(){
      return price;
    }

    void setWheels(int wheels){
      this->wheels = wheels;
    }

    void setGears(int gears){
      this->gears = gears;
    }

    void setPrice(float price){
      this->price = price;
    }

    void printBikeInfo()
    {
      printf(("Bicycle with %i wheels and %i gears costs %f\n"), wheels, gears, price);
    }
};


int main() {
  Bicycle bicycle(2,5,300);
  bicycle.printBikeInfo();
}

