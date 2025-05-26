# =============================================================================
#
# @package    aMultis test servers
# @container  Raspberry Pi Local
# @name       tcp_sender.py
# @purpose    start script for python program
# @version    v0.0.1  2025-05-25
# @author     pierre@amultis.dev
# @copyright  (C) 2020-2025 Pierre Veelen
#
# =============================================================================
import socket
import os
import time
from datetime import datetime


# function init 
# -------------
def init():
    # Maak een TCP socket (client side)
    return socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)


# function main
# -------------
def main(TCPSenderSocket, to_server="127.0.0.1", to_port=8888, bufferSize=1024):
    # resolve IP address
    to_server_IP = socket.getaddrinfo(to_server, to_port, proto=socket.IPPROTO_TCP)[0][4][0]

    print(f"[INFO ] Connecting to server {to_server} on IP {to_server_IP} via port {to_port}")
    TCPSenderSocket.connect((to_server_IP, to_port))
    print("[INFO ] Connected.")

    counter = 0
    try:
        while True:
            msgToSend = "Hello from TCP Sender " + str(counter).zfill(4)
            now = datetime.now() 
            print("[INFO ]", now.strftime("%Y-%m-%d %H:%M:%S"))
            print("Sending message: ->|{}|<-".format(msgToSend))
            
            TCPSenderSocket.sendall(msgToSend.encode())

            print("Waiting for return message...")
            msgFromServer = TCPSenderSocket.recv(bufferSize)
            print("Message received over TCP ->|{}|<-".format(msgFromServer.decode()))

            counter = (counter + 1) % 10000
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\n[INFO ] Stopping sender.")
    except Exception as e:
        print("[ERROR]", e)
    finally:
        TCPSenderSocket.close()
        print("[INFO ] Socket closed.")

if __name__ == '__main__':
    TCP_send_to_server = str(os.getenv("tcpSendToIP", "127.0.0.1"))
    TCP_send_to_port = int(os.getenv("tcpSendToPort", 8888))
    TCP_buffer = int(os.getenv("tcpBuffer", 1024))
    
    TCP_sender = init()
    main(TCP_sender, TCP_send_to_server, TCP_send_to_port, TCP_buffer)
