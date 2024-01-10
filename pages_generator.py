import random

def generate_pages(pages_nr,max_page_nr):
    with open('fifo_lfu_simulation_input.txt','w') as file:
        for i in range(pages_nr):
            page = str(random.randint(0,max_page_nr))
            file.write(page)
            file.write('\n')