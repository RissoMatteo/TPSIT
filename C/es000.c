#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define NOME_FILE "listafilm.csv"
#define FILM 31
#define STRL 31

/*
author: Noemi Baruffolo
date: 18/09/2023
es: 000
text: La videoteca "Ciak film" necessita di un programma che carichi la lista film in un array di struttura e che stampi a video i 5
campi : numero, titolo film, genere, anno di uscita, disponibilità film
*/

typedef struct {
    int number;
    char title[STRL];
    char type[STRL];
    int year;
    char state[STRL];
} Film;

/*
int contaFilm(char nomeFile[]) {
    int c;
    int cont = 0;

    FILE *fp;
    fp = fopen(nomeFile,"r");

    if(fp != NULL) {
        while ((c = fgetc(fp)) != EOF) {
            if(c =='\n') {
                cont++;
            }
        }
        fclose(fp); //chiude il file
    }
    return cont;
}
*/

int caricaFile(Film videoteca[], char nomeFile[]) {
    int k = 0;
    FILE *fp;
    fp = fopen(nomeFile, "r");

    if(fp != NULL) {
        while(fscanf(fp, "%d", &videoteca[k].number) != EOF) {
            fscanf(fp, "%s %s %d %s", videoteca[k].title, videoteca[k].type, &videoteca[k].year, videoteca[k].state);
            k++;
        }
        fclose(fp); //chiude il file
    } else {
        printf("Il file non esiste o e' vuoto!\n");
    }
    return k;
}

void stampaFilm(Film videoteca[], int dim) {
    for(int k = 0; k < dim; k++) {
        printf("\n%d %s %s %d %s", videoteca[k].number, videoteca[k].title, videoteca[k].type, videoteca[k].year, videoteca[k].state);
    }
}

int main() {
    Film videoteca[FILM];
    int dim;

    dim = caricaFile(videoteca, NOME_FILE);

    stampaFilm(videoteca, dim);

    return 0;
}