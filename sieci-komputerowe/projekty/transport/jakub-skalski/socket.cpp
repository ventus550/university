/* Jakub Skalski 314007 */

#include "transport.h"

#define SEC 1000000

int check(int outcome) {
	if (outcome >= 0)
		return outcome;
	throw std::invalid_argument(strerror(errno));
}


struct sockaddr_in validate(const char *straddr) {
	/* Validate and wrap input address. */
	struct sockaddr_in recipient;
	bzero(&recipient, sizeof(recipient));
	recipient.sin_family = AF_INET;
	if(inet_pton(AF_INET, straddr, &recipient.sin_addr) == 0) {
		std::cerr << "Invalid IP address!" << std::endl;
		exit(EXIT_FAILURE);
	}
	return recipient;
}


struct sockaddr_in address(unsigned int port) {
	struct sockaddr_in addr;
	bzero (&addr, sizeof(addr));
	addr.sin_family	= AF_INET;
	addr.sin_port	= htons(port);
	return addr;
}


class Socket {
	const int sockfd;
	const unsigned int port;

	public:
	Socket(unsigned int port = 54321) : sockfd(check(socket(AF_INET, SOCK_DGRAM, 0))), port(port) {
		struct sockaddr_in server_address = address(port);
		server_address.sin_addr.s_addr = htonl(INADDR_ANY);
		check( (bind (sockfd, (struct sockaddr*)&server_address, sizeof(server_address))));

		/* Enable broadcast */
		int broadcastPermission = 1;
		setsockopt(sockfd, SOL_SOCKET, SO_BROADCAST, (void*)&broadcastPermission, sizeof(broadcastPermission));
	}


	int send(str ip, str message, unsigned int target_port = 0) {
		return this->send(ip, &message[0], target_port);
	}


	int send(str ip, const char message[], unsigned int target_port = 0) {
		target_port = target_port ? target_port : port;
		struct sockaddr_in server_address = address(target_port);
		inet_pton(AF_INET, &ip[0], &server_address.sin_addr);

		ssize_t message_len = strlen((char *)message);
		int sent_len = sendto(sockfd, message, message_len, 0, (struct sockaddr*) &server_address, sizeof(server_address));
		return check(sent_len - message_len);
	}


	num receive(char buffer[IP_MAXPACKET+1], char sender_ip[20] = nullptr) {
		struct sockaddr_in 	sender;	
		socklen_t 			sender_len = sizeof(sender);

		check(recvfrom (sockfd, buffer, IP_MAXPACKET, 0, (struct sockaddr*)&sender, &sender_len));

		if (sender_ip)
			inet_ntop(AF_INET, &sender.sin_addr, sender_ip, 20);

		return ntohs(sender.sin_port);
	}


	double await(double seconds = 1.0) {
		/* Wait for timeout or for the sockfd to become ready and return time elapsed */
		long micro = this->microwait((long)(seconds * SEC));
		return (double)micro / SEC;
	}


	unsigned microwait(long microseconds) {
		fd_set descriptors;
		FD_ZERO (&descriptors);
		FD_SET (sockfd, &descriptors);
		struct timeval timeout = {microseconds / SEC, microseconds % SEC};
		check(select(sockfd+1, &descriptors, NULL, NULL, &timeout));
		return SEC * timeout.tv_sec + timeout.tv_usec;
	}


	~Socket() {
		close(sockfd);
	}
};