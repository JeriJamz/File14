/*

***********************CAUTION COMPILE AT YO OWN RISK*************************
*/
//This sum else I got out the book. Im doin this to go over my C basics
//But I think its suppsoed to set and enviorment
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <paths.h>

extern char **environ; //Point at this vari

/*Both array are NULL-Terminated*/
//that static makes it Null
static char *spc_restricted_environ[]={//Yea this is an array

    "IFS= \t\n",//this is for unique char in this program
    "PATH=" _PATH_STDPATH,//this set path to standard paths
    0

};

static char *spc_preserve_environ[]={

    "TZ",//this is for time zone
    0

};//these are the two arrays

void spc_sanitize_(int preservec, char **preserveenv){//this is now an obj
//preservec is an int, preserveenv take is a pointer and takes strings
//It might convers prec input into its output
    int i;
    char **new_environ, *ptr, *value, *var;
    size_t arr_size = 1, arr_ptr = 0, len, new_size = 0;//some of these are just vars
       //      now spc_restrict is var also the array is set to i, and i++ means it increaments
    for(i=0; (var = spc_restricted_environ[i]) !=0; i++){

	new_size += strlen(var) + 1//remeber spc_restrict is a string so that means var is a str
	arr_size++

}
//		I do need to clarify with the if state it only kick in when i doesnt equal zero or when the user make an input
    for(i=0; (var = spc_restricted_environ[i]) !=0; i++){//this is the same as the last
//	if it is NOT(a var name Value that has getenv(from var)) cont
	if(!(value = getenv(var))) continue;//cont is like a pass
	new_size += strlen(var) + strlen(var) + 2;//this will include the '=' we gone find out
	arr_size++;

}

    if(preservec && preserveenv){

	for(i=0; i< preservec && (var = preserveenv[i]) !=0; i++){

	    if(!(value = getenv(var))) continue;
	    new_size += strlen(var) + strlen(value) + 2;
	    arr_size++

}

}


new_size += (arr_size * sizeof(char*));new size will now be the size of the array.
if(!(new_environ = (char **)malloc(new_size))) abort();//this is a helluva statement
/*This means if its is NOT(A value named new_environ with a string pointer and its allocated mem and pointer(from new size))
Then abort I think
Dont qoute me*/
new_environ[arr_size - 1] = 0;
ptr = (char *)new_environ + (arr_size * sizeof(char *))//im bit explainin this one.It popped up a coupleof times
for(i=0; (var = spc_restricted_environ[i])!=0 ; i++){

	new_environ[arr_ptr++] = ptr;//this is now stored in ptr
	len = strlen(var);//now var len is being read
	memcpy(ptr, var, len);//this copy the memory of these variables
	ptr += len + 1;

}

for(i=0; (var = spc_preserve_environ[i]) !=0; i+=){

    if(!(value = getenv(var))) continue;
    new_environ[arr_ptr++] = ptr;
    len = strlen(var);
    memcpy(ptr, var, len);
    *(ptr + len + 1) = '='//whateva this ASCII code is
    memcpy(ptr + len + 2, value, strlen(value) + 1)
    ptr += len + strlen(value) + 2;

}

if(preservec && preserveenv){

    for(i=0; i < preservec && (var = preserve[i]) !=0; i++){

	if(!(value = getenv(var))) continue;
	new_environ[arr_ptr++] = ptr;
	len = strlen(var);
	memcpy(ptr + len + 2, value, strlen(value) + 1);
	*(ptr + len + 1) = '=';
	memcpy(ptr + len + 2, value, strlen(value) + 1);
	ptr += len + strlen(value) + 2;

}

}
  environ = new_environ;
}