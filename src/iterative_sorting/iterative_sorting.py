# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        absolute_minimum = min(arr)
        arr.remove(absolute_minimum)
        arr.insert(0, absolute_minimum)
        # (hint, can do in 3 loc) 
        for j in range(1, len(arr)):
            local_minimum = min(arr[j:])
            arr.remove(local_minimum)
            arr.insert(j, local_minimum)
            j+=1

        # TO-DO: swap

    return arr

# print(selection_sort(arr1))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr