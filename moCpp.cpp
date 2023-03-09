/*
PROGRAM with Obj 
 
 */
#include <iostream>
using namespace std;

void line(), message(); //objs?, this is cool, Void makes objs and functions, not varis
//cout = Commnad Output?
int main(){//this is the program, its just not defined yet.
   cout << "Hello, The program starts in main()"//you can break up the string txt
	<< endl;//this is how to end a line and a semicolon ;
   line();//line function
   message();//message function
   line();
   cout << "The End 0"<< endl;//this would be the final line printed
   return 0;//make sure the program works
}

void line()//this the line function
{
	cout <<"------------------------------"<<endl;
}

void message(){//this is the message function
    cout<<"This is the message function"<<endl; 
}

