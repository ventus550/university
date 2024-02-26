#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

#include "FIFO.c"


#define float(x) *(float*)x


node* list;

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
    printf("3) Append a Float \n");
    printf("4) Append an Array (0...n)\n");

    int num = getch() - '0';
    list = push(list, num);

    MainMenu();
}

void print_each(node* ls) {
    system("cls");
    while (ls->next_node != NULL) {
        print(ls);
        printf("\n");
        ls = ls->next_node;
    }
    getch();
    MainMenu();
}

void print(node* elem) {
    if(elem->data_type == 1)
        printf("%s", (char*)elem->data);
    if(elem->data_type == 2)
        printf("%d", elem->data);
    if(elem->data_type == 3)
        printf("%f", float(elem->data));
    if(elem->data_type == 4) {
        int *arr;
        for(int i = 0; i < elem->allocated_size; i++)
            printf("%d", ((int*)elem->data)[i]);
    }

}

int main()
{
    list = (node*)malloc(sizeof(node));
    list->next_node = NULL;

    MainMenu();

    return 0;
}
