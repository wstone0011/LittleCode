package main

import (
	"flag"
	"log"
	"net/http"
	"os"
	"fmt"
	"net"
)
func GetIntranetIp() {
	addrs, err := net.InterfaceAddrs()

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	for _, address := range addrs {

		// check if the ip address was loopback address
		if ipnet, ok := address.(*net.IPNet); ok && !ipnet.IP.IsLoopback() {
			if ipnet.IP.To4() != nil {
				log.Printf("Avalible Address: %s", ipnet.IP.String())
			}

		}
	}
}

func main() {
	port := flag.String("p", "8100", "port to serve on")
	directory := flag.String("d", ".", "the directory of static file to host")
	flag.Parse()

	http.Handle("/", http.FileServer(http.Dir(*directory)))

	log.Printf("Serving %s on HTTP port: %s\n", *directory, *port)
	GetIntranetIp()
	log.Fatal(http.ListenAndServe(":"+*port, nil))
}
