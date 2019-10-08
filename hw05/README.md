Madeline Twetten
Homework 5

--Project--
Successfully wrote in the project document. I signed up for the espresso machine
and I will be working with Hannah and Rahul.

--Make--
Successfully did the make exercise on the wiki. I included the makefile in my
directory.

--Installng the Kernel Source--
I installed the kernel source a received the following when telling it to boot
one the bone.

debian@beaglebone:/var/lib/cloud9$ head -3 /boot/uEnv.txt
#Docs: http://elinux.org/Beagleboard:U-boot_partitioning_layout_2.0

uname_r=5.4.0-rc2-bone1

--Cross-Compiling--

From Host:
Hello, World! Main is executing at 0x556308b406aa
This address (0x7ffd95d50e60) is in our stack frame
This address (0x556308d41018) is in our bss section
This address (0x556308d41010) is in our data section

From Bone:
Hello, World! Main is executing at 0x4575ad
This address (0xbecceb78) is in our stack frame
This address (0x468010) is in our bss section
This address (0x468008) is in our data section

--Kernel Modules--


