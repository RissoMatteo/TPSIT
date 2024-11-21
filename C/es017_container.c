#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/*
author: Noemi Baruffolo
date: 09/02/2024
es: 17 container
text: Forse sai che alle banchine del Porto i Container sono dei grandi contenitori di merci.
La gru solleva i Container e li mette in pila uno sull’altro, poi dalla banchina li carica nelle stive delle navi.
Dichiara una struttura Container coi campi:
Codice
Peso
Tara
Scrivi un programma che carica in una pila i dati dei Container poi stampa a video i dati.
*/

typedef struct container{
    int codice;
    float peso;
    float tara;
    struct container* next;
} Container;

int is_empty(Container* head){
    if(head == NULL){
        return 1;
    } else{
        return 0;
    }
}

void push(Container** head, Container* element){
    if(is_empty(*head)){
        *head = element;
        element->next = NULL;
    } else{
        element->next = *head;
        *head = element;
    }
}

Container* pop(Container** head){
    Container* ret = *head;
    if(is_empty(*head)){
        return NULL;
    } else{
        *head = ret->next;
    }
    return ret;
}

void stampaPila(Container* head){
    Container* l = head;
    printf("\nValori pila:\n");
    printf("codice peso tara\n");
    while (l != NULL){
        printf("%d ", l->codice);
        printf("%.2f ", l->peso);
        printf("%.2f \n", l->tara);
        l = l ->next;
    }
}

int main(){
    int codice;
    float peso;
    float tara;
    Container* head = NULL;

    do{
        printf("inserire il codice del container o -1 per terminare: ");
        scanf("%d", &codice);
        if(codice >= 0){
            printf("inserire il peso del container: ");
            scanf("%f", &peso);
            printf("inserire la tara del container: ");
            scanf("%f", &tara);

            Container* element = (Container*) malloc(sizeof(Container));
            element->codice = codice;
            element->peso = peso;
            element->tara = tara;
            push(&head, element);
        }
    } while (codice >= 0);

    stampaPila(head);

    printf("\nFaccio la pop del container con il codice:\n");
    Container*  removed = pop(&head);
    printf("%d\n", removed->codice);

    stampaPila(head);
    
    return 0;
}