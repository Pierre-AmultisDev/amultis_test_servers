#!/bin/bash
# =============================================================================
#
# @package    aMultis test servers
# @container  Raspberry Pi Local
# @name       run_publish_host_port_sh_app.sh
# @purpose    script to run shell script
# @version    v0.0.1  2025-06-18
# @author     pierre@amultis.dev
# @copyright  (C) 2020-2025 Pierre Veelen
#
# =============================================================================

echo [INFO ] Starting MQTT subscriber ...

# Show some info about the host
# cat /etc/os-release

# start the app
cd ./sh_app
./publish_host_port.sh
cd ..
