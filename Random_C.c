#include <stdio.h>
#include <string.h>

int main(){
	char name[50];
	char response[3]
	printf("I have no Idea what this is gonna be.\n"
			"But I am working on data validation\n"
			"So yea\n");
	printf("What is your name?\n"
			"My Bad where is my manners.\n"
			"My name is Los\n");
	gets(name);
	printf("Your name is %d, innit?", name);
	gets(response);
	
	while response !="Yes"{
		printf("I am sorry about the incovience.\n"
				"Here lets us see if we can fix that\n"
				"Please enter your name one more time?");
		gets(name);
		printf("I hope it is right this time."
				"%d, innit?", name);
		gets(response);
	}
			
}


