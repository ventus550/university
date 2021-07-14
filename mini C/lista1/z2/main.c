#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

typedef struct {

    int type;

    char napis[100];
    int liczba;
    int para[2];
    double zmnp;

    struct FIFO *next;
} FIFO;

FIFO* list;


FIFO* pop(FIFO* ls) {
    FIFO* p;
    while (ls->next != NULL) {
        p = ls;
        ls = ls->next;
    }

    p->next = NULL;
    printf("\nRemoved: ");
    print(p);

    getch();
    MainMenu();


}

FIFO* push(int type) {

    FIFO* new_item = (FIFO*)malloc(sizeof(FIFO));
    new_item->type = type;
    new_item->next = list;
    system("cls");

    if(type == 1) {
        for(int i = 0; i < 100; i++) {
            new_item->napis[i] = 0;
        }
        scanf ("%99s", new_item->napis);
    }

    if(type == 2)
        scanf("%d", &new_item->liczba);

    if(type == 3) {
        scanf("%d", &new_item->para[0]);
        scanf("%d", &new_item->para[1]);
    }

    if(type == 4)
        scanf("%lf", &new_item->zmnp);


    return new_item;
}

void MainMenu() {
    system("cls");
    printf("Choose an operation by typing the corresponding number. \n");
    printf("1) Add value to the list \n");
    printf("2) Remove the earliest value added to the list\n");
    printf("3) Print the list\n");

    int num = getch() - '0';

    if(num == 1)
        sub_menu_add();
    if(num == 2)
        pop(list);
    if(num == 3)
        print_each(list);
    if(num > 3)
        MainMenu();
}

void sub_menu_add() {
    system("cls");
    printf("Choose an operation by typing the corresponding number. \n");
    printf("1) Append a String \n");
    printf("2) Append an Integer \n");
    printf("3) Append a Pair \n");
    printf("4) Append a Float \n");

    int num = getch() - '0';
    list = push(num);

    MainMenu();
}





void print_each(FIFO* ls) {
    system("cls");
    while (ls->next != NULL) {
        print(ls);
        printf("\n");
        ls = ls->next;
    }
    getch();
    MainMenu();
}

void print(FIFO* elem) {
    if(elem->type == 1)
        for(int i = 0; i < 100; i++)
            printf("%c", elem->napis[i]);
    if(elem->type == 2)
        printf("%d", elem->liczba);
    if(elem->type == 3)
        printf("<%d,%d>", elem->para[0], elem->para[1]);
    if(elem->type == 4)
        printf("%lf", elem->zmnp);
}

int main()
{
    list = (FIFO*)malloc(sizeof(FIFO));
    list->next = NULL;

    MainMenu();

    return 0;
}
