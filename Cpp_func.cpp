// calculation powers with
// standard function pow()

#include <iostream>		//Decleration of cout
#include <cMath>		//Decleration of pow(), thus: double pow(double,double)

using namespace std;

int main(){

    double x = 2.5, y; //x is init(decleared)
    //By means of a Prototype, the compiler generates, the correct call or an error message
    //Computes x raised to the power 3:
  
   // y = pow("x", 3.0);// error, but x is a string
   // y = pow(x + 3.0); //Error, Jus one argument
    y = pow(x,3.0);//this work
    y = pow(x,3);//this works, just be converted to str


   cout << "2.5 Raised to 3 Yields:		"
	<< y << endl;
//Calaculating with pow() is possible:
   cout << "2 + (5 raised to the power 2.5) yields:  "
	<< 2.0 + pow(5.0,x) << endl;
   return 0;



}



