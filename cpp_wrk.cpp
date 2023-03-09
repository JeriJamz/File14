//these gone be some examples out the book
#include <iostream>	//Obligatory, regular shit
#include <iomanip>	//declarations, this is for feild width
#include <string>	//Manip strings

using namespace std;

int main(){
  cout<<endl<<"This is the first example in the book. Its over notation. \n";
    double x = 12.0;
    cout.precision(2);//Precision 2#two decimal points
    cout << "By default:	"<<x << endl;
    cout << "showpoint:  "<< showpoint << x << endl;
    cout << "fixed:	"<< fixed << x << endl;
    cout << "scientific: "<< scientific << x << endl;
    cout << endl<< "\n\n\n"
	 <<"This is going over field width";
    cout << "|" << setw(6) << "X" << "|";//this should set rgt 6 places(I cant spell that J word1)
    cout << fixed << setprecision(6)//I
         << setw(6) << 123.4 << endl//Love
         << "0123456789" << endl; // It
   cout.width(6);
   cout.fill('0');
   cout << internal << -123;

   cout << endl << "\n\n\n"
	<<endl << "This is over some string Manip."; 

   int number = ' ';//this is fun, ok I read the notes this makes hella sense. Its converts to ASCII
   
   cout << "The White space code is "
	<< number << endl;

   char ch;
   string lol = //I like this string prompt thing
	"\nPlease enter a character followed by"
				    "<return>: ";

   cout << lol; //I think thats console. But this prints the prompt

   cin >> ch;//stores the input
   number = ch;//why the int!!! is it bc its all 1 and 0s or bc int and strings are oddly classed together

   cout << "The character " << ch
	<< " has code " << number << endl;

   cout << uppercase //this is for the hex-dex stuff
	<< "	octal		 decimal	 hexadecimal\n "
	<< oct << setw(8) <<number << "\n"
	<< dec << setw(8) << number << "\n"
	<< hex << setw(8) << number << endl;

  char y = '0';
    cout << y << ' ' << 'A';//this should output 0 A three times
  int code = '0';
    cout << code; //should output 48, I think thats the ASCII code for it

    cout << endl << "This is over some string Manip";

/*  string label;
  string price;

    cout << "\nPlease enter an article label(lol just enter something) \n";
    cout << endl << "15 Char max";

    cin.width(16);
    cin >> label;

    cin.sync();//clears the buffer and resets
    cin.clear();//resets error flags

    cout << "\nEnter the price of input: ";
    cin >> price; //input

    //controlling output
    cout << fixed << setprecision(2)
	 << "\nInput: "
	 << "\n  Label:  " << label
	 << "\n  Price:  " << price << endl;
	//this book is gonna come back to this 
This code breaks my compiler. Ima jus chalk it up to I got the wrong header file. It wont flip the damn pointer on line 73 */

return 0;
}



