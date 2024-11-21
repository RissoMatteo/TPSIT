#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

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

struct Persona {
    char* nome;
    char* cognome;
    int eta;
    struct Persona* next;
};

struct Coda { //struttura della coda
    struct Persona* front; //è un puntatore che punta all'ultimo elemento
    struct Persona* rear;
};

struct Coda* creaCoda() { //alloca in modo dinamico una struttura struct Coda
    //la malloc alloca in modo dinamico un nuovo nodo della coda
    struct Coda* coda = (struct Coda*)malloc(sizeof(struct Coda));
    coda->front = coda->rear = NULL; //inizializazzione del puntatore front e rear a NULL
    return coda;
}

void caricaPersone(struct Persona* persona){
    printf("Inserisci il cognome: ");
    persona->cognome = (char*)malloc(50 * sizeof(char));
    scanf("%s", persona->cognome);

    printf("Inserisci il nome: ");
    persona->nome = (char*)malloc(50 * sizeof(char));
    scanf("%s", persona->nome);

    printf("Inserisci l'eta': ");
    scanf("%d", &persona->eta);
}

void inserisciInCoda(struct Coda* coda, struct Persona* persona) {
    struct Persona* nuovaPersona = (struct Persona*)malloc(sizeof(struct Persona));
    nuovaPersona->nome = strdup(persona->nome);
    nuovaPersona->cognome = strdup(persona->cognome);
    nuovaPersona->eta = persona->eta;
    nuovaPersona->next = NULL;

    if (coda->rear == NULL) {
        coda->front = coda->rear = nuovaPersona;
    } else {
        coda->rear->next = nuovaPersona;
        coda->rear = nuovaPersona;
    }
}

int isEmptyCoda(struct Coda* coda) { //la funzione isEmptyCoda restituisce 1 se la coda è vuota altrimenti restituisce 0
    return coda->front == NULL;
}

int sizeCoda(struct Coda* coda) { //con sizeCoda restituisce gli elementi con un conteggio iterativo
    int count = 0;
    struct Persona* temp = coda->front;
    while (temp != NULL) {
        count++;
        temp = temp->next;
    }
    return count;
}

void enqueue(struct Coda* coda, struct Persona* persona) {
    struct Persona* nuovaPersona = (struct Persona*)malloc(sizeof(struct Persona));
    strcpy(nuovaPersona->nome, persona->nome);
    strcpy(nuovaPersona->cognome, persona->cognome);
    nuovaPersona->eta = persona->eta;
    nuovaPersona->next = NULL; //inizializza il campo next indicando che è l'ultimo nodo nella coda

    if (isEmptyCoda(coda)) {//verifica coda vuota
    //se la coda risulta vuota il nuovo nodo è sia front che rear della coda
        coda->front = coda->rear = nuovaPersona;
    } else {
        //se la coda non è vuota aggiorna il puntatore next
        coda->rear->next = nuovaPersona;
        coda->rear = nuovaPersona;
    }
}

struct Persona* dequeue(struct Coda* coda) { //la funzione dequeue, rimuove e restituisce il primo elemento
    if (isEmptyCoda(coda)) {
        printf("Errore: la coda e' vuota\n");
        return NULL;
    }

    struct Persona* temp = coda->front; //aggiorna front
    coda->front = coda->front->next;

    if (coda->front == NULL) { //front e rear sono puntatori che indicano il primo e l'ultimo elemento della coda
        coda->rear = NULL; //imposta rear a NULL
    }
// la variabile temp è un puntatore temporaneo per memorizzare il puntatore al primo elemento prima che la funzione dequeue la rimuva
    return temp;
}

void visualizzaCoda(struct Coda* coda) {
    if (coda->front == NULL) {
        printf("La coda e' vuota.\n");
        return;
    }

    struct Persona* temp = coda->front;
    while (temp != NULL) {
        printf("Nome: %s, Cognome: %s, Eta': %d\n", temp->nome, temp->cognome, temp->eta);
        temp = temp->next;
    }
}

void rimuoviDallaCoda(struct Coda* coda) {
    if (coda->front == NULL) {
        printf("Errore: la coda e' vuota\n");
        return;
    }

    struct Persona* temp = coda->front;
    struct Persona* personaMaxEta = coda->front;
    struct Persona* prev = NULL;

    while (temp->next != NULL) {
        if (temp->next->eta > personaMaxEta->eta) {
            personaMaxEta = temp->next;
            prev = temp;
        }
        temp = temp->next;
    }

    if (prev == NULL) {
        coda->front = personaMaxEta->next;
    } else {
        prev->next = personaMaxEta->next;
    }

    if (coda->rear == personaMaxEta) {
        coda->rear = prev;
    }

    printf("Persona rimossa: Nome: %s, Cognome: %s, Eta': %d\n", personaMaxEta->nome, personaMaxEta->cognome, personaMaxEta->eta);
    free(personaMaxEta->nome);
    free(personaMaxEta->cognome);
    free(personaMaxEta);
}

void uscitaProgramma(struct Coda* coda) {
    while (coda->front != NULL) {
        struct Persona* persona = coda->front;
        coda->front = coda->front->next;
        free(persona->nome);
        free(persona->cognome);
        free(persona);
    }

    free(coda);
}

int main() {
    struct Coda* coda = creaCoda();
    struct Persona persona;

    char risposta;
    do {
        caricaPersone(&persona);
        inserisciInCoda(coda, &persona);

        printf("Vuoi inserire un'altra persona? (s/n): ");
        scanf(" %c", &risposta);
    } while (risposta == 's' || risposta == 'S');

    printf("Contenuto della coda:\n");
    visualizzaCoda(coda);

    rimuoviDallaCoda(coda);

    printf("Contenuto della coda dopo la rimozione:\n");
    visualizzaCoda(coda);

    uscitaProgramma(coda);

    return 0;
}