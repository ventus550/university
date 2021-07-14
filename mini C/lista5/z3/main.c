    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    typedef struct node{
        int occurances;
        char *str;
        struct node* next;
    } node;


    int compare(const void* a, const void* b)
    {
        return strcmp(*(const char**)a, *(const char**)b);
    }

    int main() {
        int n;
        scanf("%d", &n);
        if(n == 0)
            return 0;
        char *word[n];

        for (int i = 0; i < n; i++) {
            word[i] = malloc(20 * sizeof(char));
            scanf("%20s", word[i]);
        }
        qsort(word, n, sizeof(const char*), compare);

        node* res = (node*)malloc(sizeof(node));
        res->occurances = 0;
        res->str = word[0];
        node *p = res;
        for (int i = 0; i < n; i++) {
            if(strcmp(p->str, word[i]) == 0)
                p->occurances += 1;
            else {
                node* item = (node*)malloc(sizeof(node));
                item->occurances = 1;
                item->str = word[i];
                p->next = item;
                p = item;
            }
        }
        p = res;
        while(p != NULL) {
            printf("%s %d\n", p->str, p->occurances);
            p = p->next;
        }



        return 0;
    }
