#!/bin/sh
sudo echo ""
DIR="$( cd "$( dirname "$0" )" && pwd -P )"
sudo nohup python3 $DIR/server.py > log.txt 2>&1 &
