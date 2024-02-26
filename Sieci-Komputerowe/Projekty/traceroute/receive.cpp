/* Jakub Skalski 314007 */

#include "traceroute.h"


int await(int sockfd, unsigned microsecs) {
	/* Wait for timeout or for the sockfd to become ready and return time elapsed. */
	fd_set descriptors;
    FD_ZERO (&descriptors);
    FD_SET (sockfd, &descriptors);
	struct timeval timeout = {0, microsecs};
	int outcome = select(sockfd+1, &descriptors, NULL, NULL, &timeout);
	check(outcome, "select error: ");
	return timeout.tv_usec;
}


bool receive(int sockfd, int ttl, char sender_ip_str[]) {
	/* Attempt to retrieve ip string of sender. Return 1 if succesful and 0 otherwise. */
	struct sockaddr_in 	sender;	
	socklen_t 			sender_len = sizeof(sender);
	u_int8_t 			buffer[IP_MAXPACKET];

	ssize_t packet_len = recvfrom (sockfd, buffer, IP_MAXPACKET, MSG_DONTWAIT, (struct sockaddr*)&sender, &sender_len);
	check(packet_len, "recvfrom error: ");
	
	struct ip* 			ip_header = (struct ip*) buffer;
	struct icmp*		ip_icmp = (struct icmp *)((uint8_t *)ip_header + 4 * ip_header->ip_hl);

	inet_ntop(AF_INET, &sender.sin_addr, sender_ip_str, 20);

	if(ip_icmp->icmp_type == ICMP_TIME_EXCEEDED){
		ip_header = (struct ip *)((uint8_t *)ip_icmp + sizeof(struct icmphdr));
		ip_icmp = (struct icmp *)((uint8_t *)ip_header + ip_header->ip_hl * 4);
		return ip_icmp->icmp_seq % 100 == ttl && ip_icmp->icmp_id == htons(getpid());
	}

	if(ip_icmp->icmp_type == ICMP_ECHOREPLY) {	
		return ip_icmp->icmp_seq % 100 == ttl && ip_icmp->icmp_id == htons(getpid());
	}

	return 0;
}