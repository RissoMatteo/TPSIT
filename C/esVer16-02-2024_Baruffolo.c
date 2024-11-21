#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

#define LIM_MIN 1
#define LIM_MAX 10
#define NUM_ELEMENTI 5

/*
author: Noemi Baruffolo
date: 16/02/2024
es: verifica 
text: 
*/

//pila
typedef struct pila{
    int* numero;
    int valore;
    struct pila* next;
} Pila;

//coda
typedef struct Numero {
    int* numero;
    int valore;
    struct Numero* next;
} Numero;

typedef struct Coda {
    Numero* front;
    Numero* rear;
} Coda;

//pila
int is_empty(Pila* head){
    if(head == NULL){
        return 1;
    } else{
        return 0;
    }
}

void push(Pila** head, Pila* element){
    if(is_empty(*head)){
        *head = element;
        element->next = NULL;
    } else{
        element->next = *head;
        *head = element;
    }
}

Pila* pop(Pila** head){
    Pila* ret = *head;
    if(is_empty(*head)){
        return NULL;
    } else{
        *head = ret->next;
    }
    return ret;
}

void stampaPila(Pila* head){
    Pila* l = head;
    printf("\nValori pila:\n");
    printf("codice peso tara\n");
    while (l != NULL){
        printf("%d ", l->numero);
        l = l ->next;
    }
}

//coda
Coda* creaCoda() {
    Coda* coda = (Coda*)malloc(sizeof(Coda));
    coda->front = coda->rear = NULL;
    return coda;
}

int isEmptyCoda(Coda* coda) {
    return coda->front == NULL;
}

void enqueue(Coda* coda, Numero* num) {
    Numero* n = (Numero*)malloc(sizeof(Numero));
 
    n->valore = num->valore;
    
    n->next = NULL;
    
    if (isEmptyCoda(coda)) {
        coda->front = coda->rear = n;
    } else {
        coda->rear->next = n;
        coda->rear = n;
    }
}

Numero* dequeue(Coda* coda) {
    if (isEmptyCoda(coda)) {
        printf("Errore: la coda è vuota\n");
        return NULL;
    }

    Numero* temp = coda->front;
    coda->front = coda->front->next;

    if (coda->front == NULL) {
        coda->rear = NULL;
    }

    return temp;
}

void stampaCoda(Numero *head){
    Numero *n = head;
    printf("Coda: \n");
    while (n != NULL){
        printf("n: %d, v: %d\n", n->numero, n->valore);
        n = n->next;
    }
}

//sfida tra pila e coda
void sfida(Coda* coda, Numero* numC, Pila* numP){
    bool pila = false;
    bool coda = false;
    int removed;
    if(numP->valore > numC->valore){ //se il valore nella pila è maggiore a quello della coda
        printf("Vince: %d ", numP->valore);
        dequeue(numC);
        pop(numP);
        numP->valore = numP->valore - numC->valore;
        push(numP);
    } else if(numP->valore == numC->valore){
        printf("Hanno lo stesso valore!");
        dequeue(numC);
        removed = pop(&numP);
    } else{ //se il valore nella coda è maggiore a quello della pila
        printf("Vince: %d ", numC->valore);
        removed = pop(&numP);
        dequeue(numC);
        numC->valore = numC->valore - numP->valore;
        enqueue(coda, numC);
    }
}


int main() {
    srand(time(NULL));

    //coda
    Coda* coda = creaCoda();
    Numero* num = (Numero*) malloc(sizeof(Numero));
    
    for(int cont = 0; cont < NUM_ELEMENTI; cont++){
        num->numero = cont;
        num->valore = LIM_MIN + rand() % (LIM_MAX + 1 - LIM_MIN); //numero random
        enqueue(coda, num);
    }

    stampaCoda(num);

    //pila
    Pila* head = NULL;
    Pila* numero = (Pila*) malloc(sizeof(Pila));

    for(int cont = 0; cont < NUM_ELEMENTI; cont++){
        num->numero = cont;
        num->valore = LIM_MIN + rand() % (LIM_MAX + 1 - LIM_MIN); //numero random
        push(&head, numero);
    }

    stampaPila(head);

    while(num->next != NULL || numero->next != NULL){
        printf("pila: %d coda: %d", num->valore, numero->valore);
        sfida(coda, num, numero);
    }
    if(pila){
        stampaPila(head);
    } else{
        stampaCoda(num);
    }

    free(coda);
    
    return 0;
}