#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define DIM 10

/*
author: Noemi Baruffolo
date: 18/09/2023
es: 001_puntatori
text: scrivere un programma in C che calcoli la somma degli elementi di un array utilizzando l'aritmetica dei puntatori. Nel programma
deve essere implementata la funzione "calcolaSomma(int vett[], int dim)", calcola la somma degli elementi dell'array utilizzando un
puntatore e restituisce la somma calcolata. Il main() dichiara un array, utilizza la funzione "calcolaSomma(vett[], dim)" e stampa il
risultato della funzione
*/

int calcolaSomma(int vett[], int dim){
    int somma = 0;

    for(int *p = vett; p < vett + dim; p++){
        somma += (*p); //somma += *(vett + k);
    }

    return somma;
}

int main() {
    int vett[DIM] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int somma = 0;
    somma = calcolaSomma(vett, DIM);
    printf("La somma e': %d", somma);

    return 0;
}