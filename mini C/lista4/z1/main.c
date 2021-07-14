
#include "bst.c"

int main()
{

    node* root = new_node(10);
    add(root, 5);
    add(root, 15);
    add(root, 20);
    add(root, 3);
    add(root, 7);

    printf("\n%d", find(root, 10));
    root = rem(root, 10);
    printf("\n%d", find(root, 10));

    printf("\n%d\n", height(root));
    inorder(root);

    return 0;
}
