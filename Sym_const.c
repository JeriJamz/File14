#include <stdio.h>
#define z 100
#define x 25

int main(){

    int a,b,c, sum, mn;
    
    printf("Enter Three marks\n");
    scanf("%d %d %d", &a,&b,&c);
    sum = a + b + c;
    if (sum < 100) {
        mn = x + sum;
        printf("your magic number is: %d", mn);
    } 
        else{
            mn = z * sum;
            printf("your magic number is: %d",mn);
        }
}