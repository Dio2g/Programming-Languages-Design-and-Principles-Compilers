#pragma once

#include <iostream>
#include "Location.cpp"

class TeachingSpace : public Location {
    private:
        std::string subject;
        int occupancy;
        bool projector;

    public:
        TeachingSpace(std::string reqSubject, 
             int reqOccupancy, 
             bool reqProjector,
             std::string reqName,
             double reqLongitude,
             double reqLatitude)
             :
             Location(reqName,
                      reqLongitude,
                      reqLatitude)
        {
          subject = reqSubject;
          occupancy = reqOccupancy;
          projector = reqProjector;
        }

        std::string getSubject()
        {
          return subject;
        }

        int getOccupancy()
        {
          return occupancy;
        }

        bool hasProjector()
        {
          return projector;
        }
};
