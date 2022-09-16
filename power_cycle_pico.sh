#!/bin/bash
sudo systemctl stop controller
sudo uhubctl -l 1-1 -p 2 -a 0
sleep 2
sudo uhubctl -l 1-1 -p 2 -a 1
sudo systemctl start controller
