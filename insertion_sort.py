def insertion_sort(arr):
    #traverse from 1 to array lenght
    for i in range(1, len(arr)):
        key = arr[i]        #element being sorted into correct position
        j = i - 1
        #compare eelement in sorted portion right to left
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  
            j -= 1
        arr[j + 1] = key