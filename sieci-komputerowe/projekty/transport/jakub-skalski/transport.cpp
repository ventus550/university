/* Jakub Skalski 314007 */

#include "socket.cpp" 
#include "window.cpp" 
using namespace std;


num
port,
readlen;

str
ip,
filename;


str get(num start, num len) {
	return "GET " + to_string(start) + " " + to_string(len) + "\n";
}


num data2order(char data[]) {
	str string = str(data);

	num
	begin = 5,
	end = string.find(' ', begin);
	return stoi(string.substr(begin, end));
}


char* data2bytes(char data[]) {
	str string = str(data);
	return data + string.find('\n') + 1;
}


void manage_timers(Socket *sock, Window *wind) {
	for (Entry &ent : *wind) {
		if (ent.status == WAITING and not (ent.timer = max((num)1, ent.timer) - 1)) {
			sock->send(ip, get(ent.order, SEGSIZE), port);
			ent.timer = PATIENCE;
		}
	}
}


void shiftwrite(ofstream *of, Window *wind) {
	if (readlen == 0)
		return;

	try {
		Entry pop = wind->shift();
		num len = min(SEGSIZE, readlen);
		of->write(pop.bytes, len);
		readlen -= len;
	}

	catch (logic_error const &) {return;}
	shiftwrite(of, wind);
}


void receive(Socket *sock, Window *wind) {
	char data[IP_MAXPACKET+1];
	if(port != sock->receive(data))
		return;
	
	num order = data2order(data);
	num floor = wind->front().order;
	if (order < floor)
		return;

	char* bytes = data2bytes(data);
	num idx = (order - floor) / SEGSIZE;
	Entry *ent = &(*wind)[idx];
	ent->status = RECEIVED;
	memcpy(ent->bytes, bytes, SEGSIZE);
}


void download(Socket *sock, Window *wind, ofstream *of) {
	/* Run send-receive loop */
	manage_timers(sock, wind);

	double timeout = TIME;
	while ((timeout = sock->await(timeout))) {
		receive(sock, wind);
		debug(wind->show();)
		shiftwrite(of, wind);
	}
	
	if (readlen > 0)
		download(sock, wind, of);
}


int main(int argc, char **argv) {

	try {
		if (argc != 5) throw invalid_argument("");
		ip = argv[1];
		port = stoi(argv[2]);
		filename = argv[3];
		readlen = stoi(argv[4]);
		validate(&ip[0]);
	}
	
	catch (...) {
		cerr << "Invalid input!" << endl;
		exit(EXIT_FAILURE);
	}


	Socket 		sock;
	Window 		wind;
	ofstream 	of(filename);

	download(&sock, &wind, &of);
	return EXIT_SUCCESS;
}