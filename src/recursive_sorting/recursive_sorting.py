arrA = [2,3,4,6,9,10,16]
arrB = [1,7,9,11,14,16,17,18]
arrD = [3,4]
arrE = [1]
arrF = [1,2,3,4,5,6]
# TO-DO: complete the helper function below to merge 2 sorted arrays
# given two sorted arrays, return a new combined array 
def merge( arrA, arrB ):
    merged_arr = []
    i = 0
    j = 0
    while i < len(arrA) and j < len(arrB):
        # compare the two values, choose the smaller one
        if (arrA[i] <= arrB[j]):
            merged_arr.append(arrA[i])
            i+=1
        else:
            merged_arr.append(arrB[j])
            j+=1
    return merged_arr + arrA[i:] + arrB[j:]

# print(merge(arrA,arrB))



# TO-DO: implement the Merge Sort function below USING RECURSION
# the job of this function is to return a sorted array
def merge_sort( arr ):
    # TO-DO
    # base case (Easiest case)
    if len(arr) <= 1:
        return arr

    # divide the arrays
    half = len(arr) // 2
    left = merge_sort(arr[0:half])
    right = merge_sort(arr[half:])

        

    ##### SORTING #####
    # somehow, the arrays get sorted, because 
    # we are taking arrays of length 1,
    # which means it's already sorted *greencheckmark*
    return merge(left, right)
    # merging sorted arrays


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
