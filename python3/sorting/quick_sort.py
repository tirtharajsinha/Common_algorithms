def partition(arr,low,high):
    i = ( low-1 )
    pivot = arr[high] # pivot element
    for j in range(low , high):
        # If current element is smaller
        if arr[j] <= pivot:
            # increment
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
# sort
def quickSort(arr,low,high):
    
    if low < high:
        # index
        pi = partition(arr,low,high)
        # sort the partitions
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return arr

if __name__=="__main__":
    arr=[9,6,3,6,2,7]
    list=quickSort(arr,0,len(arr)-1)
    print(list)
