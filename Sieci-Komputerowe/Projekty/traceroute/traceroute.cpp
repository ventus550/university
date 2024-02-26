/* Jakub Skalski 314007 */

#include "traceroute.h"


using namespace std;


void check(int outcome, std::string msg) {
	if (outcome < 0) {
		std::cerr << msg << strerror(errno) << std::endl;
		exit(EXIT_FAILURE);
	}
}


struct sockaddr_in address(const char *straddr) {
	/* Validate and wrap input address. */
	struct sockaddr_in recipient;
	bzero(&recipient, sizeof(recipient));
	recipient.sin_family = AF_INET;
	if(inet_pton(AF_INET, straddr, &recipient.sin_addr) == 0) {
		cerr << "Invalid IP address!" << endl;
		exit(EXIT_FAILURE);
	}
	return recipient;
}


int main(int argc, char* argv[]) {

	if (argc != 2) {
		cout << "Expected exactly one command line argument!" << endl;
		exit(EXIT_FAILURE);
	}
	
	struct sockaddr_in addr = address(argv[1]);

	int sockfd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
	check(sockfd, "socket error: ");


	for (int i = 1; i <= 30; i++) {

		// unleash the pings!
		for (int j = 0; j < 3; j++)
			ping(sockfd, i, j, addr);
		
		// count down in microseconds
		int timeout = 1000000; 
		
		// number of packets yet to return
		int remaining = 3;
		
		// accumulated times of packets' arrivals
		int acc = 0;

		// ip string of the last received packet
		char previous_sender[20] = "*";

		cout << i << ". ";
		while (remaining && (timeout = await(sockfd, timeout))) {
			char sender_ip_str[20];
			if (receive(sockfd, i, sender_ip_str)) {
				remaining--;
				acc += timeout;
				if (strcmp(sender_ip_str, previous_sender)) {
					strcpy(previous_sender, sender_ip_str);
					cout << previous_sender << " ";
				}
			}
		}

		switch(remaining) {
			case 0:
				cout << (3000000 - acc) / 3000 << "ms" << endl;
				break;
			case 3:
				cout << "*" << endl;
				break;
			default:
				cout << "???" << endl;
		}

		if (!strcmp(argv[1], previous_sender))
			break;
		
	}
	return EXIT_SUCCESS;
}