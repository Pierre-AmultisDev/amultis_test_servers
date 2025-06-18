#!/bin/bash
#
# subscribe to host 192.168.2.83 (wired)
# using port 1883
# for topic # (all topics)
#
mosquitto_sub --host 192.168.2.83 --port 1883 --topic "#"