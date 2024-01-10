import random

def process_generator(max_proc_duration,max_proc_await_time,number_of_processes):
    with open('fcfs_sjf_simulation_input.txt','w') as file:
        for i in range(number_of_processes):
            # process_index;exec_duration;exec_await
            line = f"{i};{random.randint(1,max_proc_duration)};{random.randint(0,max_proc_await_time)}"
            file.write(line)
            file.write('\n')

# random.randint(1,max_proc_duration)
# random.randint(0,max_proc_await_time)