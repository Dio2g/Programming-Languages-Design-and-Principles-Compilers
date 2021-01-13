#pragma once
#include <string>
#include "Room.cpp"
#include "TeachingSpace.cpp"

class LabRoom : public Room, public TeachingSpace
{
  private:
    int numMachines;
    std::string machineType;
  
  public:
    LabRoom(double reqLongitude, 
            double reqLatitude, 
            double reqLength, 
            double reqBreadth, 
            std::string reqSubject, 
            int reqOccupancy, 
            bool reqProjector, 
            int reqNumMachines, 
            std::string reqMachineType,
            std::string reqName)
            :
            Room(reqName,
                 reqLength,
                 reqBreadth,
                 reqLongitude,
                 reqLatitude)
            ,
            TeachingSpace(reqSubject,
                          reqOccupancy,
                          reqProjector, 
                          reqName, 
                          reqLongitude, 
                          reqLatitude)
    {
      numMachines = reqNumMachines;
      machineType = reqMachineType;
    }

    int getNumMachines()
    {
      return numMachines;
    }

    std::string getMachineType()
    {
      return machineType;
    }

    void printInfo()
    {
      printf("Lab Room %s has a maximum capacity of %i people and %i machines. It is %f metres wide and %f metres long.\n",Room::getName().c_str(),getOccupancy(),numMachines,getBreadth(),getLength());
    }


};