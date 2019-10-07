Device Name         |   Start Address   |       End Address
-----------         |   -------------   |       -----------
External Memory     |   0x0000_0000     |       0x1FFF_FFFF
SRAM internal       |   0x402F_0400     |       0x402F_FFFF
GPIO0               |   0x44E0_7000     |       0x44E0_7FFF
UART Registers      |   0x44E0_9000     |       0x44E0_9FFF
I2C0                |   0x44E0_B000     |       0x44E0_BFFF
UART1               |   0x4802_2000     |       0x4802_2FFF
UART2               |   0x4802_4000     |       0x4802_4FFF
I2C1                |   0x4802_A000     |       0x4802_AFFF
GPIO1               |   0x4804_C000     |       0x4804_CFFF
I2C2                |   0x4819_C000     |       0x4819_CFFF
UART3               |   0x481A_6000     |       0x481A_6FFF
UART4               |   0x481A_8000     |       0x481A_8FFF
UART5               |   0x481A_A000     |       0x481A_AFFF
GPIO2               |   0x481A_C000     |       0X481A_CFFF
GPIO3               |   0x481A_E000     |       0x481A_EFFF
LCD controller      |   0x4830_E000     |       0x4830_EFFF
SDRAM               |   0X8000_0000     |       0X8FFF_FFFF


--GPIO via MMAP--

1:  Successfully completed making LEDs blink with button press
    The two buttons are on pins P9_12 and P9_25.
    P9_12 controls user 2 LED
    P9_25 controls user 3 LED
    
2:  Successfully completed toggling the gpio pin. 
    Oscilloscope results:
        period: 100us
        read 125us on oscilloscope
        CPU usage around 3% wasn't a constant number.

--LCD Display--

Successfully added tux.png and flipped him on the display.
Added the text file displaying my name and text at the bottom of the screen
Added the movie trailer to Spirited Away

## Prof. Yoder's comments

Well done.

Grade:  10/10