#include <stdio.h>

int main(){

    double d = 2.321;
    int a,b,c;
    float x = d;

    a = 50;
    b = 20;
    c = 51;

    printf("%d + %d = %d\n", a,b,a + b);
    printf("%d/%d = %d\n", a,b,a/b);
    printf("print\n");

    printf("%f\n", x);// make sure to use f instead of d bc that for strings
    printf("This should print an indent")
    printf("%6.2f\n", d);
    printf("Tru\n");

}