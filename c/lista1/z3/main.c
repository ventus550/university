#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, m;
    char str1[1000000] = "";
    char str2[1000000] = "";

    scanf("%d %s", &n, str1);
    scanf("%d %s", &m, str2);

    int max;
    if(n > m)
        max = n;
    else
        max = m;

    for(int i = 0; i < max; i++) {
        if(str1[i] < str2[i]) {
            printf("%s", str1);
            return;
        }
        if(str1[i] > str2[i]) {
            printf("%s", str2);
            return;
        }
    }
    printf("%s", str1);


    return 0;
}
