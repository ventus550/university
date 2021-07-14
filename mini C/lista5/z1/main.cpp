#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node{
        char ch1, ch2;
        int k, l;
        struct node* next;
} node;


void print_line1(node* line) {
    while(line != NULL) {
        printf("%c", line->ch1);
        line = line->next;
    }
    printf("\n");
}

void print_line2(node* line) {
    while(line != NULL) {
        printf("%c", line->ch2);
        line = line->next;
    }
    printf("\n");
}

void free_line(node* line) {
    //printf("%c\n", line->ch1);
    if(line->next != NULL)
        free_line(line->next);
    free(line);

}

void compare(node* line) {
    node* p = line;

    while(p != NULL) {
        if(p->ch1 != p->ch2) {
            printf("%d %d\n", p->k, p->l);

            print_line1(line);
            print_line2(line);
            exit(1);
        }
        p = p->next;
    }
}


int main(int argc, char **argv)
{
    char ch1;
    char ch2;
    FILE *fp1;
    FILE *fp2;

    fp1 = fopen(argv[1], "r");
    fp2 = fopen(argv[2], "r");

    if (fp1 == NULL || fp2 == NULL)
    {
        perror("Error while opening the file.\n");
        exit(EXIT_FAILURE);
    }


   node* line = (node*)malloc(sizeof(node));
   line->l = 0;
   line->k = 0;
   line->next = NULL;
   node* p = line;
   while((ch1 = fgetc(fp1)) != EOF && (ch2 = fgetc(fp2)) != EOF) {
        p->ch1 = ch1;
        p->ch2 = ch2;

        if(ch1 == '\n' || ch2 == '\n') {
            compare(line);
            node* new_line = (node*)malloc(sizeof(node));
            new_line->l = line->l + 1;
            new_line->k = 0;
            new_line->next = NULL;
            free_line(line);
            line = new_line;
            p = line;
        } else {
            node* new_char = (node*)malloc(sizeof(node));
            new_char->k = p->k + 1;
            new_char->l = p->l;
            new_char->next = NULL;
            p->next = new_char;
            p = p->next;
        }

    }

    fclose(fp1);
    fclose(fp2);
    return 0;
}
