#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

/*
author: Noemi Baruffolo
date: 26/01/2024
es: 015 film
text: Scrivere un programma dove  dichiarari una struttura FILM con i campi:
Titolo, 
Anno, 
Genere;
il programma deve prendere in ingresso i dati di un film, costruire una struttura e metterla in pila (ad es. “Leon”, 1994, “Azione”),
poi estrai dalla pila il film e lo stampi a schermo.
*/

typedef struct film{ // Nodo della coda che rappresenta una persona
    char* titolo;
    int anno;
    char* genere;
    struct film* next;
}Film;

int is_empty(Film* head){
    return head == NULL;
}

void inserisciInCoda(Film** head, Film** tail, Film* elem){
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

Film* rimuoviDallaCoda(Film** head, Film** tail){
    //dequeue
    Film* ret = *head;
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


void visualizzaCoda(Film *head)
{
    Film *h = head;
    printf("Coda: \n");
    while (h != NULL)
    {
        printf("%s, %s, %d\n", h->titolo, h->genere, h->anno);
        h = h->next;
    }
}

//come uscita da programma, ma iterativa e non ricorsiva
void rimuoviTutti(Film** head, Film** tail){
    Film* corrente = *head;
    Film* next;
    while(corrente != NULL){
        next=corrente->next;
        free(corrente);
        corrente=next;
    }
}

void uscitaProgramma(Film *head){
    if(head->next != NULL){
        uscitaProgramma(head->next);
    }
        free(head);
}

int main() {
    Film* head = (Film*)malloc(sizeof(Film));
    Film* tail = (Film*)malloc(sizeof(Film));
    Film* elemento = (Film*)malloc(sizeof(Film));
    Film* elemento2 = (Film*)malloc(sizeof(Film));
    Film* temp;

    head = NULL;
    tail = NULL;
    elemento->genere = "Azione";
    elemento->titolo = "Leon";
    elemento->anno = 1994;
    elemento->next = NULL;
    inserisciInCoda(&head, &tail, elemento);

    elemento2->genere = "Fantasy";
    elemento2->titolo = "Harry Potter e la pietra filosofale";
    elemento2->anno = 2001;
    elemento2->next = NULL;

    inserisciInCoda(&head, &tail, elemento2);
    visualizzaCoda(head);

    temp = rimuoviDallaCoda(&head, &tail);
    printf("titolo film rimosso: '%s'\n",*temp);

    visualizzaCoda(head);
    uscitaProgramma(elemento);
    return 0;
}