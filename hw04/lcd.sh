#!/bin/bash
sudo ./on_180.sh
sleep 2
sudo fbi -noverbose -T 1 -a tux.png
sleep 4
sudo ./turn_off.sh
sleep 2
sudo ./on_90.sh
sleep 2
sudo fbi -noverbose -T 1 -a tux.png
sleep 4
sudo ./text.sh
sleep 8
sudo mplayer away.mpg
sleep 2
./turn_off.sh