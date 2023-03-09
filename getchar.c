//C stuff here we go
#include <stdio.h>

int main(){

    printf("Type some data and press Enter: \n");
    char ch = getchar();
    printf("\nThe first Char is  %c \n", ch); //%c field spec for getchar()
    printf("Its code is %d \n,", ch);//this will print the ASCII of the strings
    printf("Value of the EOF is %d \n",EOF);//ima assume this how to call the EOF

}




