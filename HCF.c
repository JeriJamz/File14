//attempt at a problem from the document
#include <stdio.h>

int main(){

    int n,r, m; 

    printf("This is going to find the Highest common factor.\n"
    "Please enter Two Numbers: \n"
    "Press 0 to exit\n ");
    scanf("%d %d", &m, &n);

    while (n != 0){
        r = m%n;
        m = n;
        n = r;
    }
    printf("The highest common factor is %d", m);
}