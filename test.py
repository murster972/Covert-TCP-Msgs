from scapy.all import *

def main():
    src=""
    ip = IP(src="10.216.74.192")

    #ip.dst="216.58.206.142"
    ip.dst = "10.216.69.91"
    tcp = TCP(dport=8000)

    ip.id = 1024

    tcp.seq = 23

    #ip.show()

    while True:
        input("Pause...")
        send(ip/tcp)
