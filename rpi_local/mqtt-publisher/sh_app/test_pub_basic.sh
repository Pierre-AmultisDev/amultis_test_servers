#!/bin/bash
while true
do
    mosquitto_pub -d -t test_topic -m "test message at $(date '+%F %H:%M:%S')" 
    echo "$(date '+%F_%H:%M:%S') Press [CTRL-C] to stop ..."
    sleep 10
done


