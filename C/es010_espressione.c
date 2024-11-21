#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

/*
author: Noemi Baruffolo
date: 13/11/2023
es: 010 espressione
text: chiedere una stringa in input, ciclo for su tutti i caratteri, quando trovo una parentesi aperta faccio push, gli altri caratteri
gli ignoro, se parentesi chiusa faccio pop. Se arrivo con la pila vuota, le parentesi sono giuste
*/

typedef struct node {
    char carattere;
    int posizione;
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
        printf("%d ", l->carattere);
        l = l ->next;
    }
}

void controllaParentesi(const char* stringa) {
    Node* pila = NULL;
    int posizione = 0;
    int len = strlen(stringa);

    for (int i = 0; i < len; ++i) {
        char carattere = stringa[i];
        posizione++;

        if (carattere == '{' || carattere == '[' || carattere == '(') {
            Node* element = (Node*)malloc(sizeof(Node));
            element->carattere = carattere;
            element->posizione = posizione;
            push(&pila, element);
        } else if (carattere == '}' || carattere == ']' || carattere == ')') {
            Node* parentesi = pop(&pila);
            if (parentesi == NULL ||
                (carattere == '}' && parentesi->carattere != '{') ||
                (carattere == ']' && parentesi->carattere != '[') ||
                (carattere == ')' && parentesi->carattere != '(')) {
                printf("Errore! Parentesi non corrispondenti alla posizione %d\n", posizione);
                return;
            }
            free(parentesi);
        }
    }

    if (!is_empty(pila)) {
        Node* parentesi = pop(&pila);
        printf("Errore! Parentesi non chiuse alla posizione %d\n", parentesi->posizione);
        free(parentesi);
        return;
    }

    printf("Parentesi corrette!\n");
}

int main(){
    char stringa[] = "{1+[2+3]*5}";
    
    controllaParentesi(stringa);
    
    return 0;
}