#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

#define LUNG_RIGA 200
#define NOME_FILE "sintesi.csv"

/*
author: Noemi Baruffolo
date: 17/10/2023
es: sintesi
text:
-Creare un file .csv con COGNOME, NOME, NASCITA (annomesegiorno in formato INT)
-scorrere il file con la funzione FGETS e STRTOK
-stampare in ordine DECRESCENTE (dal più grande al più piccolo)
 utilizzando i puntatori e allocazione dinamica (MALLOC)
*/

typedef struct {
    char* cognome;
    char* nome;
    int data;
} Persona;

int contaPersone(char nomeFile[]) {
    int c;
    int cont = 0;

    FILE *fp;
    fp = fopen(nomeFile, "r");

    if (fp != NULL) {
        while ((c = fgetc(fp)) != EOF) {
            if (c == '\n') {
                cont++;
            }
        }
        fclose(fp); // chiude il file
    }
    return cont;
}

void caricaFile(Persona contatti[], char* fileName, char* campo, char* riga, int dim) {
    FILE* fp;
    fp = fopen(fileName, "r");
    int cont = 0;

    if (fp == NULL) {
        printf("Il file %s non esiste o e' vuoto!\n", fileName);
        exit(1);
    }

    for (Persona* p = contatti; p < contatti + dim; p++) {
        fgets(riga, LUNG_RIGA, fp);
        campo = strtok(riga, ",");
        p->cognome = strdup(campo);

        campo = strtok(NULL, ",");
        p->nome = strdup(campo);

        campo = strtok(NULL, ",");
        p->data = atoi(campo);

        cont++;
    }

    fclose(fp); // chiude il file
}

void swap(Persona *a, Persona *b) {
    Persona temp = *a;
    *a = *b;
    *b = temp;
}

void bubbleSort3(Persona contatto[], int n) {
    int sup, sca;
    sup = n - 1;

    while (sup > 0) {
        sca = 0;

        for (int cont = 0; cont < sup; cont++) {
            if ((contatto + cont)->data < (contatto + cont + 1)->data) {
                swap(contatto + cont, contatto + cont + 1);
                sca = cont;
            }
        }

        sup = sca;
    }
}

void stampaPersona(Persona contatti[], int dim) {
    int temp = 0;
    for (Persona* cont = contatti + dim - 1; cont >= contatti; cont--) {
        printf("\n%s %s ", cont->cognome, cont->nome);
        printf("%02d/", cont->data % 100);
        temp = cont->data / 100;
        printf("%02d/", temp % 100);
        printf("%d", temp / 100);
    }
}

int main() {
    int dim;
    dim = contaPersone(NOME_FILE);
    Persona* contatti;

    contatti = (Persona*)malloc(dim * sizeof(Persona));
    char riga[LUNG_RIGA];
    char* campo;

    caricaFile(contatti, NOME_FILE, campo, riga, dim);

    bubbleSort3(contatti, dim);

    stampaPersona(contatti, dim);

    free(contatti); // Libera la memoria allocata dinamicamente

    return 0;
}