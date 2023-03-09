//trying yo make this the page that holds all the file name
//ima try and make a list. See how this goes
//ima gonna learn this and implement it. If its a list
#include <stdio.h>//std i/o
#include <string.h>//Manip String
#include <stdlib.h>//std Libaray#malloc
#include <stdbool.h>//std bool stuff

struct node{
  int data;
  int key;
  struct node *next;//this puts a pointer to the next var
};

struct node *head = NULL;//puts a header at head in the node
struct node *current = NULL;//same as the last

//display the list
void printList(){
  struct node *ptr = head;
  printf("\n[ ");

  while(ptr != NULL){
    printf("(%d,%d)", ptr->key,ptr->data);
    ptr = ptr->next;
}
  printf(" ]");
}

//insert link at first location
void insertFirst(int key, int data){

//this create the link
  struct node *link = (struct node*) malloc(sizeof(struct node));

  link->key = key;
  link->data = data;

//this points it to the old node
  link->next = head;

//point first to new "first" node
  head = link;
}

//delete first item
struct node* deleteFirst(){

// save refer to first link
  struct node *tempLink = head;

//mark next to first link as first
  head = head->next;

//returns the deleted link
}
bool isEmpty(){
  return head == NULL;
}

int length(){
  int length = 0;
  struct node *current;

  for(current = head; current != NULL; current = current->next){
    length++;
}
  return length;
}

//find a link with given key
struct node* find(int key){

//start from the first link
  struct node* current = head;

//if the list is empty
  if(head == NULL){
     return NULL;
}
//nav through list
  while(current->key != key){

//if its the last node
    if(current->next == NULL){
      return NULL;
}
    else{//goes to the link
      current = current->next;
}
}
//if data found return current link
  return current;

}

//delete a link with given key
struct node* delete(int key){

//start from the first link
  struct node* current = head;
  struct node* previous = NULL;

  if(head == NULL){
    return NULL;
}
  while(current->key != key){

//if it is the last node
    if(current->next==NULL){
      return NULL;
    }else{
//store refer to current link

       previous = current;
//move to next link
       current = current->next;
}
}
  if(current == head){
    head = head->next;
}  else{
     //bypass the current link
     previous->next = current->next;
}
   return current;
}


  
