/* Jakub Skalski 314007 */

#include "socket.cpp"
#include "table.cpp"
#include <vector>


Table
routes,
directs;

const int
turn = 7,
inactivity = 4;

using namespace std;


void init(ip_t interface, mask_t mask, distance_t dist) {
	/* Inititalize table structures with the provided network interface */

	routes.include({net(interface, mask), mask, dist, DIRECT, inactivity});
	directs.include({interface, mask, dist, DIRECT, inactivity});
}


void sendvec(Socket *sock) {
	/* Attempt to broadcast vector components
	 * and deactivate routes on failure */

	for (Entry d : directs) {
		for (Entry r : routes) {
			const auto [subnet, mask, dist, via, ttl] = r;

			// Send only sensible routes
			if (net(via, mask) == net(d.net, d.mask))
				continue;

			try {
				sock->send(
					ip2str(broadcast(d.net, d.mask)),
					vec{net(subnet, mask), mask, dist}
				);
				routes.include({net(d.net, d.mask), d.mask, d.dist, d.via, inactivity});
			}

			catch (invalid_argument const&) {
				routes.include({net(d.net,d.mask), d.mask, UNREACHABLE, DIRECT, 0});
			}
		}
	}
}




void receive(Socket *sock) {
	char sender[20];
	auto [ip, mask, dist] = sock->receive(sender);

	// Ignore own messages
	ip_t senderip = str2ip(sender);
	Entry &ent = directs[senderip];
	if (ent.net == senderip)
		return;

	// Adding to infinity yields infinity
	dist = max(dist, dist + directs.dist(str2ip(sender)));

	// Reset direct ttl and attempt to include received vector component
	ent.ttl = inactivity;
	routes.include({ip, mask, dist, str2ip(sender), inactivity});
}


void manage_connections() {
	/* Set each expired connection to UNREACHABLE
	 * and restore most recently activated direct connections */

	directs.decay();
	routes.decay();
	for (Entry &r : routes) {
		if (r.dist != UNREACHABLE and r.via != DIRECT and directs[r.via].ttl == 0)
			r.dist = UNREACHABLE;
	}
}


void listen(Socket *sock, const long time) {
	/* Run send-receive loop */

	manage_connections();
	sendvec(sock);
	routes.show();

	long timeout = time * SEC;
	while ((timeout = sock->await(timeout)))
		receive(sock);
	
	listen(sock, time);
}


int main() {

	/* Read config from stdin */
	string str;
	getline(cin, str); 
	for(int i = stoi(str); i > 0; i--) {
		getline(cin, str);
		vec v = line2vec(str);
		init(v.ip, v.mask, v.dist);
	}

	/* Start broadcasting */
	Socket sock;
	listen(&sock, turn);
    return 0;
}