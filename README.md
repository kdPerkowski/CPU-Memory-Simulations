# CPU and Memory Simulations
## Main goal
The main goal of this project is implementation of process scheduling algorithms and page replacement algorithms and in the next step testing each of them. To write this simulation I used Python programming laguage in 3.11.7 version. I chose following process scheduling algorithms:
- First Come First Server (FCFS)
- Shortest Job First (SJF)

And page replacement algorithms:
- First In First Out (FIFO)
- Least Frequently Used (LFU)

## How to run script
If needed, it's possible to import function from files fcfs_sjf_simulation.py or FIFO_LFU_simulation.py (read bellow what that functions do) and use them in according to personal preferneces. If you want to only see results of algorithms operations on data as plots you can use FCFS_SJF_plot.ipynb or FIFO_LFU_plot.ipynb. You can also enter your data into code and create your own plots.

## Process Scheduling Algorithms
**FCFS** (First Come, First Served) is a type of scheduling algorithm used by operating systems and networks to efficiently and automatically execute queued tasks, processes and requests by the order of their arrival. An FCFS scheduling algorithm may also be referred to as a first-in, first-out (FIFO) algorithm or a first-come.

**SJF** (Shortest Job First) is an algorithm in which the process having the smallest execution time is chosen for the next execution. This scheduling method can be preemptive or non-preemptive. It significantly reduces the average waiting time for other processes awaiting execution.

### Data Generator
To create simulation data I wrote a simple function placed in process_generator.py file which creates processes. Every process has a duration time and await time to enter queue. To call the function you need three arguments: maximum process duration time, maximum process await time and the number of processes to place in the output file. The results are in the fcfs_sjf_simulation_input.txt.

### Algorithms Implementation
The simulation code is placed in fcfs_sjf_simulation.py. FCFS and SJF algorithms have separate functions. There is also a function that creates list of processes and every process is an object of Process class. To run the simulation it's necessary to input the argument as list of processes. To see algorithms performance differences there is a file FCFS_SJF_plot.ipynb which creates a plot of avarage await time of all processes in each algorithm. This is how the plot looks like:


<img src="https://github.com/kdPerkowski/CPU-Memory-Simulations/assets/82761466/29f4f06b-d86c-4aed-baa7-7241bff1142d" alt="drawing" width="400"/>

The average await time was calculated with following formula:

<img src="https://github.com/kdPerkowski/CPU-Memory-Simulations/assets/82761466/88663499-8199-4206-8956-d47ad3da65ba" alt="drawing" width="200"/>

## Page Replacement Algorithms
**FIFO** (First In First Out) is the simplest page replacement algorithm. In this algorithm, the operating system keeps track of all pages in the memory in a queue, the oldest page is in the front of the queue. When a page needs to be replaced page in the front of the queue is selected for removal.

**LFU** (Least Frequently Used) - algorithm counts how often an item is needed; those used less often are discarded first. This is similar to LRU, except that how many times a block was accessed is stored instead of how recently. While running an access sequence, the block which was used the fewest times will be removed from the cache.

### Data Generator
To create simulation data I wrote a simple function placed in pages_generator.py. The function require two arguments: number of pages and maximum number of page. Page is just a number that represents index of page. Generated data is placed in fifo_lfu_simulation_input.txt.

### Algorithms Implementation
The simulation code is palced in FIFO_LFU_simulation.py. FIFO and LFU algorithms have separate functions. To run the simulation it's necessary to input the arguments as list of pages and number of frames. To see algorithms performance differences there is a file FIFO_LFU_plot.ipynb which creates a plot of page replaces ratio of all input pages. This is how the plot looks like: 


<img src="https://github.com/kdPerkowski/CPU-Memory-Simulations/assets/82761466/a7edc4db-d519-4def-9c45-53fb99c1d326" alt="drawing" width="400"/>



