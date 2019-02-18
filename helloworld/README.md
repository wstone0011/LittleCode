# gcc编译静态库
```
gcc -c $(MYLIBDIR)/add.c -o $(MYLIBDIR)/add.o
ar rcs -o $(MYLIBDIR)/libadd.a $(MYLIBDIR)/add.o
```

# gcc编译动态库
```
gcc -shared -fpic -o libadd.so $(MYLIBDIR)/add.c
#gcc -o test main.c -I $(MYINCLUDEDIR) -L. -ladd -Wl,-rpath,./
gcc -o test main.c -I $(MYINCLUDEDIR) -rdynamic ./libadd.so -Wl,-rpath,./


-I  指定头文件目录，优先搜索的目录。
-L  指定库文件目录
-ladd  表名链接的库是libadd.a
-fpic或-fPIC，不生成用于定位的PLT部分代码。默认参数是-mgotplt。
-Wl    将后面的参数传给链接器
-rpath 设置动态库搜索路径
```

# pcap抓包举例
```
gcc -Wall -o sniffex sniffex.c -lpcap

-Wall  显示所有警告
```

# pcap with pf_ring
## 编译并安装pf_ring
```
下载pf_ring源码
git clone https://github.com/ntop/PF_RING.git

cd PF_RING/kernel
./configure
make
make install

cd PF_RING/userland/lib
./configure
make
make install

PF_RING/userland/libpcap-1.8.1
./configure
make
make install

编译后的最终文件
kernel/pf_ring.ko
userland/lib/libpfring.so
userland/libpcap-1.8.1/libpcap.so.1.8.1

在系统中的位置
/lib/modules/3.10.0-693.el7.x86_64/kernel/net/pf_ring/pf_ring.ko
/usr/local/lib/libpfring.so
/usr/local/lib/libpcap.so.1.8.1
```
## 链接libpcap.so with pf_ring
```
gcc -Wall -o sniffex sniffex.c -rdynamic /usr/local/lib/libpcap.so -Wl,-rpath,/usr/local/lib

可用来判断是否链接成功的命令
ldd sniffex
lsmod |grep pf_ring
strings /usr/local/lib/libpcap.so.1.8.1 |grep pf_ring
strings /usr/local/lib/libpcap.so.1.8.1 |grep pfring
```
