def LinearSearch(arr,elem):
    for i in range(len(arr)):
        if arr[i] == elem:
            return i
    return False
arr=[1,2,3,4,5,6]
LinearSearch(arr,2)
