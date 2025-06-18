#!/bin/bash
# sudo is required to ensure access to pid file (/run/mosquitto/mosquitto.pid) as defined in .conf 
sudo mosquitto --config-file /etc/mosquitto/mosquitto.conf
