from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
import time
import numpy as np

sizes = [5,10,20]
times = []

#measure time for sorting algorithm (time diff)
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

#generate random array and masure time for selection sort
for size in sizes:
    arr = np.random.randint(0,1000,size)
    print(arr)
    time_taken = measure_time(selection_sort,arr)
    times.append(time_taken)

print(times)