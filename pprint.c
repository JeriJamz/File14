#include <stdio.h>

int main(){

   int i = 1;

    printf("Type some data and then press Enter: ");
    while( i != 0){
	char ch = getchar();


	printf("Press 0: to quit");
	printf("Chars is %c\n%d" ,ch,i);
    }

}



