#!/usr/bin/env python

#temp= `i2cget -y 2 0x48`

temp1=`i2cget -y 2 0x48`  
temp2=`i2cget -y 2 0x4a` 

echo -n "Temp Sensor 1: "
echo $((temp1*18/10+32))
echo $(($temp1))

echo -n "Temp Sensor 2: "
echo $((temp2*18/10+32))
echo $(($temp2))


i2cset -y -r 2 0x48 0x02 22
i2cset -y -r 2 0x4a 0x02 22

i2cset -y -r 2 0x4a 0x03 27
i2cset -y -r 2 0x4a 0x03 27