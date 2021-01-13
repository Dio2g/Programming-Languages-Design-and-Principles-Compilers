#include<stdio.h>
#include<stdlib.h>
#include <string.h>
struct frequencyData
{
 char ch;
 int frequency;
};
int main()
{
 char * str = "hello world";
 struct frequencyData * frequencies
 = malloc(sizeof(struct frequencyData) * 26);
 int i = 0;
 //populate frequencies structs for a to z
 // chars are essentially ints in c so we can add one to get the next char
 
 for(char c = 'a'; c <= 'z'; c++)
 {
 frequencies[i].ch = c;
 frequencies[i].frequency = 0;
 i++;
 }
 //check each char in string and increment frequency
 // n.b. a = 97 in ascii, so 'a'-97 = 0.
 for(i = 0; i < strlen(str); i++)
 {
 char c = str[i];
 if(c >= 'a' && c <= 'z')
 frequencies[c - 97].frequency++;
 }
 for(i = 0; i < 26; i++)
 printf("%c = %i\n",frequencies[i].ch,frequencies[i].frequency);
}