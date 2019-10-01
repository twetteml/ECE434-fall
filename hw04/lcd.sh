#!/bin/bash
sudo ./on_180.sh
sleep 5
sudo fbi -noverbose -T 1 -a tux.png
sleep 10
sudo ./turn_off.sh
sleep 5
sudo ./on_90.sh
sleep 5
sudo fbi -noverbose -T 1 -a tux.png
sleep 10
./turn_off.sh