#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define DIM 10

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