CFLAGS = -std=c++17 -Wall -Wextra -O3

transport:
	g++ $(CFLAGS) transport.cpp socket.cpp window.cpp -o transport
	
test:
	-pkill -f transport-server
	g++ $(CFLAGS) transport.cpp -o transport
	@./transport-binaries/transport-server 32123 &
	./transport 127.0.0.1 32123 output 1

zip:
	make distclean
	tar -cvJf ../jakub_skalski.tar.xz .

clean: 
	rm -f *.o

distclean:
	rm -f *.o transport
	
upload:
	bash ../upload.sh
	
mount:
	bash ../mount.sh
