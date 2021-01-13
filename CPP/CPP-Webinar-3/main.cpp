#include <iostream>

#include "LectureTheatre.cpp"
#include "LabRoom.cpp"

int main() {
  LectureTheatre * lectureTheatre1 
    = new LectureTheatre(
      53.472219, //longitude
      -2.239589, //latitude
      20, //length
      30, //breadth
      "Comp. Sci.", //subject
      66, //occupancy
      true, //projector?
      200, //seats
      true, //lecture capture
      "C0.14" //name
      );

    LabRoom * labRoom1 
    = new LabRoom(
      53.472432, //longitude
      -2.239765, //latitude
      15, //length
      20, //breadth
      "Comp. Sci.", //subject
      66, //occupancy
      true, //projector?
      10, //number of machines
      "Desktop", //machine type
      "C0.14" //name
      );


  std::cout << lectureTheatre1->TeachingSpace::getLongitude() << "\n";

  lectureTheatre1->printInfo();
  labRoom1->printInfo();

}