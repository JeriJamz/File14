//defining and init variables
#include <iostream>
using namespace std;

int main(){

  int  x = 123.456F,//x,y is init
       y = 76.543F,//assign multi numbers
       sum;//not init
  sum = x + y;//init

  cout << "Total:		"
       << x << " + " << y << " = "<< sum << endl;
  cout << "Diffrence:		"
       << x << " - "<< y << " = "<< (x-y)<<endl; //x-y is called last second
  return 0;

}