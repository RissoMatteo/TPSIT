#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/*
author: Noemi Baruffolo
date: 12/01/2024
es: 011
text: data in input una stringa e usando una pila, verificare se è palindroma o no
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


void push(Node** head, char value) {
    Node* element = (Node*)malloc(sizeof(Node));
    element->valore = value;

    if (is_empty(*head)) {
        *head = element;
        element->next = NULL;
    } else {
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

void stampaPila(Node* head) {
    Node* l = head;
    printf("\nValori lista: ");

    while (l != NULL) {
        printf("%c ", l->valore);
        l = l->next;
    }
}

bool isPalindromo(char* str) {
    Node* head = NULL;

    for (int cont = 0; str[cont] != '\0'; cont++) {
        push(&head, str[cont]);
    }

    char popped;
    for (int cont = 0; str[cont] != '\0'; cont++) {
        Node* removed = pop(&head);
        popped = removed->valore;

        if (popped != str[cont]) {
            return false;
        }
    }

    return true;
}

int main() {
    char* str;

    printf("Inserire una parola: ");

    str = (char*)malloc(100 * sizeof(char));

    if (str == NULL) {
        printf("Errore di allocazione di memoria.");
        return 1;
    }

    fflush(stdin);
    scanf("%s", str);

    if (isPalindromo(str)) {
        printf("\nLa stringa e' palindroma.\n");
    } else {
        printf("\nLa stringa non e'palindroma.\n");
    }

    free(str);

    return 0;
}