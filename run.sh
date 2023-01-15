#!/bin/sh
sudo echo ""
sudo nohup python server.py > log.txt 2>&1 &
