//lookinf diffrent methods to put in os, I need a file manager.

#include <stdio.h>
#include <string.h>

struct Books{//this is the main var name. Can I automate it where it add both names?

  char title[50];
  char author[50];
  char subject[100];
  int book_id;

};//this is also another var name

void printBook(struct Books book);//call this before you make the var for it

int main(){

     struct Books Book1;
     struct Books Book2;//these are dec of book types

//this is for book one
     strcpy(Book1.title,"Book1 Title\n");
     strcpy(Book1.author,"Book1 Author\n");
     strcpy(Book1.subject,"Book1 Subject\n");
     Book1.book_id = 1234;

//this is for book2
     strcpy(Book2.title,"Book2 Title\n");
     strcpy(Book2.author,"Book2 Author\n");
     strcpy(Book2.subject,"Book2 Subject\n");
     Book2.book_id = 1564856;

     printBook(Book1);
     printBook(Book2);

  return 0;
}

void printBook(struct Books book){
  
     printf("This the print book function");
     printf("Book title: %s\n", book.title);
     printf("Book subject is %s\n", book.subject);

}


