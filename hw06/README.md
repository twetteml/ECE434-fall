Madeline Twetten
Homework 6

--Watch--

1. Where does Julia Cartwright work?
National Instruments

2. What is PREEMT_RT? Hint: Google it.
Real time linux kernel patch

3. What is mixed criticality?
When a system is able to handle two different types of criticality (safety and non-safety) 
and can run them at the same time.

4. How can drivers misbehave?
scheduler, shared kernel, and the stack between rt and non-rt.

5. What is Δ in Figure 1?
It is the latency. The delta is the change between the event and the application launch.

6. What is Cyclictest[2]?
Have a timestamp and sleep for a certain amount of time. Then, have another timestamp and take the
difference between the first and second to find out the total amount of time slept. Subtract the set
duration from the difference between the two time stamps to find the latency.

7. What is plotted in Figure 2?
In figure two, the results from cyclictest are plotted form preempt and preempt_rt.

8. What is dispatch latency? Scheduling latency?
dispatch latency -> the amount of time a system takes to respond to a request for a process to begin operation.
scheduling latency -> the time that the system is inproductive due to scheduling tasks.

9. What is mainline?
A process that is running that contains mulitple threads that can be switched on and off of the process.

10. What is keeping the External event in Figure 3 from starting?
It can't start until the interrupt finishes.

11. Why can the External event in Figure 4 start sooner?
It can start sooner because it is now preemptive, so the interrupt can go into another thread.

## Prof. Yoder's comments

Good start.  Looking for plots.

Grade:  7/10
