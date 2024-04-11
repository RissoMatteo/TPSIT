#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

#define STRL 101
#define LUNG_RIGA 200
#define NOME_FILE "sintesi.csv"

typedef struct{
    char* title; //char title[STRL];
    char* author;
    int year;
} Libro;

int contaLibri(char nomeFile[]) {
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

int chiediDim(int min, int max, char mess[]) {
    int n;

    do{
        printf(mess);
        scanf("%d", &n);
    } while(n < min || n > max);
    return n;
}

void caricaFile(Libro* archivio, char* fileName, char* campo, char* riga, int dim) {
    FILE* fp;
    fp = fopen(fileName, "r");
    int k = 0;

    if(fp == NULL) {
        printf("Il file %s non esiste o e' vuoto!\n", fileName);
        exit(1);   
    }

    for (Libro *p = archivio; p < archivio + dim; p++) {

        fgets(riga, LUNG_RIGA, fp);
        campo = strtok (riga,",");

        campo = strtok (NULL,",");
        p->title = strdup(campo); //strdup duplica il campo

        campo = strtok (NULL,",");
        p->author = strdup(campo);

        campo = strtok (NULL,",");
        p->year = atoi(campo); //atoi passa da stringa e int con atof da stringa a float

        k++;

        }
        fclose(fp); //chiude il file
}

void stampaLibro(Libro* archivio, int dim) {
   for (Libro *k = archivio; k < archivio + dim; k++){
        printf("\n%d %s %s %d %s", k->title, k->author, k->year);
    }
}

void stampaLibriData(Libro* archivio, int dim, int data) {
    int nx = 0;
    for (Libro *cont = archivio; cont < archivio + dim; cont++){
        if(data == cont->year){
            printf("\n%d %s %s %d %s", cont->title, cont->author, cont->year);
        }
    }
}

void swap(Libro *a, Libro *b) {
    Libro temp = *a;
    *a = *b;
    *b = temp;
}

void bubbleSort3(Libro archivio[], int dim) {
    int sup, sca; 
    sup = dim - 1;
    while (sup > 0) {
        sca = 0;
        for (Libro *p = archivio; p < archivio + sup; p++) {
            if (p->year < (p + 1)->year){
                swap(p, p + 1);
                sca = p - archivio;
            }
        }
        sup = sca;
    }
}

int main(){
    char fileName[] = "listaLibri.csv";
    int dim;
    int data;
    dim = contaLibri(fileName);
    Libro* archivio;
    
    archivio = (Libro*) malloc(dim * sizeof(Libro));
    char riga[LUNG_RIGA];
    char* campo;
      
    caricaFile(archivio, fileName, campo, riga, dim);

    stampaLibro(archivio, dim);

    printf("Inserisci un anno: ");
    scanf("%d", data);

    stampaLibriData(archivio, dim, data);

    bubbleSort3(archivio, dim);
    stampaLibro(archivio, dim);

    free(archivio);

    return 0;
}