#include <stdio.h>

int main(){

    int n;

    printf("How many number would you like to enter\n");
    scanf("%d", &n);
    for (int h = 1; h <= n; h++)
        printf("%d. I must not sleep in class\n", h);

}