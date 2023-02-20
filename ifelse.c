//an ex. from the documentation
//will get three marks, output an avg, then pass or fail statment
#include <stdio.h>
int main(){

    int mark1, mark2, mark3;
    double avg;
    printf("Enter Three Marks: ");
    scanf("%d %d %d", &mark1, &mark2, &mark3);
    avg = (mark1 + mark2 + mark3) / 3.0;
    printf("\nAverage is %3.2lf\n", avg);
    if (avg>= 50) printf("Pass\n");
        else printf("Fail\n");

}