#include <stdio.h>
#include <string.h>

int main(){

    char name[50];
    char response[3];
    char name2[50];

    printf("I have no idea what this is gonna be.\n"                                              
    "While were here what is your name?\n");
    gets(name);
    printf("%s, is your name, no?\n",name);
    gets(response);
    if (response == "No"){
        printf("Please enter you name again.\n");
        gets(name2);
        printf("%s, is this correct?", name2);
        gets(response);
    }
    else{
        printf(" %s 0 ", response);}
    printf(" 0 ");
}