#pragma once

#include <iostream>
#include "Location.cpp"

class Room : public Location{
    private:
        double length;
        double breadth;

    public:
        Room(std::string reqName, 
             double reqLength, 
             double reqBreadth,
             double reqLongitude,
             double reqLatitude)
             : 
             Location(reqName,
                      reqLongitude,
                      reqLatitude)
        {
          length = reqLength;
          breadth = reqBreadth;
        }

        double calculateArea()
        {   
            return length * breadth;
        }

        double getLength()
        {
          return length;
        }

        double getBreadth()
        {
          return breadth;
        }
};
