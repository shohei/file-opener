#!/bin/sh
sudo echo ""
DIR="$( cd "$( dirname "$0" )" && pwd -P )"
sudo nohup python $DIR/server.py > log.txt 2>&1 &
