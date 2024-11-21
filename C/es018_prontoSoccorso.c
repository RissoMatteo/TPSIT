#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/*
author: Noemi Baruffolo
date: 09/02/2024
es: 18 pronto soccorso
text: Nei Pronto Soccorsi dell’ospedale i pazienti sono classificati con un colore: 
rosso (urgentissimo)
giallo (grave)
verde (moderato)
bianco (lieve) 
Funziona così: quando una persona arriva al pronto soccorso l’infermiere lo registra (nome e età) e decide anche il colore di priorità;
appena un medico è libero deve gestire prima quelli con codice rosso, poi giallo, poi verde e poi bianco. 
Dichiara una struttura Paziente con i campi:
Nome,
Età,
Colore;
il programma deve gestire 4 code diverse e inserire il paziente nella lista corretta, quando un medico è libero entra il paziente
successivo, (quindi sceglie il primo dei pazienti codice verde solo se non ci sono codici rosso e giallo).
Le informazioni vanno visualizzate a schermo.
*/

typedef struct Paziente {
    char* nome;
    int eta;
    char* colore;
    struct Paziente* next;
} Paziente;

typedef struct Coda {
    Paziente* front;
    Paziente* rear;
} Coda;

Coda* creaCoda() {
    Coda* coda = (Coda*)malloc(sizeof(Coda));
    coda->front = coda->rear = NULL;
    return coda;
}

int isEmptyCoda(Coda* coda) {
    return coda->front == NULL;
}

void enqueue(Coda* coda, Paziente* paziente) {
    Paziente* p = (Paziente*)malloc(sizeof(Paziente));
 
    p->nome = strdup(paziente->nome);
    p->eta = paziente->eta;
    
    p->colore = strdup(paziente->colore);
    p->next = NULL;
    
    if (isEmptyCoda(coda)) {
        coda->front = coda->rear = p;
    } else {
        coda->rear->next = p;
        coda->rear = p;
    }
}

Paziente* dequeue(Coda* coda) {
    if (isEmptyCoda(coda)) {
        printf("Errore: la coda è vuota\n");
        return NULL;
    }

    Paziente* temp = coda->front;
    coda->front = coda->front->next;

    if (coda->front == NULL) {
        coda->rear = NULL;
    }

    return temp;
}

int main() {
    int num;
    Coda* codaRossa = creaCoda();
    Coda* codaGialla = creaCoda();
    Coda* codaVerde = creaCoda();
    Coda* codaBianca = creaCoda();

    int nColore = 0;

    do{
        printf("inserire il numero corrispondente alla scelta(1. aggiungi paziente 2.fare visitare il paziente) o -1 per terminare:\n");
        scanf("%d", &num);
        if(num == 1){
            Paziente* paziente = (Paziente*) malloc(sizeof(Paziente));
            paziente->nome = (char*) malloc(sizeof(char)* 100);
            paziente->colore = (char*) malloc(sizeof(char)* 100);

            printf("Inserisci il nome: ");
            fflush(stdin);
            scanf("%s", paziente->nome);
            printf("Inserisci l'eta': ");
            scanf("%d", &paziente->eta);
            printf("Inserisci il colore del codice d'emergenza: ");
            fflush(stdin);
            scanf("%s", paziente->colore);

            if(strcmp(paziente->colore, "rosso") == 0){ //rosso
                enqueue(codaRossa, paziente);
            }
            else if(strcmp(paziente->colore, "giallo") == 0){ //giallo
                enqueue(codaGialla, paziente);
            }
            else if(strcmp(paziente->colore, "verde") == 0){ //verde
                enqueue(codaVerde, paziente);
            }
            else if(strcmp(paziente->colore, "bianco") == 0){ //bianco
                enqueue(codaBianca, paziente);
            }
            printf("\nHo aggiunto il paziente nella coda %s !\n", paziente->colore);
           
        } else if(num == 2){
            Paziente* p = NULL;
            if(isEmptyCoda(codaRossa) != 1){
                p = dequeue(codaRossa);
            } else if(isEmptyCoda(codaGialla) != 1){
                p = dequeue(codaGialla);
            } else if(isEmptyCoda(codaVerde) != 1){
                p = dequeue(codaVerde);
            } else if(isEmptyCoda(codaBianca) != 1){
                p = dequeue(codaBianca);
            }
            if(p == NULL){
                printf("Nessun paziente in attesa!\n");
            } else{
                printf("Il paziente %s e' stato visitato con il codice %s\n", p->nome, p->colore);
            }
        }
    }while(num >= 0);
    free(codaRossa);
    free(codaGialla);
    free(codaVerde);
    free(codaBianca);

    return 0;
}