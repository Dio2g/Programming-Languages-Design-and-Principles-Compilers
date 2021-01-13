#include <iostream>
using namespace std;
class Consumable
{
 private:
 string name;
 int price;
 public:
 Consumable(string reqName, int reqPrice)
 {
 name = reqName;
 price = reqPrice;
 }
 string getName()
 {
 return name;
 }
};
class Food : public Consumable
{
 private:
 int calories;
 public:
 Food(string reqName, int reqPrice, int reqCalories)
 : Consumable(reqName, reqPrice)
 {
 calories = reqCalories;
 }
};
class Drink : public Consumable
{
 private:
 int volume;

 public:
 Drink(string reqName, int reqPrice, int reqVolume)
 : Consumable(reqName, reqPrice)
 {
 volume = reqVolume;
 }
};
class Pizza : public Food
{
 private:
 string topping;
 public:
 Pizza(string reqName, int reqPrice, int reqCalories, string
reqTopping)
 : Food(reqName, reqPrice, reqCalories)
 {
 topping = reqTopping;
 }
};
class Burger : public Food
{
 private:
 string filling;
 public:
 Burger(string reqName, int reqPrice, int reqCalories, string
reqFilling)
 : Food(reqName, reqPrice, reqCalories)
 {
 filling = reqFilling;
 }
};
class AlcoholicDrink : public Drink
{
 private:
 float abv;
 public:
 AlcoholicDrink(string reqName, int reqPrice, int reqVolume, float
reqABV)
 : Drink(reqName, reqPrice, reqVolume)
 {
 abv = reqABV;
 }
};
class SoftDrink : public Drink
{
 private:
 bool fizzy;
 public:
 SoftDrink(string reqName, int reqPrice, int reqVolume, bool
reqFizzy)
 : Drink(reqName, reqPrice, reqVolume)
 {
 fizzy = reqFizzy;
 }
};
class Soup : public Food, public Drink
{
 private:
 string flavour;
 public:
 Soup(string reqName, int reqPrice, int reqCalories, int reqVolume,
string reqFlavour)
 : Food(reqName, reqPrice, reqCalories),
 Drink(reqName, reqPrice, reqVolume)
 {
 flavour = reqFlavour;
 }
};
int main()
{
 Consumable * c = new Consumable("Yeast",1);
 Food * f = new Food("Cake", 5, 1000);
 Drink * d = new Drink("Water", 2, 500);
 Pizza * p = new Pizza("Margherita", 10, 700, "Cheese and Tomato");
 Burger * b = new Burger("Cheese Burger", 5, 800, "Cheese");
 AlcoholicDrink * a = new AlcoholicDrink("Wine",20,700,14.5);
 SoftDrink * sd = new SoftDrink("Lemonade", 2, 1000, true);
 Soup * s = new Soup("Gazpacho", 6, 300, 500, "Tomato");
 cout << c->getName() << endl;
 cout << f->getName() << endl;
 cout << d->getName() << endl;
 cout << p->getName() << endl;
 cout << b->getName() << endl;
 cout << a->getName() << endl;
 cout << sd->getName() << endl;
 cout << s->Food::getName() << endl;
}