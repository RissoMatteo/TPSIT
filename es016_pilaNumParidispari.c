#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

typedef struct numero{
    int num;
    struct numero* next;
}Numero;

bool is_empty(Numero* head){
    return head == NULL;
}

void push(Numero **head, Numero *element){
    if(is_empty(*head)){
        *head = element;
        element->next = NULL;
    }
    else{
        element->next = *head;
        *head = element;
    }
}

Numero* pop(Numero **head){
    Numero* stack;
    if(is_empty(*head)){
        return NULL;
    }
    else{
        stack = *head;
        *head = stack->next;
    }
    return stack;
}

Numero* pila_pari_dispari(Numero* head){
    Numero* p;
    while(head->next != NULL){
        p = (Numero*)malloc(sizeof(Numero));
        if(head->num % 2 == 0)
            push(&p, head);
        head = head->next;
    }
    while(head->next != NULL){
        p = (Numero*)malloc(sizeof(Numero));
        if(head->num % 2 != 0)
            push(&p, head);
        head = head->next;
    }
    return p;
}

void print_stack(Numero* head){
    Numero* s = head;
    while(s != NULL){
        printf("%d ", s->num);
        s = s->next;
    }
}

int main(){
    Numero* head;
    Numero* el;
    Numero* pila_finale;
    char car = 'n';
    int n;
    while(car == 'n'){
        head = (Numero*)malloc(sizeof(Numero));
        el = (Numero*)malloc(sizeof(Numero));
        printf("inserisci un numero: ");
        scanf("%d", &n);
        el->num = n;
        push(&head, el);
        head = head->next;
        printf("vuoi fermare? (s o n): ");
        fflush(stdin);
        scanf("%c", &car);
    }
    pila_finale = pila_pari_dispari(head);
    print_stack(pila_finale);
    free(head); free(el); free(pila_finale);
    return 0;
}