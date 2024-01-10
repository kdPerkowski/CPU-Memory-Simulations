import numpy
from pages_generator import generate_pages

#fifo algorithm
def fifo(data,frames):
    data_len = len(data)
    timer = 0
    page_replaces = 0
    memory = []
    page_time_dict = {}

    #loop going through all pages data elements
    while timer < data_len:
        #add pages to each frame and increment of page replaces
        if len(memory) < frames:
            if data[timer] not in memory:
                memory.append(data[timer])
                page_replaces += 1
                page_time_dict[data[timer]] = timer
        #if frames are full start replacing them with fifo algorithm
        elif len(memory) == frames:
            #if element is not in frame find element with the least time replace and replace it with new page
            if data[timer] not in memory:
                min_time = min(list(page_time_dict.values()))
                page_to_replace = list(page_time_dict.keys())[list(page_time_dict.values()).index(min_time)]

                memory[memory.index(page_to_replace)] = data[timer]

                page_time_dict[data[timer]] = timer
                del page_time_dict[page_to_replace]

                page_replaces += 1

        #increment page replaces time
        timer += 1

    #function outputs time of page replacements time and number of page replacements
    return timer,page_replaces

#lfu algorithm
def lfu(data,frames):
    data_len = len(data)
    timer = 0
    page_replaces = 0
    memory = []
    page_time_dict = {}
    page_frequency_dict = {}

    #loop going through all pages data elements
    while timer < data_len:
        #add pages to each frame and increment of page replaces
        if len(memory) < frames:
            if data[timer] not in memory:
                memory.append(data[timer])
                page_replaces += 1
                page_time_dict[data[timer]] = timer
                page_frequency_dict[data[timer]] = 1
            #if page is in memory increment frequency
            elif data[timer] in memory:
                page_frequency_dict[data[timer]] += 1
        #if frames are full start replacing them with lfu algorithm
        elif len(memory) == frames:
            if data[timer] not in memory:
                min_freq = min(page_frequency_dict.values())
                pages_with_min_freq = []
                for i in range(len(memory)):
                    if page_frequency_dict[memory[i]] == min_freq:
                        pages_with_min_freq.append(memory[i])

                #replace page which has the least frequency
                if len(pages_with_min_freq) == 1:
                    page_to_replace = pages_with_min_freq[0]

                    memory[memory.index(page_to_replace)] = data[timer]

                    del page_frequency_dict[page_to_replace]

                    page_replaces += 1
                    page_frequency_dict[data[timer]] = 1
                    page_time_dict[data[timer]] = timer
                #if there is more than one page with the same frequency compare frame entry time and replace the page
                elif len(pages_with_min_freq) > 1:
                    entry_time_table = []
                    for i in range(len(pages_with_min_freq)):
                        entry_time_table.append(page_time_dict[pages_with_min_freq[i]])

                    min_time = min(entry_time_table)

                    page_to_replace = list(page_time_dict.keys())[list(page_time_dict.values()).index(min_time)]

                    memory[memory.index(page_to_replace)] = data[timer]

                    del page_frequency_dict[page_to_replace]

                    page_replaces += 1
                    page_frequency_dict[data[timer]] = 1
                    page_time_dict[data[timer]] = timer
            elif data[timer] in memory:
                #if page in memory increment frequency 
                page_frequency_dict[data[timer]] += 1

        #increment page replaces time
        timer += 1

    #function outputs page replaces time and number of page replacements
    return timer,page_replaces

#TEST CODE

# generate_pages(10000,200)

# pages_data = numpy.genfromtxt('fifo_lfu_simulation_input.txt')

# timer_fifo,page_replaces_fifo = fifo(pages_data,4)
# timer_lfu,page_replaces_lfu = lfu(pages_data,140)

# print("FIFO")
# print(timer_fifo)
# print(f"Page replaces: {page_replaces_fifo}")
# print("LFU")
# # print(timer_lfu)
# print(f"Page replaces: {page_replaces_lfu}")