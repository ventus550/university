#include "apue.h"
#include <fcntl.h>

#define BUFFSIZE 4096

int main(int argc, char **argv) {
  int n;
  char buf[BUFFSIZE];


  int file = open(argv[1], O_RDONLY, 0);
  while ((n = read(file, buf, BUFFSIZE)) > 0)
    if (write(STDOUT_FILENO, buf, n) != n)
      err_sys("write error");

  if (n < 0)
    err_sys("read error");
   
  close(file);

  exit(0);
}
