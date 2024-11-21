#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

#define DIM 100
#define LIM_MIN 1
#define LIM_MAX 20

/*
author: Noemi Baruffolo
date: 9/10/2023
es: 002
text: Implementa l'algoritmo di ordinamento Selection Sort per ordinare un array di numeri interi,
con l'aritmetica dei puntatori, scambiando l'elemento minimo.
*/

int chiediDim(int min, int max, char mess[]) {
    int n;

    do{
        printf(mess);
        scanf("%d", &n);
    } while(n < min || n > max);
    return n;
}

void caricaVettCasualeConStampa(int vett[], int dim) {
    
    for(int k = 0; k < dim; k++){
       *(vett + k) = LIM_MIN + rand() % (LIM_MAX + 1 - LIM_MIN);
       //per controllare che ordini veramente stampo il vettore casuale
        printf("[%d]:%d ", k, vett[k]);
        printf("\n");
    }
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void selectionSort(int vett[],int n) {
    int k, kmin, j;

    for(k = 0;k < n - 1; k++) {
        kmin = k;

        for(j = k + 1; j < n; j++){
            if(*(vett + kmin) > *(vett + j)) // confronti
                kmin = j;
            }
        if(kmin != k){
            swap((vett + k), (vett + kmin)); //scambi
        }
    }
return;
}

void stampaVett(int vett[], int dim) {
    for (int k = 0; k < dim; k++) {
        printf("[%d]:%d ", k, vett[k]);
        printf("\n");
    }
    printf("\n");
}

int main() {
    int vett[DIM];
    int dim = chiediDim(LIM_MIN, DIM, "Inserisci il numero massimo di numeri caricabili nel vettore: ");

    srand(time(NULL));

    printf("Vettore casuale:\n");
    caricaVettCasualeConStampa(vett, dim);

    selectionSort(vett, dim); //ordina il vettore
    
    printf("Vettore ordinato:\n");
    stampaVett(vett, dim);

    return 0;
}