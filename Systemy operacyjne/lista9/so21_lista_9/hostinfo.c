// struct addrinfo {
//     int ai_flags;
//     int ai_family;
//     int ai_socktype;
//     int ai_protocol;
//     socklen_t ai_addrlen;
//     struct sockaddr *ai_addr;
//     char *ai_canonname;
//     struct addrinfo *ai_next;
// };

#include "csapp.h"

int main(int argc, char **argv) {
  struct addrinfo *p, *listp, hints;
  char buf[MAXLINE];
  char puf[MAXLINE];
  int rc, flags;

  if (argc != 2 && argc != 3)
    app_error("usage: %s <domain name>\n", argv[0]);

  /* Get a list of addrinfo records */
  memset(&hints, 0, sizeof(struct addrinfo));

  //- hints.ai_family = AF_INET; /* IPv4 only */
  hints.ai_family = AF_UNSPEC;   /* IPv4 + IPv6 */
  
  /* SOCK_DGRAM jeśli marzy nam się obsługiwać tylko UDP
  lub możemy pozostawić to pole niewypełnione co oznacza obsługę dowolnego typu gniazda */
  hints.ai_socktype = SOCK_STREAM; 

  /* Connections only */
  //- if ((rc = getaddrinfo(argv[1], NULL, &hints, &listp)) != 0)
  char *service = argc == 3 ? argv[2] : NULL;
  if ((rc = getaddrinfo(argv[1], service, &hints, &listp)) != 0)
    gai_error(rc, "getaddrinfo");

  /* Walk the list and display each IP address */
  flags = NI_NUMERICHOST;  /* Display address string instead of domain name */
  flags |= NI_NUMERICSERV; /* Display service string instead of service name */
  for (p = listp; p; p = p->ai_next) {
    Getnameinfo(p->ai_addr, p->ai_addrlen, buf, MAXLINE, puf, MAXLINE, flags);

    if (p->ai_family == AF_INET)
      printf("%s", buf);
    else
      printf("[%s]", buf);
    
    if (service != NULL)
      printf(":%s", puf);
    
    printf("\n");
    
  }

  /* Clean up */
  freeaddrinfo(listp);

  return EXIT_SUCCESS;
}
