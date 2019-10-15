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

8. What is dispatch latency? Scheduling latency?

9. What is mainline?

10. What is keeping the External event in Figure 3 from starting?

11. Why can the External event in Figure 4 start sooner?
