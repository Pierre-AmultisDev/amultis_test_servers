#!/bin/bash
# =============================================================================
#
# @package    aMultis test servers
# @container  Raspberry Pi Local
# @name       run_test_port.sh
# @purpose    script to run shell script
# @version    v0.0.1  2025-06-18
# @author     pierre@amultis.dev
# @copyright  (C) 2020-2025 Pierre Veelen
#
# =============================================================================

echo [INFO ] Starting port tester ...

# Show some info about the host
# cat /etc/os-release

echo [INFO ] Show active listerners on port 1883 ...
sudo ss -tulnp | grep 1883

echo [INFO ] Show active listerners on port 8123 ...
sudo ss -tulnp | grep 8123
