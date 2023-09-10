#ifndef _POINT_
#def _POINT_
#include <stdio.h>

typedef unsigned char *byte_pointer;//its pointing at this

void show_bytes(byte_pointer start, size_t len){//this creates a obj. Arg BP idk start is and the len of size_t

	int i;
	for(i = 0 ; i < len ; i++)
			printf(" %.2x", start[i]);//start gotta be what starts a function and store it in BP
	printf("\n");

}

void show_int(int x){

    show_bytes((byte_pointer) &x, sizeof(int));

}

void show_pointer(void *x){

	show_bytes((byte_pointer) &x, sizeof(void *));

}

void reverse_array(int a[], int cnt){

    int first, last;
    for(first =0 , last = cnt -1;
        first <= last;
	first++,last--
	inplace_swap(&a[first], &a[last]))

}

#endif