/* Jakub Skalski 314007 */

#include "utils.cpp"
#include <vector>


class Entry {
	public:
	ip_t net;
	mask_t mask;
	distance_t dist;
	ip_t via;
	uint32_t ttl;
};


class Table : public std::vector<Entry> {

	void print_entry(Entry ent) {
		using std::cout;
		const auto[net, mask, dist, via, ttl] = ent;

		cout << ip2str(net) << "/" << (ip_t)mask << " ";
		if (dist == UNREACHABLE)
			cout << "\033[1;31munreachable \033[0m";
		else
			cout << "distance " << dist << " ";
		
		if (via == DIRECT)
			cout << "connected directly";
		else
			cout << "via " << ip2str(via);

		debug(cout << " (" << ttl << ")";)
		cout << '\n';
	}

	public:
	Entry &operator[](ip_t subnet) {
		/* Extract entry by subnet */

		for (Entry &ent : *this)
			if (net(ent.net, ent.mask) == net(subnet, ent.mask))
				return ent;
		throw std::invalid_argument("Key " + ip2str(subnet) + " does not exist");
	}

	void include(Entry ent) {
		/* Attempt to insert a new entry into the table */ 

		try {
			Entry &ant = (*this)[ent.net];
			
			if (ent.dist == UNREACHABLE and ant.dist == UNREACHABLE)
				return;

			if (ent.via == ant.via or ent.dist <= ant.dist)
				ant = ent;
		}

		catch (std::invalid_argument const&) {
			if (ent.dist != UNREACHABLE or ent.via == DIRECT)
				this->push_back(ent);
		}

	}

	void decay() {
		/* Remove expired entries */

		for (auto it = this->begin(); it != this->end(); ++it) {
			it->ttl = std::max(1, (int)it->ttl) - 1;
			if (!it->ttl and it->via != DIRECT and it->dist == UNREACHABLE)
				this->erase(it--);
		}
	}

	distance_t dist(ip_t subnet) {
		return (*this)[subnet].dist;
	}

	void show() {
		fflush(stdout);
		system("clear");

		for (Entry ent : *this)
			this->print_entry(ent);
	}
};
