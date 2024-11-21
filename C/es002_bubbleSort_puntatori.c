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
text: Hai a disposizione un array di numeri interi disordinati,
ordinare questo array in modo crescente non è necessario conoscere in anticipo la lunghezza dell'array.
Si utilizzi la funzione swap: "swap(&arr[j], &arr[j + 1])" e l'algoritmo di ordinamento bubbleSort.
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
    
    for(int *p = vett; p < vett + dim; p++){
       (*p) = LIM_MIN + rand() % (LIM_MAX + 1 - LIM_MIN);
       //per controllare che ordini veramente stampo il vettore casuale
        printf("%d ", *p);
        printf("\n");
    }
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void bubbleSort3(int vett[], int n) {
    int sup, sca; 
    sup = n - 1;
    while (sup > 0) {
        sca = 0;
        for (int *p = vett; p < vett + sup; p++) {
            if (*p > *(p + 1)){
                swap(p, p + 1);
                sca = p - vett;
            }
        }
        sup = sca;
    }
}

void stampaVett(int vett[], int dim) {
    for (int *p = vett; p < vett + dim; p++) {
        printf("%d ", *p);
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

    bubbleSort3(vett, dim); //ordina il vettore
    
    printf("Vettore ordinato:\n");
    stampaVett(vett, dim);

    return 0;
}