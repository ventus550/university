#include <stdio.h>
#include <stdlib.h>
#include "vector.c"

#define int(x) *(int*)x

void print(vector *v) {
    printf("vector [ ");
    for(int i = 0; i < v->size; i++)
        printf("%d ", int(v->data[i]));
    printf("]\n");
}

int main() {
    int a = 1, b = 2;
    void *ptr1 = &a, *ptr2 = &b;

    vector v;
    vector_init(&v, 10, sizeof(int));

    vector_push_back(&v, ptr1);
    vector_push_back(&v, ptr1);
    vector_push_back(&v, ptr1);
    vector_push_back(&v, ptr1);
    print(&v);

    vector_assign(&v, 0, ptr2);
    print(&v);

    printf("[2]: %d, front: %d, back: %d\n", int(vector_at(&v, 2)), int(vector_front(&v, 0)), int(vector_back(&v, 0)));

    printf("popped: %d\n", int(vector_pop_back(&v)));
    print(&v);

    vector_resize(&v, 2);
    print(&v);

    vector_resize(&v, 3);
    print(&v);

    vector_push_back(&v, ptr2);
    vector cv;
    vector_copy(&cv, &v);
    print(&cv);

    vector_clear(&cv);
    print(&cv);

    printf("\nTest rozszerzalnosci \n");
    vector tv;

    vector_init(&tv, 2, sizeof(int));
    for(int i = 0; i < 10; i++) {
        vector_push_back(&tv, ptr1);
        print(&tv);
    }

    return 0;
}
