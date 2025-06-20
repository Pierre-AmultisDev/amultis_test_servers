#!/bin/bash
# =============================================================================
#
# @package    aMultis test servers
# @container  Raspberry Pi Local
# @name       run_mqtt_broker_sh_app.sh
# @purpose    script to run shell script
# @version    v0.0.1  2025-06-08
# @author     pierre@amultis.dev
# @copyright  (C) 2020-2025 Pierre Veelen
#
# =============================================================================

echo [INFO ] Starting MQTT broker ...

# Show some info about the host
# cat /etc/os-release

# start the app
cd ./sh_app
sudo cp mosquitto_basic.conf /etc/mosquitto/conf.d/mosquitto_basic.conf
./test_broker_basic.sh
cd ..
