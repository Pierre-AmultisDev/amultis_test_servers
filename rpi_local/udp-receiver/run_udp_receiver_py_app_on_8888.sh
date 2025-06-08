#!/bin/bash
# =============================================================================
#
# @package    aMultis test servers
# @container  Raspberry Pi Local
# @name       run_udp_receiver_py_app_on_8888.sh
# @purpose    script to run python script
# @version    v0.0.1  2025-05-25
# @author     pierre@amultis.dev
# @copyright  (C) 2020-2025 Pierre Veelen
#
# =============================================================================

echo [INFO ] Starting UDP receiver ...

# Show some info about the host
# cat /etc/os-release

# set the port number and buffer size for the udp receiver
export udpReceiveFromPort=8888
export udpBuffer=1024

# start the app
cd ./py_app
python3 udp_receiver.py
cd ..
