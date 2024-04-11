#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

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