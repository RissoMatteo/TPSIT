#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define LUNG_RIGA 200
#define NUM_RIGHE 20000
#define FILM 31
#define STRL 31

/*
author: Noemi Baruffolo
date: 18/09/2023
es: 000_malloc
text: La videoteca "Ciak film" necessita di un programma che carichi la lista film in un array di struttura e che stampi a video i 5
campi : numero, titolo film, genere, anno di uscita, disponibilità film

con puntatori
*/

typedef struct {
    int number;
    char* title; //char tittle[STRL];
    char* type;
    int year;
    char* state;
} Film;

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

void caricaFile(Film videoteca[], char* fileName, char* campo, char* riga, int dim) {
    FILE* fp;
    fp = fopen(fileName, "r");
    int k = 0;

    if(fp == NULL) {
        printf("Il file %s non esiste o e' vuoto!\n", fileName);
        exit(1);   
    }
    for (Film *p = videoteca; p < videoteca + dim; p++) {

        fgets(riga, LUNG_RIGA, fp);
        campo = strtok (riga,",");
        //(*(videoteca + k)).number = atoi(campo); //più pesante e scomoda, meglio la seguente
        p->number = atoi(campo); //atoi passa da stringa e int con atof da stringa a float

        campo = strtok (NULL,",");
        p->title = strdup(campo); //strdup duplica il campo

        campo = strtok (NULL,",");
        p->type = strdup(campo);

        campo = strtok (NULL,",");
        p->year = atoi(campo);

        campo = strtok (NULL,",");
        p->state = strdup(campo);

        k++;

        }
        fclose(fp); //chiude il file
}

void stampaFilm(Film videoteca[], int dim) {
   for (Film *k = videoteca; k < videoteca + dim; k++){
        printf("\n%d %s %s %d %s", k->number, k->title, k->type, k->year, k->state);
    }
}

int main() {
    char fileName[] = "listaFilmConVirgole.csv";
    int dim;
    dim = contaFilm(fileName);
    Film* videoteca;
    
    videoteca = (Film*) malloc(dim * sizeof(Film));
    char riga[LUNG_RIGA];
    char* campo;
      
    caricaFile(videoteca, fileName, campo, riga, dim);

    stampaFilm(videoteca, dim);

    free(videoteca);

    return 0;
}