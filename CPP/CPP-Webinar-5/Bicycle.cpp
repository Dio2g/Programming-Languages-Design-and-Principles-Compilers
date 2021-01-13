#pragma once

#include "Vehicle.cpp"

class Bicycle: public Vehicle
{
  private:
    int numGears;

  public:
    Bicycle(float reqNumGears, 
            int   reqNumWheels, 
            int   reqTopSpeed, 
            float reqPrice)
            :
            Vehicle(reqNumWheels,
                    reqTopSpeed,
                    reqPrice)
    {
      numGears = reqNumGears;
    }

  int getNumGears()
  {
    return numGears;
  }
};