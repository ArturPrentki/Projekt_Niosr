#!/bin/bash

set -e

source /opt/ros/humble/setup.bash
source /home/niosr/startgazebo.sh

echo "Provided arguments: $@"

exec $@
