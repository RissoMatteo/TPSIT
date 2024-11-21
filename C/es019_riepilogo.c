#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/*
author: Noemi Baruffolo
date: 19/02/2024
es: riepilogo puntatori
text: Esercizio di riepilogo sui Puntatori
Implementare strutture dati a coda e pila utilizzando puntatori, gestire operazioni come l'inserimento, l'estrazione e il confronto di
elementi tra di esse.
Il codice deve soddisfare i seguenti punti:
- Creare una struttura per i nodi di una lista (Nodo) con un campo dati e un puntatore al prossimo nodo.
- Implementare una struttura per la coda (Coda) con puntatori all'inizio e alla fine.
- Implementare una struttura per la pila (Pila) con un puntatore alla cima.
- Creare funzioni di inizializzazione per la coda e la pila.
- Implementare funzioni per l'inserimento (inserisci) e l'estrazione (estrai) nella coda.
- Implementare funzioni per l'inserimento (inserisci) e l'estrazione (estrai) nella pila.
- Scrivere una funzione per confrontare due code e determinare se sono uguali (equals).
All'interno del programma principale, eseguire operazioni di inserimento, estrazione e confronto utilizzando le strutture create,
sfruttando la memoria dinamica (malloc e free) per gestire la creazione e la distruzione dei nodi, assicurarsi di trattare adeguatamente
i casi in cui la coda o la pila risultano vuote. 
*/

//struttura nodo
typedef struct node{
    int dati;
    struct node* next;
} Node;

//pila
typedef struct pila{
    int dati;
    struct pila* next;
} Pila;

//coda
typedef struct Coda {
    Node* front;
    Node* rear;
} Coda;

//coda
Coda* creaCoda() {
    Coda* coda = (Coda*)malloc(sizeof(Coda));
    coda->front = coda->rear = NULL;
    return coda;
}

int isEmptyCoda(Coda* coda) {
    return coda->front == NULL;
}

void enqueue(Coda* coda, Node* node) {
    Node* n = (Node*)malloc(sizeof(Node));
 
    n->dati = node->dati;
    
    n->next = NULL;
    
    if (isEmptyCoda(coda)) {
        coda->front = coda->rear = n;
    } else {
        coda->rear->next = n;
        coda->rear = n;
    }
}

Node* dequeue(Coda* coda) {
    if (isEmptyCoda(coda)) {
        printf("Errore: la coda è vuota\n");
        return NULL;
    }

    Node* temp = coda->front;
    coda->front = coda->front->next;

    if (coda->front == NULL) {
        coda->rear = NULL;
    }

    return temp;
}

//pila
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
        printf("%d ", l->dati);
        l = l ->next;
    }
}

bool areEquals(Node* datoC, Pila* datoP){
    bool uguali = false;
    if(datoC->dati == datoP->dati){
        uguali = true;
    }
    return uguali;
}

int main() {
    int numC = 1;
    int numP = 1;
    //coda
    Coda* coda = creaCoda();
    Node* datoC = (Node*) malloc(sizeof(Node));

    //pila
    Pila* head = NULL;
    Pila* datoP = (Pila*) malloc(sizeof(Pila));
    
    datoC->dati;
    datoP->dati;

    enqueue(coda, datoC);
    push(&head, datoP);
    free(coda);

    stampaCoda(datoC);
    stampaPila(head);

    if(areEquals(datoC, datoP)){
        printf("Sono uguali! ");
    }else{
        printf("Non sono uguali! ");
    }


    return 0;
}