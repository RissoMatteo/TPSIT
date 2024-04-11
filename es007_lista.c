#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

typedef struct El {
    int dato;
    struct El *next;
} Elemento;

int somma(Elemento *head, int n){
    if(head == NULL){
        return -1;
    }
    int somma = 0;
    Elemento *l = head;
    while(l != NULL){
        if(l->dato % n == 0){
            somma += l->dato;
        }
        l = l->next;
    }
    return somma;
}

int main(){
    int n, ris, numMult;
    Elemento* head = NULL;
    Elemento* l;

    do{
        printf("inserisci un naturale o -1 per terminare: ");
        scanf("%d", &n);
        if(n >= 0){
            if(head == NULL){
                head = (Elemento*) malloc(sizeof(Elemento));
                l = head;
            }
            else{
                l->next = (Elemento*) malloc(sizeof(Elemento));
                l = l->next;
            }
            l->dato = n;
            l->next = NULL;
        }
    }while(n >= 0);
    printf("inserisci il numero M: ");
    scanf("%d", &numMult);
    ris = somma(head, numMult);
    printf("la somma è: %d", ris);
    free(head);
    free(l);
    return 0;
}