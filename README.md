# CPU and Memory Simulations
## Main goal
The main goal of this project is implementation of process scheduling algorithms and page replacement algorithms and in the next step testing each of them. To write this simulation I used Python programming laguage in 3.11.7 version. I chose following process scheduling algorithms:
- First Come First Server (FCFS)
- Shortest Job First (SJF)

And page replacement algorithms:
- First In First Out (FIFO)
- Least Frequently Used (LFU)

## Process Scheduling algorithms
**FCFS** (First Come, First Served) is a type of scheduling algorithm used by operating systems and networks to efficiently and automatically execute queued tasks, processes and requests by the order of their arrival. An FCFS scheduling algorithm may also be referred to as a first-in, first-out (FIFO) algorithm or a first-come.

**SJF** (Shortest Job First) is an algorithm in which the process having the smallest execution time is chosen for the next execution. This scheduling method can be preemptive or non-preemptive. It significantly reduces the average waiting time for other processes awaiting execution.

### Data generator
To create simulation data I wrote a simple function placed in process_generator.py file which creates processes. Every process has a duration time and await time to enter queue. To call the function you need three arguments: maximum process duration time, maximum process await time and the number of processes to place in the output file. The results are in the fcfs_sjf_simulation_input.txt.

### Algorithms implementation
The simulation code is placed in fcfs_sjf_simulation.py. FCFS and SJF algorithms have separate functions. There is also a function that creates list of processes and every process is an object of Process class. To run the simulation it's necessary to input the argument as list of processes. To see algorithms performance differences
