Homework 2 - Madeline Twetten

---Buttons and LEDs---
Successfully created the buttons blinking LEDs program + ran on board.
The program is BlinkYoLEDS.py

---Measuring a gpio pin on an oscilloscope---

1: min: 0V, max: 3.3V

2: 238ms

3: It is over twice 100ms (138ms more than 100ms).

4: The 100ms is half of the period, the reast of the 38ms is overhead time.

5: About 3% usage

6:
sleep time       period         processor usage
0.05              136.5ms               6.0%
0.025             86ms                  8.7%    
0.01              56.3ms                13.6%                    
0.005             46ms                  15.8%    

7: The period is not stable, every second or so, it spikes to a higher number like 70ms or 130ms

8: When I ran vi, my period became stable and only toggled in a range of 1ms.

9: From my observations, cleaning up togglegpio.sh does not affect the period, but it becomes 
   a little more stable

10: Yes, the period is shorter.

11: The smallest period that I was able to get was about 26ms.

---Python script---
The python script is togglegpio.py. To change the period, change the variable 
period in the python file.

1: Min 0v, Max 3.3V
2: 101ms 
3: It is almost exactly 100ms
4: This value is not different than 100ms.
5: About 1.3%
6:
sleep time          period          processor usage
0.05                51.38ms         2.1%
0.025               26ms            4.3%
0.01                11.38ms         10%
0.005               6.35ms          19%

7: The period seems more stable, it does not rapidly jump.
8: When i ran vi, my period remained stable.
9: Made my own python script
10: Did not use togglegpio.sh for my python script.
11: The smallest period I can get is around 380us

---C script---

1: Min 0v, max 3.2V
2: 409us
3: It is not close to 100ms, the C toggling is much faster.
4: This value is different because the compiler can quickly do C code.
5: About 50%
6:
sleep time          period          processor usage
1000                3ms             48%
60                  407us           36%
0                   280us           100%

7: The period is unstable
8: When I ran vi, the period stayed around the 410us range rather than jumping to 500us.
9: Used the c script
10: Used the c script
11: The smallest period I can get is 280us.

---Etch a Sketch---

The 4 buttons draw the etch a sketch. If you press both button 1 and button 4 at 
the same time, the program exits. If you hold down a button, the program automtically
draws until it hits the edge of the window. Edit the window variable in the .py file
to change the window size.
