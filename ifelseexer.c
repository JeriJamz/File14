#include <stdio.h>

int main(){

    char s[50];

    printf("This is a test run Just to test "//Not to far
    "Input Validation\n");
    printf("Enter Yes or No \n"
    "This is case sensitive\n");
    gets(s);
    if (s == "Yes") printf("Yes");
        else printf("No");

}