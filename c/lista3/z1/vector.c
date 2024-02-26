#include "vector.h"


void vector_init(vector* v, size_t capacity, size_t element_size) {
    v->capacity = capacity;
    v->size = 0;
    v->element_size = element_size;
    v->data = malloc(capacity*element_size);

}
void vector_copy(vector* destination, vector* source) {
    destination->capacity = source->capacity;
    destination->element_size = source->element_size;
    destination->size = source->size;
    free(destination->data);
    destination->data = malloc(destination->capacity * destination->element_size);

    for(int i = 0; i < destination->size; i++) {
        destination->data[i] = source->data[i];
    }
}

void vector_assign(vector *v, int i, void* elem) {
    v->data[i] = elem;
}

void* vector_at(vector *v, int i) {
    return v->data[i];
}

void* vector_front(vector *v, int i) {
    return v->data[0];
}

void* vector_back(vector *v, int i) {
    return v->data[v->size-1];
}

void vector_push_back(vector* v, void* elem) {
    if(v->size == v->capacity) {
        v->data = realloc(v->data, 2*v->capacity*v->element_size);
        v->data[v->capacity] = elem;
        v->capacity = 2*v->capacity;
        v->size = v->size + 1;
    } else {
        v->data[v->size] = elem;
        v->size++;
    }
}

void* vector_pop_back(vector *v) {
    v->size--;
    return v->data[v->size];
}

void vector_clear(vector* v) {
    free(v->data);
    v->size = 0;
    v->capacity = 0;
    v->element_size = 0;
}

void vector_resize(vector* v, int n) {
    if(v->size > n)
        v->size = n;
    v->data = realloc(v->data, n*v->element_size);
}

void vector_reserve(vector* v, int n) {
    int diff = n - (v->capacity - v->size);

    if(diff > 0)
        v->data = realloc(v->data, (v->capacity + diff) * v->element_size);
}


size_t vector_size(vector* v) {
    return v->size;
}
size_t vector_capacity(vector* v) {
    return v->capacity;
}
int vector_empty(vector* v) {
    if(v->size == 0)
        return 1;
    return 0;
}
