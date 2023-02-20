#include <stdio.h>
#include <string.h>

int main(){


    char x[10];
    char part[20] = "Who"; //this only calls strcat bc it already got its value
    char one[15] = "Wit";
    char roll[50];
    char name[50];

    strcpy(roll, "WOOOOOOO PIIIIGGGG SOOOOOOOIIIIEEEEEE");

    strcat(part, " ya ");
    strcat(part, one);//this perm adds part and one together still working on a way to seperate it

    strcpy(x , "Jeri James");//strcpy when the value aint been set yet

    printf("Hello %s\n", x);
    printf("%s\n", part);
    printf("%s\n", one);
    printf("What is yo name? \n");
    gets(name);
    printf("%s, it is nice to meet you\n", name);
    /*gets(roll); this is not how gets work...
    printf("%s\n",roll);*/


}
