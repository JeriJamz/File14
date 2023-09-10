//no way this works I saw it in my book
#include <stdio.h>
#include <setjmp.h>

jmp_buf env;
int main(){

  int r, a = 100;
    printf("call setjmp to save enviorment\n");
    if((r = setjmp(env)) == 0){

	A();
	printf("normal return\n");

    }
    else{

	printf("back to main() via long jump, r = %d a = %d\n", r,a);	

    }

}

i`	nt A(){

    printf("Enter A()\n");
    B();
    printf("Exit A()");

}

int B(){

    printf("Enter B()\n");
    printf("Long Jump? [Y|N]");

    if(getchar() == 'Y'){

	longjmp(env,1234);

    };

    printf("Exit B()\n");

}





