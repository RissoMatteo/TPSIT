#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

/*
author: Noemi Baruffolo
date: 1/12/2023
es: 008
text:
 Supponendo
date le seguenti definizioni:
typedef struct El {
    int s;
    struct El *next;
}ElementoLista;
 typedef ElementoLista *ListaDiInteri;
• definire una funzione FirstEven che, data
una ListaDiInteri restituisce la posizione (puntatore) del primo elemento pari
nella lista (restituisce NULL se la lista non contiene elementi pari).
ListaDiInteri FirstEven(ListaDiInteri lis) {
 while (lis != NULL) {
     if (lis->s % 2 == 0)
            return lis;
  // il primo pari è in lis
       else
        lis = lis ->next;
     }
     return NULL;
 }

*/
typedef struct El {
    int s;
    struct El *next;
}ElementoLista;

ElementoLista* firstEven(ElementoLista* lis) {
    while (lis != NULL) {
        if (lis->s % 2 == 0)
            return lis;
        else
            lis = lis->next;
    }
    return NULL;
}

int main(){
    int n;
    ElementoLista* lista = NULL;
    ElementoLista* l;
    do{
        printf("inserisci un naturale o -1 per terminare: ");
        scanf("%d", &n);
        if(n >= 0){
            if(lista == NULL){
                lista = (ElementoLista*) malloc(sizeof(ElementoLista));
                l = lista;
            }
            else{
                l->next = (ElementoLista*) malloc(sizeof(ElementoLista));
                l = l->next;
            }
            l->s = n;
            l->next = NULL;
        }
    }while(n >= 0);
    ElementoLista* posPrimoPari = firstEven(lista);
    printf("valore: %d", posPrimoPari->s);

    return 0;
}