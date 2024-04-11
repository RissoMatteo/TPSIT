#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


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