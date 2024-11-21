#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/*
author: Noemi Baruffolo
date: 21/09/2023
es: 004
text: Scrivi un programma in linguaggio C che consenta all'utente di creare un array dinamico
di interi. Il programma deve avere una dimensione array specificata, usando la
funzione malloc per allocare in modo dinamico gli interi.
L’utente deve poter inserire valori interi, che verranno stampati. Assicurarsi di liberare la
memoria allocata dinamicamente utilizzando la funzione free alla fine del
programma per evitare perdite di memoria.
*/

int chiediDim(int min, int max, char mess[]) {
    int n;

    do{
        printf(mess);
        scanf("%d", &n);
    } while(n < min || n > max);
    return n;
}

void caricaVett(int* vett, int dim){
    printf("Inserisci %d valori interi:\n", dim);

        for (int *p = vett; p < vett + dim; p++) {
            scanf("%d", p);
        }
}

void stampaVett(int* vett, int dim) {
    printf("Valori inseriti:\n");
    for (int *p = vett; p < vett + dim; p++) {
        printf("%d ", *p);
    }
    printf("\n");
}

int main() {
    int dim;
    int* vett;
    
    printf("Inserisci la dimensione del vettore: ");
    scanf("%d", &dim);

    vett = (int*)malloc(dim * sizeof(int));

    if (vett != NULL) {

        caricaVett(vett, dim);

        stampaVett(vett, dim);

        free(vett); // Libera la memoria allocata dinamicamente
    }

    return 0;
}