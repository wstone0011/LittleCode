MYINCLUDEDIR=include
MYLIBDIR=lib

all:
	make add
	make sum

sum:
	#gcc -o test main.c -I $(MYINCLUDEDIR) -L. -ladd -Wl,-rpath,./
	gcc -o test main.c -I $(MYINCLUDEDIR) -rdynamic ./libadd.so -Wl,-rpath,./

add:
	#gcc -c -o libadd.o -fPIC $(MYLIBDIR)/add.c
	#gcc -shared -o libadd.so libadd.o
	gcc -shared -fpic -o libadd.so $(MYLIBDIR)/add.c

clean:
	rm -f *.o *.so test
