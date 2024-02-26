#ifndef VECTOR_H_INCLUDED
#define VECTOR_H_INCLUDED


typedef struct vector {
    size_t size;
    size_t capacity;
    size_t element_size;
    void** data;
} vector;


void vector_init(vector* v, size_t capacity, size_t element_size);
void vector_copy(vector* destination, vector* source);
void vector_assign(vector *v, int i, void* elem);
void* vector_at(vector *v, int i);
void* vector_front(vector *v, int i); //nie rozumiem dlaczego przekazujemy tutaj indeks..
void* vector_back(vector *v, int i); //tak samo tutaj :/
void vector_push_back(vector* v, void* elem);
void* vector_pop_back(vector* v);
void vector_clear(vector* v);
void vector_resize(vector* v, int n);
void vector_reserve(vector* v, int n);
size_t vector_size(vector* v);
size_t vector_capacity(vector* v);
int vector_empty(vector* v);

#endif // VECTOR_H_INCLUDED
