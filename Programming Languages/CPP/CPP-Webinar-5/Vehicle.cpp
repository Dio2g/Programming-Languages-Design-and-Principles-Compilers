#pragma once

class Vehicle
{
  private:
    int numWheels;
    float price;
    int topSpeed;

  public:
    Vehicle(int   reqNumWheels, 
            float reqPrice, 
            int   reqTopSpeed)
    {
      numWheels = reqNumWheels;
      price = reqPrice;
      topSpeed = reqTopSpeed;
    }

    int getNumWheels()
    {
      return numWheels;
    }

    float getPrice()
    {
      return price;
    }

    int getTopSpeed()
    {
      return topSpeed;
    }

    double pricePerWheel(){
      return getPrice()/getNumWheels();
    }
};