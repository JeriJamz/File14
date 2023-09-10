#include<stdio.h>
#include<string.h>

int main(){

  char first[50];
  char last[50];
  char name[100];


    printf("We gone take down a name\n"
	   "What is your first name\n");
    gets(first);
    strcat(name,first);
    strcat(name," ");
    printf("whats your last name\n");
    gets(last);
    strcat(name,last);

    printf("Your name is %s", name);

}


