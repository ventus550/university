CFLAGS = -std=c++17 -Wall -Wextra

traceroute: ping.o receive.o traceroute.o
	g++ ping.o receive.o traceroute.o -o traceroute

ping.o: ping.cpp traceroute.h
	g++ -c $(CFLAGS) ping.cpp

receive.o: receive.cpp traceroute.h
	g++ -c $(CFLAGS) receive.cpp

traceroute.o: traceroute.cpp traceroute.h
	g++ -c $(CFLAGS) traceroute.cpp
	
zip:
	make distclean
	tar -cvJf ../jakub_skalski.tar.xz .

clean: 
	rm -f *.o

distclean:
	rm -f *.o traceroute