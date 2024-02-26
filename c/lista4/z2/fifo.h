#ifndef FIFO_H_INCLUDED
#define FIFO_H_INCLUDED

typedef struct {

    int data_type;

    size_t allocated_size;
    void* data;
    struct node* next_node;

} node;

node* push(node*, int);
node* pop(node*);

#endif // FIFO_H_INCLUDED
