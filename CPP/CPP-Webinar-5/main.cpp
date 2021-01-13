#pragma once

#include <iostream>

#include "Vehicle.cpp"
#include "Bicycle.cpp"
#include "Car.cpp"

double pricePerWheel(Vehicle v1){
  return v1.getPrice()/v1.getNumWheels();
}

int main() {              //          whls price  speed   
  Vehicle * v1 = new Vehicle(         3,   1000,  40);
                          //      grs whls price  speed 
  Bicycle * b1 = new Bicycle(     7,  2,   500,   30);
                          // eng  sts whls price  speed 
  Car     * c1 = new Car(    2.0, 4,  4,   20000, 100);

  Vehicle * vehicleArray[3];

  vehicleArray[0] = v1;
  vehicleArray[1] = b1;
  vehicleArray[2] = c1;

  for(Vehicle * v : vehicleArray)
    std::cout << v->getPrice() << std::endl;

  std::cout << b1->pricePerWheel() << std::endl;
}



