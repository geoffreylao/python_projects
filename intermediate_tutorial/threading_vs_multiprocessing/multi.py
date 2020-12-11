from multiprocessing import Process
import os

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()

# create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

# start each process
for p in processes:
    p.start()

# join 
for p in processes:
    p.join()

print('end main')

from threading import Thread

threads = []
num_threads = 10

for i in num(threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# start
for t in threads:
    t.start()

# join
for t in threads:
    t.join()

print('end main')