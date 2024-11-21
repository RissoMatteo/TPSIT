#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

/*
author: Noemi Baruffolo
date: 13/11/2023
es: 009 pile
text: creare una pila 
*/

typedef struct node{
    int valore;
    struct node* next;
} Node;

int is_empty(Node* head){
    if(head == NULL){
        return 1;
    } else{
        return 0;
    }
}

void push(Node** head, Node* element){
    if(is_empty(*head)){
        *head = element;
        element->next = NULL;
    } else{
        element->next = *head;
        *head = element;
    }
}

Node* pop(Node** head){
    Node* ret = *head;
    if(is_empty(*head)){
        return NULL;
    } else{
        *head = ret->next;
    }
    return ret;
}

void stampaPila(Node* head){
    Node* l = head;
    printf("\nValori lista: ");
    while (l != NULL){
        printf("%d ", l->valore);
        l = l ->next;
    }
}

int main(){
    int n;
    Node* head = NULL;

    do{
        printf("inserire un numero naturale o -1 per terminare: ");
        scanf("%d", &n);
        if(n >= 0){
            Node* element = (Node*) malloc(sizeof(Node));
            element->valore = n;
            push(&head, element);
        }
    } while (n >= 0);

    stampaPila(head);

    printf("\nFaccio la pop:\n");
    Node*  removed = pop(&head);
    printf("%d\n", removed->valore);

    stampaPila(head);
    
    return 0;
}