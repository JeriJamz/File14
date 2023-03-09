#include <stdio.h>

int main(){

  char* ch;

   printf("Type data (really looking for yes)\n"
	  "Then press <Enter>\n");
     gets(ch);//so this doesnt work
    if(ch != "Yes"){
	printf("try again");
	gets(ch);
}

}


