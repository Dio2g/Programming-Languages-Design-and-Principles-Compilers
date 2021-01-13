#pragma once

#include <iostream>

class Location {
    private:
        double longitude;
        double latitude;
        std::string name;

    public:
        Location(std::string reqName, 
             double reqLongitude, 
             double reqLatitude)
        {
          name = reqName;
          longitude = reqLongitude;
          latitude = reqLatitude;
        }

        std::string getName()
        {
          return name;
        }

        double getLongitude()
        {
          return longitude;
        }

        double getLatitude()
        {
          return latitude;
        }
};
