#include <stdio.h>

int main(){

    char name[50];// declare this first
    /*dont need the strcpy*/

    printf("Hi what is your name? ");// wait for input
    gets(name);// stored the variable 
    printf("nice to meet you, %s\n",name);//prints it out, %s is the specifaction

}