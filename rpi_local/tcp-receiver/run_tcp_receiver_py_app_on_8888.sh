#!/bin/bash
# =============================================================================
#
# @package    aMultis test servers
# @container  Raspberry Pi Local
# @name       run_tcp_receiver_py_app_on_8888.sh
# @purpose    script to run python script
# @version    v0.0.1  2025-05-25
# @author     pierre@amultis.dev
# @copyright  (C) 2020-2025 Pierre Veelen
#
# =============================================================================

echo [INFO ] Starting TCP receiver ...

# Show some info about the host
# cat /etc/os-release

# set the port number and buffer size for the tcp receiver
export tcpReceiveFromPort=8888
export tcpBuffer=1024

# start the app
cd ./py_app
python3 tcp_receiver.py
cd ..
