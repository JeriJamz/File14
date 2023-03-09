#include <sys/types.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <pwd.h>//this might not be a thing idk.

int main(int argc, char *argv[]){
    uid_t	uid;
    struct passwd *pwd;


    uid = getuid();
    printf("Users UID is %d.\n ",(int)uid);
    if(!(pwd = getpwuid(uid))){
	printf("Unable to get users password file record\n");
	endpwent();
	return 1;
}
	printf("Users Home Directory is %s. \n", pwd->pwd_dir);
	endpwent();
	return 0;
}

