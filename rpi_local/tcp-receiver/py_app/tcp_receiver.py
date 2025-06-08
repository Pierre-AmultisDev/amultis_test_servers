# =============================================================================
#
# @package    aMultis test servers
# @container  Raspberry Pi Local
# @name       tcp_receiver.py
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
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Internet, TCP
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # get host ip address
    temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    temp_socket.connect(("8.8.8.8", 80))
    ip_address = temp_socket.getsockname()[0]
    temp_socket.close()

    server_socket.bind(('', receive_from_port))
    server_socket.listen(5)  # Maximaal 5 clients in wachtrij

    now = datetime.now()
    print("[INFO ]", now.strftime("%Y-%m-%d %H:%M:%S"), f"TCP receiver initialized at IP: {ip_address} on port: {receive_from_port}")
    return server_socket


# function main 
# -------------
def main(server_socket, bufferSize=1024):
    while True:
        now = datetime.now()
        print("[INFO ]", now.strftime("%Y-%m-%d %H:%M:%S"), "Waiting for a connection ...")
        
        conn, addr = server_socket.accept()
        now = datetime.now()
        print("[INFO ]", now.strftime("%Y-%m-%d %H:%M:%S"), "Connection established with", f"{addr}")

        try:
            data = conn.recv(bufferSize)
            if not data:
                now = datetime.now()
                print("[INFO ]", now.strftime("%Y-%m-%d %H:%M:%S"), "No data received, closing connection.")
                conn.close()
                continue

            now = datetime.now()
            print("[INFO ]", now.strftime("%Y-%m-%d %H:%M:%S"), f"received message: ->|{data.decode()}|<- from IP {addr}")

            #msgToSend = "Message received OK at " + now.strftime("%Y-%m-%d %H:%M:%S")
            #conn.sendall(msgToSend.encode())

        except Exception as e:
            print("[ERROR]", now.strftime("%Y-%m-%d %H:%M:%S"), e)
        finally:
            conn.close()
            print("[INFO ]", now.strftime("%Y-%m-%d %H:%M:%S"), "Connection closed.")

if __name__ == '__main__':
    TCP_receiverport = int(os.getenv("tcpReceiveFromPort", 8888))
    TCP_buffer = int(os.getenv("tcpBuffer", 1024))

    TCP_receiver = init(TCP_receiverport)
    main(TCP_receiver, TCP_buffer)
