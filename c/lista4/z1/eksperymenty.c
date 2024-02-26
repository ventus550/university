#include "bst.c"

int main()
{
    node* root = new_node(10);

    time_t t;
    srand((unsigned) time(&t));
    for(int i = 0 ; i < 106 ; i++ ) {
        add(root, rand() % 50);
    }


    printf("\n%d\n", height(root));
    inorder(root);

    return 0;
}
