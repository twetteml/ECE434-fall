#!/bin/bash
export LED=51         # P9_16

# This is for the Black SPI 0
export RESET=12     # RESET - P9_20
export DC=13        # D/C   - P9_19
export CS=5         # CS    - P9_17

sudo bash << EOF
    # Remove the framebuffer modules
    if lsmod | grep -q 'fbtft_device ' ; then rmmod fbtft_device;  fi
    if lsmod | grep -q 'fb_ili9341 '   ; then rmmod --force fb_ili9341;    fi
    if lsmod | grep -q 'fbtft '        ; then rmmod --force fbtft;         fi
    # Set the pinmuxes for the display
    config-pin P9_19 gpio   # D/C
    config-pin P9_20 gpio   # RESET
    config-pin P9_18 spi    # spi 0_d1 MOSI
    config-pin P9_21 spi    # spi 0_d0 MISO
    config-pin P9_22 spi_sclk # spi 0_sclk
    config-pin P9_17 spi_cs # spi 0_cs0
    
    # LED pin, turn on
    ./backl.py
    sleep 0.1
    
    # Insert the framebuffer modules
    modprobe fbtft_device name=adafruit28 busnum=1 rotate=180 gpios=reset:$RESET,dc:$DC cs=0
EOF