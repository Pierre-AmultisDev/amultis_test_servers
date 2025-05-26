#!/bin/bash
# =============================================================================
#
# @package    aMultis test servers
# @container  Raspberry Pi Local
# @name       run_udp_sender_py_app_on_8888.sh
# @purpose    start script for python program
# @version    v0.0.1  2025-05-25
# @author     pierre@amultis.dev
# @copyright  (C) 2020-2025 Pierre Veelen
#
# =============================================================================

echo [INFO ] Starting UDP sender ...

# Show some info about the host
# cat /etc/os-release

# export udpSendToIP=127.0.0.1
# export udpSendToIP=195.240.91.108
export udpSendToIP=udp-local.amultis.dev

# set the port number and buffer size for the udp receiver
export udpSendToPort=8888
export udpBuffer=1024

# start the app
cd ./py_app
python3 udp_sender.py
cd ..
