#!/bin/sh
sudo lsof -i -P | grep LISTEN | grep :4568
