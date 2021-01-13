#include <iostream>
#include "Room.cpp"

int main() {
  Room roomStack;
  int x,y;
  std::cin >> x;
  std::cin >> y;

  roomStack.length = x;
  roomStack.breadth = y;

  int area = roomStack.calculateArea();
  std::cout << area << std::endl;

  Room * roomHeap = new Room();
  roomHeap->length = x;
  roomHeap->breadth = y;
  int area2 = roomHeap->calculateArea();
  std::cout << area2 << std::endl;

  delete roomHeap;

  int numRooms;
  std::cout << "enter number of rooms" << std::endl;
  std::cin >> numRooms;

  Room* array;
  array = new Room[numRooms];
  double lengthIn;
  double breadthIn;
  for(int i=0; i<numRooms; i++){
    std::cout << "enter length" << std::endl;
    std::cin >> lengthIn;
    std::cout << "enter breadth" << std::endl;
    std::cin >> breadthIn;
    array[i].breadth = breadthIn;
    array[i].breadth = lengthIn;
  }

  for(int i=0; i<numRooms; i++){
  std::cout << array[i].calculateArea() << std::endl;
  }
}


