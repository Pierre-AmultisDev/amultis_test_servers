#!/bin/bash
# =============================================================================
#
# @package    aMultis test servers
# @container  Raspberry Pi Local
# @name       run_mqtt_publisher_sh_app.sh
# @purpose    script to run shell script
# @version    v0.0.1  2025-06-08
# @author     pierre@amultis.dev
# @copyright  (C) 2020-2025 Pierre Veelen
#
# =============================================================================

echo [INFO ] Starting MQTT publisher ...

# Show some info about the host
# cat /etc/os-release

# start the app
cd ./sh_app
./test_pub.sh
cd ..
