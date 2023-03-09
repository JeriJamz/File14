#include <iostream>
using namespace std;

int main(){

   cout << endl<< "/nSize of Fundemental Types\n"
	<< endl<< "Type			Number of Bytes\n"
	<< endl<< "Char:		"<<sizeof(char)
	<< endl<< "\nshort:		"<<sizeof(short)
	<< endl<< "\nint:		"<<sizeof(int)
	<< endl<< "\nlong:		"<<sizeof(long)
	<< endl<< "\nfloat:		"<<sizeof(float)
	<< endl<< "\ndouble:		"<<sizeof(double)
	<< endl<< "\nlong double:	"<<sizeof(long double);//yea its typed like that
   cout << "\nThis is the bit size of the data types, yay asm." << endl;  
  return 0;
}


