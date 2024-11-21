#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/*
author: Noemi Baruffolo
date: 12/01/2024
es: 011
text: data in input una stringa e usando una pila, verifichi se è palindroma o no
*/

typedef struct node{
    char valore;
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

int main() {
    char c;
    Node* head = NULL;

    do{
        printf("inserire una lettera o -1 per terminare: ");
        scanf("%c", &c);
        if(c >= 0){
            Node* element = (Node*) malloc(sizeof(Node));
            element->valore = c;
            push(&head, element);
        }
    } while (c >= 0);

    stampaPila(head);

    printf("\nFaccio la pop:\n");
    Node*  removed = pop(&head);
    printf("%d\n", removed->valore);

    stampaPila(head);
    
    return 0;
}