#include <stdio.h>

// Variable definition: 
extern int a, b;
extern int c;
extern float f;

int main(){
     //variable definition
    int a, b;
    int c;
    float f;

    //actual initalization
    a = 10;
    b = 20;
    c = a + b;

    printf("Value of C: %d \n", c);

    f = 70.0/3.0;
    printf("Value of f: %f\n", f)

    return 0;
}