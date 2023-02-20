//this is an example from the Document
#include <stdio.h>

int main(){
    double hrs, parts,JbChar;
    printf("Hours worked? ");
    scanf("%lf", &hrs);
    printf("Cost of the parts? ");
    scanf("%lf", parts);
    JbChar = hrs * 100 + parts;
    if (JbChar < 150) JbChar = 150; // reads(if jobchare is less than 150, the Job charge = 150 )
    printf("The Job charge is, %3.2f", JbChar);
}