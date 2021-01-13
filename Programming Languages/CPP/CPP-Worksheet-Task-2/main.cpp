#include <iostream>
using namespace std;
class Factorial
{
 private:
 int num;
 int factorial;
 public:
 Factorial(int reqNum)
 {
 num = reqNum;
 factorial = 1;
 for(int i = 2; i <= num; i++)
 factorial *= i;
 }
 
 int getFactorial()
 {
 return factorial;
 }
};
int main()
{
 //stack version
 Factorial myFactorial = Factorial(10);
 cout << myFactorial.getFactorial() << endl;
 //heap version
 Factorial * myFactorial2 = new Factorial(10);
 cout << myFactorial2->getFactorial() << endl;
 delete myFactorial2;
}