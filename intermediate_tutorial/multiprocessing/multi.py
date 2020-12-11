from multiprocessing import Process, Value, Array, Lock, Pool
from multiprocessing import Queue
import os
import time

# array
# def add100(numbers, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         for i in range(len(numbers)):
#             with lock:
#                 numbers[i] += 1

#queue
# def square(numbers, queue):
#     for i in numbers:
#         queue.put(i*i)

# def make_negative(numbers, queue):
#     for i in numbers:
#         queue.put(-1*i)

#pool
def cube(number):
    return number * number * number

if __name__ == "__main__":

#pool
    numbers = range(10)
    pool = Pool()

    # map, apply, join, close
    result = pool.map(cube, numbers) # also async versions
    # pool.apply(cube, numbers[0])

    pool.close()
    pool.join() 

    print(result)

    # queue
    # numbers = range(1, 6)
    # q = Queue()

    # p1 = Process(target=square, args=(numbers, q))
    # p2 = Process(target=make_negative, args=(numbers, q))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # while not q.empty():
    #     print(q.get())

    # array
    # lock = Lock()
    # shared_array = Array('d', [0.0, 100.0, 200.0])
    # print('Array at beginning is', shared_array[:])

    # p1 = Process(target=add100, args=(shared_array,lock))
    # p2 = Process(target=add100, args=(shared_array,lock))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # print('array at end is', shared_array[:])