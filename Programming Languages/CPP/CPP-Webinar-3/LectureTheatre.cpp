#pragma once

#include "Room.cpp"
#include "TeachingSpace.cpp"


class LectureTheatre : public Room, public TeachingSpace
{
  private:
    int numSeats;
    bool lectureCapture;
  
  public:
    LectureTheatre( double reqLongitude, 
                    double reqLatitude, 
                    double reqLength, 
                    double reqBreadth, 
                    std::string reqSubject, 
                    int reqOccupancy, 
                    bool reqProjector, 
                    int reqNumSeats, 
                    bool reqLectureCapture,
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
      numSeats = reqNumSeats;
      lectureCapture = reqLectureCapture;
    }

    int getNumSeats()
    {
      return numSeats;
    }

    bool getLectureCapture()
    {
      return lectureCapture;
    }

    void printInfo()
    {
      printf("Lecture Theatre %s has a maximum capacity of %i people and %i seats. It is %f metres wide and %f metres long.\n",Room::getName().c_str(),getOccupancy(),numSeats,getBreadth(),getLength());
    }
};