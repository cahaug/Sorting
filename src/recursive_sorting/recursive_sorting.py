# arrA = [2,3,4,6,9,10,16]
# arrB = [1,5,7,8,10,11,12]
# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(0, elements):
        if arrA == [] and len(arrB) > 0:
            merged_arr.pop()
            merged_arr.insert(i, arrB[0])
            arrB.pop(0)
        elif arrB == [] and len(arrA) > 0:
            merged_arr.pop()
            merged_arr.insert(i, arrA[0])
            arrA.pop(0)
        elif arrA[0] <= arrB[0]:
            merged_arr.insert(i, arrA[0])
            print('A<B')
            merged_arr.pop()
            arrA.pop(0)
        elif arrA[0] > arrB[0]:
            merged_arr.pop()
            print('A>B')
            merged_arr.insert(i, arrB[0])
            arrB.pop(0)
        elif len(arrA) == 0 and len(arrB) == 0:
            print("""We're done here.""")
        else:
            print("""Ran Out of Conditions. Error?""")


    # print(merged_arr)
    return merged_arr

# print(merge(arrA,arrB))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


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
