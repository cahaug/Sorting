arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# Selection Sort: (imagine you are holding n cards in your hand...)
# 1. Select the smallest card and move it to the far left
# 2. Select the next smallest card and move it to the left so that it is to the immediate right of the previous card
# 3. Repeat the previous step until all the cards in the right place

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # cur_index = i
        # smallest_index = cur_index
        # TO-DO: find next smallest element
        # 1. Select the smallest card and move it to the far left
        absolute_minimum = min(arr)
        arr.remove(absolute_minimum)
        arr.insert(0, absolute_minimum)
        # 2. Select the next smallest card and move it to the left so that it is to the immediate right of the previous card, 3. Repeat
        # (hint, can do in 3 loc) 
        for j in range(1, len(arr)):
            local_minimum = min(arr[j:])
        # TO-DO: swap
            arr.remove(local_minimum)
            arr.insert(j, local_minimum)
            j+=1


    return arr

print(selection_sort(arr1))


# Bubble Sort: (imagine you are holding n cards in your hand...)
# 1. Compare a pair of elements 
#       - If the right hand side is less than the left hand side, swap the values
#       - Else, do nothing
# 2. Iterate through the array, comparing other pairs of adjacent elements 
#       (* the last pair of compared values will be the arrayLength-2 & arraylength-1 as we are using zero-based indexing)
# 3. If one or more swaps was performed on a given pass, repeat the pass/process (reset swap boolean/counter here)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    arrLen = len( arr )
    for i in range(arrLen):
        for j in range(0, arrLen-i-1):
#           (STEP #1,2,3)
            if arr[j]>arr[j+1]:
                comparative_maximum = arr[j]
                arr.remove(comparative_maximum)
                arr.insert(j+1, comparative_maximum)
    return arr

# print(bubble_sort(arr1))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

# print(count_sort(arr1))