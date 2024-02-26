#include <stdio.h>
#include <stdlib.h>

typedef struct item{
    int val;
    struct item *next;
    struct item *prev;
} Item;

typedef struct list {
    Item *head;
    Item *tail;
} List;

void insert(List* ls, int val) {
    Item* new_Item = (Item*)malloc(sizeof(Item));
    new_Item->val = val;
    new_Item->next = NULL;
    new_Item->prev = NULL;
    if(ls->head == NULL) {
        ls->head = new_Item;
        ls->tail = new_Item;
    } else {
        new_Item->next = ls->head;
        ls->head->prev = new_Item;
        ls->head = new_Item;
    }
}

void append(List* ls, int val) {
    Item* new_Item = (Item*)malloc(sizeof(Item));
    new_Item->val = val;
    new_Item->next = NULL;
    new_Item->prev = NULL;
    if(ls->head == NULL) {
        ls->head = new_Item;
        ls->tail = new_Item;
    } else {
        new_Item->prev = ls->tail;
        ls->tail->next = new_Item;
        ls->tail = new_Item;
    }
}

int remove_front(List* ls) {
    if(ls->head == NULL) {
        printf("LISTA PUSTA\n");
        return -1;
    }

    if(ls->head == ls->tail) {
        Item* tmp = ls->head;
        ls->head = NULL;
        ls->tail = NULL;
        return tmp->val;
    }

    Item* tmp = ls->head;
    ls->head = ls->head->next;
    tmp->next = NULL;
    return tmp->val;
}

int remove_back(List* ls) {
    if(ls->tail == NULL) {
        printf("LISTA PUSTA\n");
        return -1;
    }

    if(ls->head == ls->tail) {
        Item* tmp = ls->head;
        ls->head = NULL;
        ls->tail = NULL;
        return tmp->val;
    }

    Item* tmp = ls->tail;
    ls->tail = ls->tail->prev;
    tmp->prev = NULL;
    return tmp->val;
}

int pw(int n) {
    int sum = 1;
    for(int i = 0; i < n; i++) {
        sum *= 10;
    }
    return sum;
}


int main()
{
    List* Lista = (List*)malloc(sizeof(List));
    Lista->head = NULL;
    Lista->tail = NULL;

    int ops;
    scanf("%d", &ops);
    for(int i = 0; i < ops; i++) {
        char str[8];
        gets(str);
        int op = str[0] - '0';

        int k = 0;
        while(str[2 + k] <= '9' && str[2 + k] >= '0' && k < 6) {
            k++;
        }

        int a = 0;
        for(int j = 0; j < k; j++) {
            a += (int)(str[2+j] - '0') * pw(k - j - 1);
        }

        if(op == 1)
            insert(Lista, a);
        if(op == 2)
            append(Lista, a);
        if(op == 3) {
            int res = remove_front(Lista);
            if(res != -1)
                printf("Zdjeto %d\n", res);
        }
        if(op == 4) {
            int res = remove_back(Lista);
            if(res != -1)
                printf("Zdjeto %d\n", res);
        }


    }
    printf("\n Operations Limit Reached \n");
}
