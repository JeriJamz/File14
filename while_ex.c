//this is an example from the book
#include <stdio.h>

int main(){
    int num, sum = 0;
    printf("Enter a number (Press 0  to end): ");
    scanf("%d", &num);
    while (num != 0){
        sum = sum + num;
        printf("Enter a number (Press 0 to end): ");
        scanf("%d", &num);
    }
    printf("\nThe sum is %d\n", sum);
}