# =============================================================================
#
# @package    aMultis test servers
# @container  Raspberry Pi Local
# @name       udp_sender.py
# @purpose    start script for python program
# @version    v0.0.1  2025-05-25
# @author     pierre@amultis.dev
# @copyright  (C) 2020-2025 Pierre Veelen
#
# =============================================================================
import socket
from datetime import datetime
import os
import time

 
# function init 
# -------------
def init():
    # Create a UDP socket at client/sender side
    # UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    return socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


# function main
# -------------
def main(UDPSenderSocket, to_server="127.0.0.1", to_port=8888, bufferSize=1024):

    # get the IP address of to_server
    # https://docs.python.org/3/library/socket.html#socket.getaddrinfo
    to_server_IP = socket.getaddrinfo(to_server, to_port, proto=socket.IPPROTO_UDP)[0][4][0]

    counter = 0
    while True: 
        msgToSend = "Hello from UDP Sender " + str(counter).zfill(4)
        now = datetime.now() 
        print("[INFO ]", now.strftime("%Y-%m-%d %H:%M:%S"))
        print("sending message: ->|{}|<-".format(msgToSend))
        print("to:", to_server, "on IP:", to_server_IP, "via port:", str(to_port))
        
        bytesToSend = msgToSend.encode()
        # Send to server using created UDP socket
        UDPSenderSocket.sendto(bytesToSend, (to_server_IP,to_port))

        # wait for message from the other side    
        print("Waiting for return message")
        msgFromServer = UDPSenderSocket.recvfrom(bufferSize)
        msg = "Message received over UDP ->|{}|<-".format(msgFromServer[0].decode())
        print(msg)

        counter = counter + 1
        if counter == 9999:
            counter = 0
        time.sleep(5)
    return

if __name__ == '__main__':
    UDP_send_to_server= str(os.getenv("udpSendToIP", "127.0.0.1"))
    UDP_send_to_port = int(os.getenv("udpSendToPort", 8888))
    UDP_buffer = int(os.getenv("udpBuffer", 1024))
    
    UDP_sender = init()
    main(UDP_sender, UDP_send_to_server, UDP_send_to_port, UDP_buffer)
