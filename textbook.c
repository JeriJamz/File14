//trynna find the negative buffer limit so watch for updates
#include <stdio.h>

int main(){

  int x = -16546464664;
  int y = -41464456;
  int z = x + y;

  int mod = z/2^64;

    printf("This is z %d", mod);


}

