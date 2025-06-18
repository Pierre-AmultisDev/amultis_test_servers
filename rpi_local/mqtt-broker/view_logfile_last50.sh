#!/bin/bash
# =============================================================================
#
# @package    aMultis test servers
# @container  Raspberry Pi Local
# @name       view_logfile_last50.sh
# @purpose    script to run shell script
# @version    v0.0.1  2025-06-18
# @author     pierre@amultis.dev
# @copyright  (C) 2020-2025 Pierre Veelen
#
# =============================================================================

echo [INFO ] Starting logviewe ...

# Show some info about the host
# cat /etc/os-release

sudo tail -n 50 /var/log/mosquitto/mosquitto.log

