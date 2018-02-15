#!/usr/bin/env python3
import socket
import sys

def main(ip="127.0.0.1", port=80):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    s.listen(5)

    print("[*] Server listening on: IP:{} PORT:{}".format(ip, port))

    try:
        while True:
            c_sock, c_addr = s.accept()

            c_recv = c_sock.recv().decode()
            print("[*] {} - {}", format(c_addr, c_recv))
    except KeyboardInterrupt:
        pass
    finally:
        print("[-] Server closed.")
        s.close()

if __name__ == '__main__':
    #NOTE: IP passed as first arg and port as second
    if len(sys.argv) == 3:
        ip = sys.argv[1]
        port = sys.argv[2]
        main(ip, port)
    else:
        main()
