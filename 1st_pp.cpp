#include <iostream>
using namespace std;

void line(), message();

int main(){

    cout<< "Hello, This is the start of program"
    <<endl;
    line();
    message();
    line();
    cout<<"This is the output message"<<endl;

    return 0;

}

void line(){
    cout<<"------------------------"<<endl;
}

void message(){

    cout<<"This is the message function"<<endl;

}

