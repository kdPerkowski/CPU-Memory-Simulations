import numpy
from process_generator import process_generator

#class for handling process objects
class Process:
    def __init__(self,id,exec_duration,exec_await):
        self.id = id
        self.exec_duration = exec_duration
        self.exec_await = exec_await
        self.finished = False
        self.time_to_start = 0

#creating object for each process
def create_processes(input_table):
    output_table = []
    for i in range(len(input_table)):
        proc = Process(input_table[i,0],input_table[i,1],input_table[i,2])
        output_table.append(proc)
    return output_table

#fcfs algorithm
def fcfs(proc_table):
    #creating timer, queue for processes and list with awaiting time value of every process
    timer = 0
    queue = []
    await_table = []


    #while loop will continue until queue is not empty or all of processes won't have finished attribute equal to true
    while not all([x.finished for x in proc_table]) or queue != []:
        for process in proc_table:
            if process.exec_await == timer:
                queue.append(process)
                process.finished = True

        if queue != []:
            #sort queue by process await time
            queue.sort(key=lambda x:x.exec_await)

            #if statement with loop comparing await time of every process if its equal checking id of each process
            if len(queue) > 1:
                for i in range(len(queue)-1):
                    if queue[i].exec_await == queue[i+1].exec_await:
                        if queue[i].id > queue[i+1].id:
                            queue[i],queue[i+1] = queue[i+1],queue[i]
    
            #checking duration of execution of first process from queue if its equal 0 add to list time to start of execution and delete item from queue else decrement execution duration and increment time to start for other processes in the queue
            if queue[0].exec_duration == 0:
                await_table.append(queue[0].time_to_start)
                del queue[0]
            else:
                queue[0].exec_duration -= 1
                for i in queue[1:]:
                        i.time_to_start += 1
        
        #increment time of processes completion
        timer += 1

    #calculate the avarage
    avg_await = 0
    for i in await_table:
        avg_await+=int(i)
    avg_await/=len(await_table)

    #function output processes completion time and average of process await time
    return avg_await

#sjf algorithm
def sjf(proc_table):
    #creating timer, queue for processes and list with awaiting time value of every process
    timer = 0
    queue = []
    await_table = []

    #while loop will continue until queue is not empty or all of processes won't have finished attribute equal to true
    while not all([x.finished for x in proc_table]) or queue != []:
        #loop used fot checking if process can join the queue
        for process in proc_table:
            if process.exec_await == timer:
                queue.append(process)
                process.finished = True

        if queue != []:
            #sort queue by duration of process execution
            queue.sort(key=lambda x:x.exec_duration)

            #if statement with loop comparing exec duration of every process if its equal checking await time
            if len(queue) > 1:
                for i in range(len(queue)-1):
                    if queue[i].exec_duration == queue[i+1].exec_duration:
                        if queue[i].exec_await > queue[i+1].exec_await:
                            queue[i],queue[i+1] = queue[i+1],queue[i]

            #checking duration of execution of first process from queue if its equal 0 add to list time to start of execution and delete item from queue else decrement execution duration and increment time to start for other processes in the queue
            if queue[0].exec_duration == 0:
                await_table.append(queue[0].time_to_start)
                del queue[0]
            else:
                queue[0].exec_duration -= 1
                for i in queue[1:]:
                    i.time_to_start += 1

        #increment time of processes completion
        timer += 1

    #calculate the avarage
    avg_await = 0
    for i in await_table:
        avg_await+=int(i)
    avg_await/=len(await_table)

    #function output processes completion time and average of process await time
    return avg_await


#TEST CODE


# process_generator(10,0,50)

# process_data = numpy.genfromtxt('fcfs_sjf_simulation_input.txt',delimiter=';')

# # variables with processes completion time and average of process await time
# fcfs_avg = fcfs(create_processes(process_data))
# sjf_avg = sjf(create_processes(process_data))

# print("FCFS")
# # print(f"Czas: {fcfs_time}")
# print(f"Średni czas oczekiwania: {fcfs_avg}")

# print("SJF")
# # print(f"Czas: {sjf_time}")
# print(f"Średni czas oczekiwania: {sjf_avg}")
