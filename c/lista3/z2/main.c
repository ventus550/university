#include <stdio.h>
#include <stdlib.h>

#define LOG(x) printf("%c\n", x);


int length(char *string) {
    int k = 0;
    while(*(string + k) != '\0')
        k++;

    return k;
}

char *strncat (char *destination, const char *source, size_t num) {

    char *p = destination + length(destination);
    for(int i = 0; i < num; i++) {
        //!printf("%c", *(destination+i));
        *(p + i) = *(source + i);
    }
    return destination;
}

char * strcat (char *destination, const char *source) {
    return strncat(destination, source, length(source));
}

int min(int a, int b) {
    if(a < b)
        return a;
    return b;
}

int strncmp (const char *str1, const char *str2, size_t num) {
    int l1 = length(str1),
        l2 = length(str2);

    if(l1 != l2 && min(l1, l2) < num) {
        return 0;
    }

    int i = 0;
    while(i < num && *(str1 + i) != '\0') {
        if(*(str1 + i) != *(str2 + i))
            return 0;
        i++;
    }
    return 1;
}

int strcmp (const char * str1, const char * str2) {
    int l1 = length(str1),
        l2 = length(str2);

    if(l1 != l2)
        return 0;
    return strncmp(str1, str2, l1);
}


int main()
{
    char napis1[31] = "Nietoperz";
    char *napis2 = "Pelikan";

    printf("%d\n", length(napis1));
    printf("%d\n", length(napis2));

    printf("%s\n", strncat(napis1, napis2, 5));
    strcat(napis1, napis2);
    printf("%s\n", napis1);
    strcat(napis1, napis2);
    printf("%s\n", napis1);


    char napis3[10] = "alac";
    printf("%d\n", strncmp(napis3, "alad", 3));
    printf("%d\n", strcmp(napis3, "alad"));


    return 0;
}
