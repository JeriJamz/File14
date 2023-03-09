#include <iostream>
using namespace std;

void pause();

int main(){

    cout << endl << "Testing"//this is how to break the str lines up so you 
         << endl << "Testing";// aint gott use hella ;
         pause();
    cout << "!" << endl;
    cout << "Does this work"; //you dont really need endl; jus the semi-colon

    return 0 ;

}

void pause(){

    cout<< "BREAK";//this works
}

