#include "FIFO.h"

node* pop(node* ls) {
    node* p;
    while (ls->next_node != NULL) {
        p = ls;
        ls = ls->next_node;
    }

    printf("\nRemoved: ");
    print(p);
    p->next_node = NULL;
    free(p->data);

    getch();
    MainMenu();
}

node* push(node* ls, int type) {

    node* new_item = (node*)malloc(sizeof(node));
    new_item->data_type = type;
    new_item->next_node = ls;
    system("cls");

    if(type == 1) {
        new_item->data = (char*)malloc(sizeof(char)*100);
        scanf ("%100s", new_item->data);
    }

    if(type == 2)
        scanf("%d", &new_item->data);

    if(type == 3) {
        new_item->data = (float*)malloc(sizeof(float));
        scanf("%f", new_item->data);
    }

    if(type == 4) {
        //mozna bylo od razu ale w poleceniu jest mowa o kopiowaniu tablic,
        //poniewaz w mojej implementacji wszystko dzieje sie przez konsole
        //zostawiam to jako przyklad tego jakbym sobie poradzil z pushowaniem obiektow o zaalokowanej wczesniej pamieci
        scanf("%d", &new_item->allocated_size);
        int *array = (int*)malloc(sizeof(int)*new_item->allocated_size);

        new_item->data = (int*)malloc(sizeof(int)*new_item->allocated_size);
        for(int i = 0; i < new_item->allocated_size; i++){
            array[i] = i;
        }
        memcpy(new_item->data, array, sizeof(int)* new_item->allocated_size);
        free(array);
    }


    return new_item;
}
