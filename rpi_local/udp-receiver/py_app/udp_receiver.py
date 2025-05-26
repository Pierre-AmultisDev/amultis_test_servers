# =============================================================================
#
# @package    aMultis test servers
# @container  Raspberry Pi Local
# @name       udp_receiver.py
# @purpose    start script for python program
# @version    v0.0.1  2025-05-25
# @author     pierre@amultis.dev
# @copyright  (C) 2020-2025 Pierre Veelen
#
# =============================================================================
import socket
import os
from datetime import datetime

# function init 
# -------------
def init(receive_from_port):
    # get host ip address
    temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    temp_socket.connect(("8.8.8.8", 80))
    ip_address = temp_socket.getsockname()[0]
    temp_socket.close()

    receiversocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  ## Internet,UDP
    receiversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    receiversocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) #enable broadcasting mode
    receiversocket.bind(('', receive_from_port))
    print("UDP receiver initialized at IP: {} on port: {}".format(ip_address, receive_from_port))
    return receiversocket

    
# function main 
# -------------
def main(UDPReceiverSocket, bufferSize=1024, to_port=8888):
    while True:
        data, from_address = UDPReceiverSocket.recvfrom(bufferSize) # get data
        print(from_address)

        now = datetime.now() 
        print("[INFO ]", now.strftime("%Y-%m-%d %H:%M:%S"), "received message: ->|{}|<- from IP {}".format(data.decode(), from_address))
        msgToSend = "Message received OK at " + now.strftime("%Y-%m-%d %H:%M:%S")
        bytesToSend = msgToSend.encode()

        UDPReceiverSocket.sendto(bytesToSend, from_address) # write data
     
    return


if __name__ == '__main__':
    UDP_receiverport = int(os.getenv("udpReceiveFromPort", 8888))
    UDP_buffer = int(os.getenv("udpBuffer", 1024))
    
    UDP_receiver = init(UDP_receiverport)
    main(UDP_receiver, UDP_buffer, UDP_receiverport)
