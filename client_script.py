#!/bin/python

import socket

def main():
    IP_ADDR = '127.0.0.1'
    PORT = 2223
    print("[*] Client started ...!")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((IP_ADDR, PORT))
        print("[*] Successfully Connected ...!")
    except:
        print("[*] Connection Refused ...!")
        exit()

    try:
        while True:
            msg = input("Enter message: ")
            msg = msg.encode('utf8')
            sock.send(msg)
            msg_recv = sock.recv(1024)
            print("[*] Message from server >> ", msg_recv.encode('utf8'))
        sock.close()
    except:
        print("[*] Error ...!")

if __name__ == '__main__':
    main()
