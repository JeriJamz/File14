#include <iostream>
using namespace std;


int main(){

    cout << "Range of types int and unsigned int"
         << endl << endl;
    cout << "Type           Mini                Max"
         <<endl
         <<"-------------------------------------------"
         <<endl;

    cout <<"int             "<< INT_MIN<< "             "
                             << INT_MAX<<endl;//this is way less static than c
    cout <<"Unsigned int    "<< "           0            "
                             << UINT_MAX <<endl;//i think this is unsigned int
    return 0;

}