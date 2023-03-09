#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main(){
  string label;
  string price;

   cout << "\nEnter something(15 Char Max): ";

   cin.width(16);
   cin >> label;

   cin.sync();//clears and resets buffers
   cin.clear();//resets error flags

   cout <<"\nEnter the price of the input: ";
   cin >> price;

	//controll output
    cout << fixed << setprecision(2)
	 << "\nInput: "
	 << "\n  Label:  "<< label
	 << "\n  Price:  "<< price << endl;
//this bs again
return 0;
}q




