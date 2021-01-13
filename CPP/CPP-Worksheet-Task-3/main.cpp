#include <iostream>
using namespace std;
class TextAnalyser
{
 private:
 string text;
 string characters = "abcdefghijklmnopqrstuvwxyz!?*&";
 int frequencies[30];
 public:
 TextAnalyser(string reqText)
 {
 text = reqText;
 }
 void analyse()
 {
 for(int i = 0; i < text.length(); i++)
 {
 char ch = text[i];
 int index = characters.find_first_of(ch);
 frequencies[index]++;
 }
 }
 void printFrequencies()
 {
 for(int i = 0; i < characters.length(); i++)
 {
 if(frequencies[i] != 0)
 cout << characters[i] << ": " << frequencies[i] << endl;
 }
 }
};
int main()
{
 TextAnalyser * textAnalyser = new TextAnalyser("hello world!");
 textAnalyser->analyse();
 textAnalyser->printFrequencies();
}