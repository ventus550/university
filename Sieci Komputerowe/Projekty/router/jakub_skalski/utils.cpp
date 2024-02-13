/* Jakub Skalski 314007 */

#pragma once
#include "router.h"


std::string ip2str(ip_t ip) {
	ip = htonl(ip);
	char sender_ip_str[20];
	struct in_addr sin_addr = {ip};
	inet_ntop(AF_INET, &sin_addr, sender_ip_str, sizeof(sender_ip_str));
	return std::string(sender_ip_str);
}

ip_t str2ip(std::string ip) {
	struct in_addr sin_addr;
	inet_pton(AF_INET, &ip[0], &sin_addr);
	return ntohl(sin_addr.s_addr);
}

ip_t broadcast(ip_t ip, mask_t mask) {
	/* Get broadcast address */
	return ip | (0xFFFFFFFF >> mask);
}

ip_t net(ip_t ip, mask_t mask) {
	/* Get subnet ip */
	mask_t len = 32;
	return (ip >> (len-mask)) << (len-mask);
}

vec line2vec(std::string str) {
	/* Convert line string to vector component */
	unsigned sep = str.find('/');
	str[sep] = ' ';

	sep = 0;
	std::string words[4];
	for (int i = 0; i < 4; i++) {
		words[i] = str.substr(sep, str.find(' ', sep) - sep);
		sep += words[i].length() + 1;
	}

	return vec{str2ip(words[0]), (mask_t)stoi(words[1]), (distance_t)stoi(words[3])};
}

