//outputs 3 random numbers
#include <iostream>  //decleration of cin and cout
#include <cstdlib>   // Prototypes of srand(), rand()


using namespace std;
int main(){

   unsigned int seed;
   int z1, z2, z3;
   
   cout << "	---Randome Numbers ---\n" << endl;
   cout << "To Inititalize the Number Genereator,"
	<< "\nPlease Enter an Interger Value:    ";
   cin  >> seed; //take input

   srand( seed);//this is wat makes it random

   z1 = rand();//calls the random number
   z2 = rand();
   z3 = rand();

   cout << "\nThree Random Number:   "
        << z1 << "  " << z2 << "  " << " "<< z3 << endl;
   return 0;	

}
