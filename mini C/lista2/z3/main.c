#include <stdio.h>
#include <stdlib.h>

void print(int side, int arr[side][side])
{
    printf("Checking...\n");
    int i, j;
    for (i = 0; i < side; i++) {
        for (j = 0; j < side; j++)
            printf("%d ", arr[i][j]);
        printf("\n");
    }


}


int hetmani(int n) {

    void copy2(int arr[n][n],int *b)
    {
        print(n,arr);
        /*int i;
        for(i=0; i<n; i++)
        {
            b[i]=arr[i][i];
        }*/
    }



    int q(int x, int y, int tab[n][n]) {
        printf("\n\nRecToPos: %d %d %d\n", x, y, tab[x][y]);
        print(n, tab);
        if(x != -1 && tab[x][y] != 0) {
            return 0;
        }

        if(x == n-1)
            return 1;

        int sum = 0;
        for(int i = 0; i < n; i++) {
            int tmp[n][n];
            copy2(tab[0], tmp[0]);

            print(n, tmp);

            int k = 1;
            while(x+k < n) {

                if(y+k < n)
                    tmp[x+k][y+k] = 2;
                if(y-k >= 0)
                    tmp[x+k][y-k] = 3;
                tmp[x+1][y+k] = 4;
                k++;
            }
            sum += q(x+1, i, tmp);
        }
        return sum;
    }

    int tb[n][n];
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            tb[i][j] = 0;

    return q(-1, -1, tb);
}




int main()
{
    printf("%d", hetmani(4));
    return 0;
}
