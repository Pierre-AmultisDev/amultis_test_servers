#!/bin/bash
# =============================================================================
#
# @package    amultis test servers
# @container  Raspberry Pi Local
# @name       run_udp_sender_py_app_on_8888.sh
# @purpose    startscript for python program
# @version    v0.0.1  2025-05-25
# @author     pierre@amultis.dev
# @copyright  (C) 2020-2025 Pierre Veelen
#
# =============================================================================

echo [INFO ] Starting UDP receiver ...

# Show some info about the host
# cat /etc/os-release

# set the port number and buffer size for the udp receiver
# export udpSendToIP=127.0.0.1
export udpSendToIP=195.240.91.108
export udpSendToPort=8888
export udpBuffer=1024

# start the app
cd ./py_app
python3 udp_sender.py
cd ..
