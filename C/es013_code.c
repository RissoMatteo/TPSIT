#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/*
author: Noemi Baruffolo
date: 26/01/2024
es: 013
text: esempio coda in c
*/

struct Num { //nodo della coda che contiene un intero ossia key
    int key;
    struct Num* next;
};

struct Coda { //struttura della coda
    struct Num* front; //è un puntatore che punta all'ultimo elemento
    struct Num* rear;
};
  //si crea la coda
struct Coda* creaCoda() { //alloca in modo dinamico una struttura struct Coda
    //la malloc alloca in modo dinamico un nuovo nodo della coda
    struct Coda* coda = (struct Coda*)malloc(sizeof(struct Coda));
    coda->front = coda->rear = NULL; //inizializazzione del puntatore front e rear a NULL
    return coda;
}

int isEmptyCoda(struct Coda* coda) { //la funzione isEmptyCoda restituisce 1 se la coda è vuota altrimenti restituisce 0
    return coda->front == NULL;
}

int sizeCoda(struct Coda* coda) { //con sizeCoda restituisce gli elementi con un conteggio iterativo
    int count = 0;
    struct Num* temp = coda->front;
    while (temp != NULL) {
        count++;
        temp = temp->next;
    }
    return count;
}

void enqueue(struct Coda* coda, struct Num* numero) {
    struct Num* nuovoNumero = (struct Num*)malloc(sizeof(struct Num));
    nuovoNumero->key = numero->key; //assegna il valore della key
    nuovoNumero->next = NULL; //inizializza il campo next indicando che è l'ultimo nodo nella coda

    if (isEmptyCoda(coda)) {//verifica coda vuota
    //se la coda risulta vuota il nuovo nodo è sia front che rear della coda
        coda->front = coda->rear = nuovoNumero;
    } else {
        //se la coda non è vuota aggiorna il puntatore next
        coda->rear->next = nuovoNumero;
        coda->rear = nuovoNumero;
    }
}

struct Num* dequeue(struct Coda* coda) { //la funzione dequeue, rimuove e restituisce il primo elemento
    if (isEmptyCoda(coda)) {
        printf("Errore: la coda è vuota\n");
        return NULL;
    }

    struct Num* temp = coda->front; //aggiorna front
    coda->front = coda->front->next;

    if (coda->front == NULL) { //front e rear sono puntatori che indicano il primo e l'ultimo elemento della coda
        coda->rear = NULL; //imposta rear a NULL
    }
// la variabile temp è un puntatore temporaneo per memorizzare il puntatore al primo elemento prima che la funzione dequeue la rimuva
    return temp;
}

int main() { //nel main si crea una coda con la funzione creaCoda
    struct Coda* coda = creaCoda();

    struct Num num1 = {4, NULL};
    struct Num num2 = {5, NULL};
    struct Num num3 = {6, NULL};

    enqueue(coda, &num1); //  enqueue inserimento
    enqueue(coda, &num2);
    enqueue(coda, &num3);

    printf("Dimensione della coda: %d\n", sizeCoda(coda)); //stampa dimensione

    while (!isEmptyCoda(coda)) {
        struct Num* numeroCoda = dequeue(coda); // rimozione dequeue
        printf("Numero dalla coda: %d\n", numeroCoda->key);
        free(numeroCoda); // Deallocazione dell'elemento
    }

    free(coda);

    return 0;
}