from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
import time
import numpy as np

sizes = [100, 200, 300, 400, 500, 1000]
selection_times = []
insertion_times = []
bubble_times = []

#measure time for sorting algorithm (time diff)
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

#generate random array and masure time for sorting algorithms
for size in sizes:
    arr_selection = np.random.randint(0,1000,size)
    arr_insertion = arr_selection.copy()
    arr_bubble = arr_selection.copy()
    
    selection_time = measure_time(selection_sort,arr_selection)
    selection_times.append(selection_time)

    insertion_time = measure_time(insertion_sort,arr_insertion)
    insertion_times.append(insertion_time)

    bubble_time = measure_time(bubble_sort, arr_bubble)
    bubble_times.append(bubble_time)

print('Selection times', selection_times)
print('Insertion times', insertion_times)
print('Bubble times', bubble_times)