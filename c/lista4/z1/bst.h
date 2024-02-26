#ifndef BST_H_INCLUDED
#define BST_H_INCLUDED

typedef struct node{
    int value;
    struct node* left;
    struct node* right;
} node;


node* new_node(int val);


void addNode(node* r, node* source);

node* add(node *r, int val);

int find(node* r, int val);

node* rem(node* r, int val);
int height(node* r);

void inorder(node* r);


#endif // BST_H_INCLUDED
