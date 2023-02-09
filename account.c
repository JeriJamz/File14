#include <stdio.h>

//let me see if i can make sum like a memory bank 

int main(){

    char name[100], acctnum[17];//use the gets method for these
    double bal, intrest, service;// scanf here
    int trans;

    printf("What is the name of the account holder?: ");
    gets(name);
    printf("What is the account number?");
    gets(acctnum);
    printf("What is the balance?");
    scanf("%lf",&bal);
    intrest = bal * .06;
    printf("The intrest on your account is %0.2lf\n", intrest);
    printf("Please enter the number of transactions: ");
    scanf("%d",&trans);
    service = trans * .5;
    printf("Your number of service fee is: %0.2lf", service);

}