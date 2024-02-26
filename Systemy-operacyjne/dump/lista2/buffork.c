#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("foo ...");
    //fflush(stdout);
    fork();
    fork();
    fork();
}