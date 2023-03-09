#include <stdio.h>
#include <string.h>

int main(){

  char ch;  
  char name[50];
    //this put the file pointer and the in function.
    FILE*in = fopen("input.txt", "r");//i think this will create and read for a file
    while((ch = getc(in)) != '\n')
	putchar(ch);
    putchar('\n');
    fclose(in);

/*    printf("Hello my name is FreeBird.\n"
	    "What is your name?");
*/
}


