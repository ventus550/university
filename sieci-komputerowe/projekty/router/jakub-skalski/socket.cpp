/* Jakub Skalski 314007 */

#include "utils.cpp"

#define SEC 1000000

int check(int outcome) {
	if (outcome >= 0)
		return outcome;
	throw std::invalid_argument(strerror(errno));
}

struct sockaddr_in address(unsigned int port) {
	struct sockaddr_in addr;
	bzero (&addr, sizeof(addr));
	addr.sin_family	= AF_INET;
	addr.sin_port	= htons(port);
	return addr;
}

void* serialize(void *buf, vec *v) {
	memcpy(buf, v, sizeof(vec));
	return buf;
}

vec deserialize(void *buf) {
	return *(vec *)buf;
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

	int send(std::string ip, vec v) {
		struct sockaddr_in server_address = address(port);
		inet_pton(AF_INET, &ip[0], &server_address.sin_addr);

		char buf[sizeof(vec)];
		ssize_t message_len = sizeof(vec);
		int sent_len = sendto(sockfd, serialize(buf, &v), message_len, 0, (struct sockaddr*) &server_address, sizeof(server_address));
		//debug(std::cout << "Sent to " << ip << " (" << sent_len << ")\n";)
		return check(sent_len - message_len);
	}


	vec receive(char sender_ip_str[20]) {
		struct sockaddr_in 	sender;	
		socklen_t 			sender_len = sizeof(sender);
		u_int8_t 			buffer[IP_MAXPACKET+1];

		check(recvfrom (sockfd, buffer, IP_MAXPACKET, 0, (struct sockaddr*)&sender, &sender_len));
		inet_ntop(AF_INET, &sender.sin_addr, sender_ip_str, 20);
		vec v = deserialize(buffer);

		// debug(
		// 	std::cout << "Received {" << ip2str(v.ip) << ", " << (ip_t)v.mask << ", " << v.dist << "} from " << sender_ip_str << std::endl;
		// 	fflush(stdout);
		// )

		return v;
	}


	unsigned await(long microseconds) {
		/* Wait for timeout or for the sockfd to become ready and return time elapsed */
		fd_set descriptors;
		FD_ZERO (&descriptors);
		FD_SET (sockfd, &descriptors);
		struct timeval timeout = {microseconds / SEC, microseconds % SEC};
		check(select(sockfd+1, &descriptors, NULL, NULL, &timeout));
		return SEC * timeout.tv_sec + timeout.tv_usec;
	}


	void listen() {
		char sender_ip_str[20];
		for (;;) {
			this->receive(sender_ip_str);
		}
	}


	~Socket() {
		close(sockfd);
	}
};

bool isup(std::string interface) {
	Socket sock{55555};
	try { sock.send(interface, {0,0,0}); }
	catch (std::invalid_argument const&) { return false; }
	return true;
}