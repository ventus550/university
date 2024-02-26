#ifndef traceroute_h
#define traceroute_h


#include <iostream>
#include <netinet/ip.h>
#include <netinet/ip_icmp.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <cassert>
#include <unistd.h>
#include <chrono>


void check(int outcome, std::string msg);
void ping(int sockfd, int ttl, int seq, sockaddr_in &address);
int await(int sockfd, unsigned microsecs);
bool receive(int sockfd, int ttl, char sender_ip_str[]);

#endif