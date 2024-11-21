#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

/*
author: Noemi Baruffolo
date: 26/01/2024
es: 014
text: Gestione di una Coda di Persone

È richiesto di creare un programma in linguaggio C che gestisca una coda di persone.
Ogni persona è rappresentata da un elemento che contiene le seguenti informazioni:
- Nome
- Cognome
- Età 

Il programma dovrà eseguire le seguenti operazioni:

1. Inserimento nella coda: Implementare una funzione chiamata “inserisciInCoda” che consenta l'inserimento di una persona nella coda.
La funzione chiederà all'utente di inserire il nome, cognome ed età della persona e successivamente inserirà l'elemento nella coda.

2. Visualizzazione della coda: Implementare una funzione chiamata “visualizzaCoda” che stampi a video le informazioni di tutte le
persone presenti nella coda. Se la coda è vuota, verrà stampato un messaggio adeguato.

3. Rimozione dalla coda: Implementare una funzione chiamata “rimuoviDallaCoda” che rimuova la persona più anziana presente nella coda.
Nel caso in cui ci siano persone con la stessa età massima, verrà rimossa la prima persona inserita con quell'età.

4. Uscita dal programma: Implementare una funzione chiamata “uscitaProgramma” che liberi la memoria allocata per la coda e termini il
programma.
*/

typedef struct persona{ // Nodo della coda che rappresenta una persona
    char* nome;
    char* cognome;
    int eta;
    struct persona* next;
}Persona;

int is_empty(Persona* head){
    return head == NULL;
}

void inserisciInCoda(Persona** head, Persona** tail, Persona* elem){
    //enqueue
    if(is_empty(*head)){
        *head = elem;
    }
    else{
        (*tail)->next = elem;
    }
    *tail = elem;
    elem->next = NULL;
}

Persona* rimuoviDallaCoda(Persona** head, Persona** tail){
    //dequeue
    Persona* ret = *head;
    if(is_empty(*head)){
        return NULL;
    }
    else{
        *head = ret->next;
    }
    if(*head == NULL){
        *tail = NULL;
    }
    return ret;
}


void visualizzaCoda(Persona *head)
{
    Persona *h = head;
    printf("Coda: \n");
    while (h != NULL)
    {
        printf("%s, %s, %d\n", h->nome, h->cognome, h->eta);
        h = h->next;
    }
}

//come uscita da programma, ma iterativa e non ricorsiva
void rimuoviTutti(Persona** head, Persona** tail){
    Persona* corrente = *head;
    Persona* next;
    while(corrente != NULL){
        next=corrente->next;
        free(corrente);
        corrente=next;
    }
}

void uscitaProgramma(Persona *head){
    if(head->next != NULL){
        uscitaProgramma(head->next);
    }
        free(head);
}

int main() {
    Persona* head = (Persona*)malloc(sizeof(Persona));
    Persona* tail = (Persona*)malloc(sizeof(Persona));
    Persona* elemento = (Persona*)malloc(sizeof(Persona));
    Persona* elemento2 = (Persona*)malloc(sizeof(Persona));
    Persona* temp;

    head = NULL;
    tail = NULL;
    elemento->cognome = "Baruffolo";
    elemento->nome = "Noemi";
    elemento->eta = 18;
    elemento->next = NULL;
    inserisciInCoda(&head, &tail, elemento);

    elemento2->cognome = "Rossi";
    elemento2->nome = "Andrea";
    elemento2->eta = 18;
    elemento2->next = NULL;

    inserisciInCoda(&head, &tail, elemento2);
    visualizzaCoda(head);

    temp = rimuoviDallaCoda(&head, &tail);

    visualizzaCoda(head);
    uscitaProgramma(elemento);
    return 0;
}