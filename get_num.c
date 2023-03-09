//this is an example from the book
//it could be hella useful
#include <stdio.h>

int main(){

    printf("Input data Plus a number\n"
	    "Then Press <Enter>: \n");
  char ch = getchar();
//its only looking for numbers
    while(ch<'0' || ch>'9') ch = getchar();
  int num = 0;
    while(ch >= '0'&& ch<='9') {//this would be good for hidin info in plain sight
	//this happens when we got a number
	num = num * 10 + ch - '0';//this how to make a string a number. I think
	ch = getchar();//note it only picks up the first num so updates coming
}
     printf("Number is %d\n", num);
}

