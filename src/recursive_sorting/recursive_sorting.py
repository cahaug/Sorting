arrA = [2,3,4,6,9,10,16]
arrB = [1,7,9,11,14,16,17,18]
arrD = [3,4]
arrE = [1]
arrF = [1,2,3,4,5,6]
# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(0, elements):
        if arrA == [] and len(arrB) > 0:
            merged_arr.pop()
            print('arrA is empty')
            merged_arr.insert(i, arrB[0])
            arrB.pop(0)
        elif arrB == [] and len(arrA) > 0:
            merged_arr.pop()
            print('arrB is empty')
            merged_arr.insert(i, arrA[0])
            arrA.pop(0)
        elif arrA[0] <= arrB[0]:
            merged_arr.pop()
            print('A<B')
            merged_arr.insert(i, arrA[0])
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

# this function takes any array of numbers and 
# divides it in half, into two arrays. if odd number of values the +1 goes to the front array
def splitArr( arrA ):
    if len( arrA ) == 1:
        return [arrA]
    elif len(arrA) == 2:
        newArray1= [arrA[0]]
        newArray2= [arrA[1]]
        return [newArray1, newArray2]
    elif len(arrA) % 2 != 0:
        midpoint_idx = len(arrA) // 2 + 1
        newArray1 = arrA[:int(midpoint_idx)]
        newArray2 = arrA[int(midpoint_idx):]
        return [newArray1, newArray2]
    elif len(arrA) % 2 == 0:
        midpoint_idx = len(arrA) // 2
        newArray1 = arrA[:int(midpoint_idx)]
        newArray2 = arrA[int(midpoint_idx):]
        return [newArray1, newArray2]



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # while we have arrays that are greater than 1 in length, split the array
    #  into two subarrays, each half the length of the original
    splitOnce = splitArr( arr )
    arraysShortEnough = False
    shortEnoughArrays = [] 
    while arraysShortEnough != True
        for array in splitOnce:
            if len( array ) == 1:
                shortEnoughArrays.append(array)
            else:
                return splitArr( array )
             

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
