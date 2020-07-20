# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    test = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, test - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        test -= 1




    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    if len(arr) == 0:
        return []
    maximum = max(arr) + 1
    count_arr = [0] * (maximum)
    # sort_arr = []
    for i in arr:
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            count_arr[i] += 1
    # for i, v in enumerate(count_arr):
    #     sort_arr.extend([i] * (v))
    index = 0
    for i in range(len(count_arr)):
        for _ in range(count_arr[i]):
            arr[index] = i
            index += 1
    return arr
    # return sort_arr

