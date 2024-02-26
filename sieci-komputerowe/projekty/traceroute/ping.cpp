/* Jakub Skalski 314007 */

#include "traceroute.h"

u_int16_t compute_icmp_checksum (const void *buff, int length) {
	u_int32_t sum;
	const u_int16_t* ptr = (u_int16_t*)buff;
	assert (length % 2 == 0);
	for (sum = 0; length > 0; length -= 2)
		sum += *ptr++;
	sum = (sum >> 16) + (sum & 0xffff);
	return (u_int16_t)(~(sum + (sum >> 16)));
}

void ping(int sockfd, int ttl, int seq, sockaddr_in &address) {
	/* Send a single ICMP echo packet. */
	struct icmp packet;
	packet.icmp_type = ICMP_ECHO;
	packet.icmp_code = 0;
	packet.icmp_id = htons(getpid());

	/* Make packets unique so that they are not dropped. */
	packet.icmp_seq = 100*seq + ttl;
	
	packet.icmp_cksum = 0;
	packet.icmp_cksum = compute_icmp_checksum(&packet, sizeof(packet));

	setsockopt(sockfd, IPPROTO_IP, IP_TTL, &ttl, sizeof(ttl));
	
	check(	
		sendto(sockfd,
			&packet, sizeof(packet), 
			0,
			(struct sockaddr*)&address, sizeof(address)),
		"sendto error: "
	);
}