#pragma once

#include "Vehicle.cpp"

class Car: public Vehicle
{
  private:
    float engineSize;
    int seats;
  
  public:
    Car(float reqEngineSize, 
        int reqSeats, 
        int  reqNumWheels, 
        int reqTopSpeed, 
        float reqPrice)
        :
        Vehicle(reqNumWheels,
                reqTopSpeed,
                reqPrice)
    {
      engineSize = reqEngineSize;
      seats = reqSeats;
    }

    float getEngineSize()
    {
      return engineSize;
    }

    int getSeats()
    {
      return seats;
    }
};