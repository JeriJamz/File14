//this is where the unser input and the program output
#include <stdio.h>

int main(){

    char name[50];
    char k[3];

    printf("Entrt a name\n");
    gets(name);
    printf("%s ,are you a returning user\n", name);
    gets(k);
    if (k = "Yes"){
        printf("0");
    }
    else{
        printf("1");
    }
}