#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node{
        char ch;
        struct node* next;
} node;


void print_word(FILE *f, node* word) {
    if(word->next != NULL && word->next->next != NULL)
        print_word(f, word->next);
    fputc(word->ch, f);
    free(word);
}


int main(int argc, char **argv)
{
    char ch;
    FILE *fp1;
    FILE *fp2;

    fp1 = fopen(argv[1], "r");
    fp2 = fopen(argv[2], "w");

    if (fp1 == NULL || fp2 == NULL)
    {
        perror("Error while opening the file.\n");
        exit(EXIT_FAILURE);
    }


   node* word = (node*)malloc(sizeof(node));
   word->next = NULL;
   node* p = word;
   while((ch = fgetc(fp1)) != EOF) {
        p->ch = ch;
        if(isspace(ch)) {
            print_word(fp2, word);
            putc(ch, fp2);
            node* new_word = (node*)malloc(sizeof(node));
            new_word->next = NULL;
            word = new_word;
            p = word;
        } else {
            node* new_char = (node*)malloc(sizeof(node));
            new_char->next = NULL;
            p->next = new_char;
            p = p->next;
        }

    }

    fclose(fp1);
    fclose(fp2);
    return 0;
}
