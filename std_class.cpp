//Using Strs
#include<iostream>  // Dec of cin,cout
#include<string>  //Dec of class string
using namespace std;

int main(){

    // defines four strings:
    string prompt("What is your name:  "),//if use string promt you use the comma
	name,		//(MT var)this is the user input(in string)
	line(40,'-'),	//Data Viz, line#the var name line(40#number of repeats), line(40,'-'#the Char that gonna repeat)
	total = "Hello "; //you can also do this

  cout << prompt; //this starts this program
  getline(cin,name); //this gotta get the name from the user

  total = total + name;// "Hello {name}"
  
  cout << line << endl //outputs line and name(at 40?)
       << total << endl;
  cout << "Your name is " //outputs this
       << name.length() << "Str long"<< endl;//this this how to call .length()
  cout<< line << endl;
return 0;

return 0;
  

}


