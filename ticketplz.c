#include <stdio.h>
//ticket please
/*Remember to add total sales to the programs y bc u r a weetard*/
int main(){

    int gt,rt,st;
    double gtp,rtp,stp,gs,rs,ss;

    printf("please enter Ground ticket prices/ sales:");
    scanf("%0.2lf", &gtp);
    printf("\nPlease enter Total Ground tickets sold : \n");
    scanf("%d",&gt);
    printf("\nPlease enter Reserved ticket prices : ");
    scanf("%0.2lf", &rtp);
    printf("\nPlease enter Total Reseved Tickets sold : ");
    scanf("%d",&rt);
    printf("\nPlease enter Stand ticket prices: ");
    scanf("%0.2lf", &stp);
    printf("\nPlease enter stand tickets sold : ");
    scanf("%d",&st);
    gs = gtp * gt;
    rs = rtp * rt;
    ss = stp * st;
    printf("\nThe total are:"
    "\nGround ticket sales/total: %d/%0.2lf"
    "\nStand Ticket sales/total: %d/%0.2lf"
    "\nReserved Tickets sales/total: %d/%0.2lf", gt,gs,st,ss,rt,rs);


}
