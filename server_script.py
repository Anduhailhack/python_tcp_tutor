#!/bin/python

import socket

def main():
    IP_ADDR = '127.0.0.1'
    PORT = 2223
    print("[*] Server started ...!")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.bind((IP_ADDR, PORT))
        print("[*] Binded Successfully ...!")
    except:
        PORT = PORT+1
        main()

    try:
        sock.listen(5)
        data, addr = sock.accept()

        while True:
            print("[*] Got connection from >> ", addr)
            msg = data.recv(1024)
            print("[*] Message from client >> ", msg.encode('utf8'))

            msg_server = str(input("Enter message : "))
            msg_server = msg_server.encode('utf8')
            data.send(msg_server)

        sock.close()
    except:
        print("[*] Error ...!")

if __name__ == '__main__':
    main()
