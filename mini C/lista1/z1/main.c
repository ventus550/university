#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef int my_type;


int max(int array[], size_t arr_size) {

    assert(arr_size > 0);

    int mx = array[0];
    for(int i = 0; i < arr_size; i++) {
        if (array[i] > mx)
            mx = array[i];
    }

    return mx;
}

int max2(int array[][77], size_t side_size) {

    assert(side_size > 0);

    int mx = array[0];
    for (int i = 0; i < side_size; i++) {
        for (int j = 0; j < 77; j++) {
            if (array[i][j] > mx)
                mx = array[i][j];

        }
    }

    return mx;
}

my_type geq(my_type a, my_type b) {
    if (a > b)
        return a;
    return b;
}


my_type max3(my_type array[], size_t arr_size) {

    assert(arr_size > 0);

    if (arr_size == 0)
        return -1;

    my_type mx = array[0];
    for(int i = 0; i < arr_size; i++) {
        mx = geq(array[i], mx);
    }

    return mx;
}


int main()
{
    int A[] = {1,2,3,4,5,6,7,8,9,0};
    my_type B[] = {1,2,3,4,5,6,7,8,9,0};

    printf("%d", max3(B, 10);




    return 0;
}
