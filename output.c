#include <stdio.h>

int main(){
    char aa[50],a[50];

    FILE * out = fopen("output.txt", "w");//"w"this is for write
    fprintf(out,"%c", aa);

    printf("What would you like to add to the other file\n");
    gets(a);
    

}


