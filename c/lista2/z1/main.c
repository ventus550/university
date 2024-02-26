#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>



int F(int n, int k) {
    int rec(int n, int k, int isFirst) {
        if(n == 0)
            if(k == 0)
                return 1;
            else
                return 0;
        else {
            int sum = 0;
            for(int i = isFirst; i < 10; i++)
                sum += rec(n-1, k-i, 0);
            return sum;
        }
    }

    return rec(n,k,1);
}

int FMem(int n, int k) {
     int mem[n+1][k+1];
     for(int i = 0; i < n+1; i++)
        for(int j = 0; j < k+1; j++)
            mem[i][j] = -1;

    int rec(int n, int k, int isFirst) {
        if(k < 0)
            return 0;
        if(mem[n][k] != -1) {
            return mem[n][k];
        }

        if(n == 0)
            if(k == 0)
                return 1;
            else
                return 0;
        else {
            int sum = 0;
            for(int i = isFirst; i < 10; i++)
                sum += rec(n-1, k-i, 0);
            return sum % ((int)pow(10,9.0) + 7);
        }
    }
    rec(n, k, 1);
}

int isvalid(char* str, int N, int K) {
    int sum = 0;
    for(int i = 0; i < N; i++)
        sum += str[i] - '0';

    if(sum == K)
        return 1;
    return 0;
}

void FGen(int N, int K) {
    int mem[N+1][K+1];
     for(int i = 0; i < N+1; i++)
        for(int j = 0; j < K+1; j++)
            mem[i][j] = -1;

    int rec(int n, int k, int isFirst, char* num) {
        if(k < 0)
            return 0;
        if(mem[n][k] != -1) {
            return mem[n][k];
        }

        if(n == 0)
            if(k == 0) {
                for(int i = 0; i < N; i++)
                    printf("%c", num[N - i - 1]);
                printf("\n");
                assert(isvalid(num, N, K));
                return 1;
            }

            else
                return 0;
        else {
            int sum = 0;
            for(int i = isFirst; i < 10; i++) {
                num[n-1] = '0' + i;
                sum += rec(n-1, k-i, 0, num);
            }

            return sum % ((int)pow(10,9.0) + 7);
        }
    }
    char t[N];
    rec(N, K, 1, t);
}


int main()
{

    //printf("%d\n", FMem(2,10));
    FGen(4, 10);

    return 0;
}
