#include <iostream>

class Room {
    public:
        double length;
        double breadth;

        int calculateOccupancy(float rate)
        {   
            return (calculateArea()/6)*rate;
        }

        double calculateArea()
        {   
            return length * breadth;
        }
};

int main() {

  Room room;

  room.length = 10;
  room.breadth = 10;

  std::cout << room.calculateArea() << std::endl;
  std::cout << room.calculateOccupancy(1) << std::endl;
  std::cout << room.calculateOccupancy(0.5) << std::endl;
  std::cout << room.calculateOccupancy(0.33) << std::endl;
}

