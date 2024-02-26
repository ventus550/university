/* Jakub Skalski 314007 */

#include "transport.h"
#include <deque>

#define RECEIVED 1
#define WAITING 0

class Entry {
	public:
	num order;
	num timer;
	num status;
	char bytes[SEGSIZE + 1]; 
};


class Window : public std::deque<Entry> {
	str entry2str(Entry ent) {
		if (ent.status == RECEIVED)
			return "\033[1;36m" + std::to_string(ent.order) + "\033[0m";
		return std::to_string(ent.order);
	}


	public:
	Window() : std::deque<Entry>() {
		for (num i = 0; i < WINSIZE; i++)
			this->push_back({i * SEGSIZE, 1, WAITING, ""});
	}


	Entry shift() {
		if (this->front().status == WAITING)
			throw std::logic_error("");

		Entry ent = this->front();
		this->push_back({this->back().order + SEGSIZE, PATIENCE, WAITING, ""});
		this->pop_front();
		return ent;
	}


	void show() {
		fflush(stdout);
		std::cout << "[ ";
		for (Entry ent : *this)
			std::cout << this->entry2str(ent) << " ";
		std::cout << "]" << std::endl;
	}
};
