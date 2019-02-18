MYINCLUDEDIR=include
MYLIBDIR=lib

all:
	make add
	make sum

sum:
	#gcc -o test main.c $(MYLIBDIR)/libadd.a
	gcc -o test main.c -I $(MYINCLUDEDIR) -L $(MYLIBDIR) -ladd

add:
	gcc -c $(MYLIBDIR)/add.c -o $(MYLIBDIR)/add.o
	ar rcs -o $(MYLIBDIR)/libadd.a $(MYLIBDIR)/add.o

clean:
	rm -rf $(MYLIBDIR)/*.a $(MYLIBDIR)/*.o test
