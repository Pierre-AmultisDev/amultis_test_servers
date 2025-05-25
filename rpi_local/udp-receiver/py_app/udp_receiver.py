#Libraries
import socket    #https://wiki.python.org/moin/UdpCommunication
from datetime import datetime
import os

##Parameters
#localPort=8888
#bufferSize=1024

#Objects
#sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  ## Internet,UDP

## function get_ip_address 
## -------------
#def get_ip_address():
#    """get host ip address"""
#    ip_address = '';
#    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    s.connect(("8.8.8.8",80))
#    ip_address = s.getsockname()[0]
#    s.close()
#    return ip_address

# function init 
# -------------
def init(receive_from_port):
    receiversocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  ## Internet,UDP
    # get host ip address
    ip_address = '';
    receiversocket.connect(("8.8.8.8",80))
    ip_address = receiversocket.getsockname()[0]
    receiversocket.close()

    receiversocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  ## Internet,UDP
    receiversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    receiversocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) #enable broadcasting mode
    receiversocket.bind(('', receive_from_port))
    print("UDP receiver initialized at IP: {} on port: {}".format(ip_address,receive_from_port))
    return receiversocket

    
# function main 
# -------------
def main(UDPReceiverSocket, bufferSize=1024):
    while True:
        data, addr = UDPReceiverSocket.recvfrom(bufferSize) # get data
        now = datetime.now() 
        print("[INFO ]", now.strftime("%Y-%m-%d %H:%M:%S"), "received message: ->|{}|<- from IP {}".format(data.decode(),addr))
        msgToSend = "Message received OK at " + now.strftime("%Y-%m-%d %H:%M:%S")
        UDPReceiverSocket.sendto(msgToSend.encode(),addr)  # write data
    return


if __name__ == '__main__':
    UDP_receiverport = int(os.getenv("udpReceiveFromPort", 8888))
    UDP_buffer = int(os.getenv("udpBuffer", 1024))
    
    UDP_receiver = init(UDP_receiverport)
    main(UDP_receiver, UDP_buffer)
