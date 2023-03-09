//define and use vars
#include <iostream>
using namespace std;

int gVar1;		//global Var, and it has not real value, you can declare it later
int gVar2 = 2;		//explicit initalizaition its has a value

int main(){
   char ch('A');		//This is a local Vari being init, this is how to make string var
    			//char ch = 'A'; is also valid
   cout<<"Value of gVar1:      "<<gVar1 <<endl;
   cout<<"Value of gVar2:      "<<gVar2 <<endl;
   cout<<"Character in Ch:     "<<ch    <<endl;

   int sum, number = 3;//Local Vari w/ and w/o init

   sum = number + 5;
   cout << "Value of sum:      "<< sum << endl;

   return 0; 
  
}


