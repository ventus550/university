#include <stdio.h>
#include <stdlib.h>

#include "bst.h"

node* new_node(int val) {
    node* new_node = (node*)malloc(sizeof(node));
    new_node->left = NULL;
    new_node->right = NULL;
    new_node->value = val;

    return new_node;
}


void addNode(node* r, node* source) {
    if(source == NULL)
        return;

    node* p = r;

    while(1) {
        if(source->value <= p->value)
            if(p->left == NULL) {
                p->left = source;
                break;
            }
            else
                p = p->left;
        else
            if(p->right == NULL) {
                p->right = source;
                break;
            }
            else
                p = p->right;
    }
}

node* add(node *r, int val) {
    if(r == NULL)
        return new_node(val);
    addNode(r, new_node(val));
}

int find(node* r, int val) {
    node* p = r;

    while(p != NULL) {

        if(val == p->value)
            return 1;

        if(val < p->value)
            p = p->left;

        if(val > p->value)
            p = p->right;
    }

    return 0;
}

node* rem(node* r, int val) {
    if(find(r, val) == 0)
        return r;

    if(r->value == val) {
        if(r->right != NULL)
            addNode(r->right, r->left);
        if(r->right == NULL && r->left == NULL) {
            free(r);
            return NULL;
        }
        return r->right;
    }

    void replace(node* r) {

        if(r->left->value == val) {
            node* left = r->left->left;
            node* right = r->left->right;
            free(r->left);
            r->left = NULL;
            addNode(r, right);
            addNode(r, left);
            return;
        }

        if(r->right->value == val) {
            node* left = r->right->left;
            node* right = r->right->right;
            free(r->right);
            r->right = NULL;
            addNode(r, right);
            addNode(r, left);
            return;
        }

        if(val < r->value)
            replace(r->left);
        else
            replace(r->right);
    }

    replace(r);
    return r;
}

int height(node* r) {
    int max(int n, int m) {
        if(n > m)
            return n;
        return m;
    }

    int hrec(node* n, int h) {
        if(n == NULL)
            return h;
        return max(hrec(n->left, h + 1), hrec(n->right, h + 1));
    }

    return hrec(r, 0);
}

void inorder(node* r) {
    printf("inorder print:\n");

    void rec(node* n) {
        if(n == NULL)
            return;
        rec(n->left);
        printf("%d ", n->value);
        rec(n->right);
    }

    rec(r);
    printf("\n");


}
