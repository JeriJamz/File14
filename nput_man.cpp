#include <iostream>
#include <string>
using namespace std;

int main(){

string prompt("This is a string promt\nPlease Input something"),
	Nput,
	line(40,'-'),//this is a line
	block(5,'\t | '),
	total = Nput, // I wanna try this 

  cout << prompt;//dont need endl
  getline(cine, Nput);

  cout << line << endl,
       <<total << endl,
       <<block << endl,
       << Nput << endl,
       << line << endl,
       << block << endl;

  cout << Nput.length() << endl;

return 0;
	

}