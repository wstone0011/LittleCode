all: sniffex.c
	gcc -Wall -o sniffex sniffex.c -lpcap

with_pfring:
	gcc -Wall -o sniffex sniffex.c -rdynamic /usr/local/lib/libpcap.so -Wl,-rpath,/usr/local/lib

clean:
	rm -f *.o sniffex

