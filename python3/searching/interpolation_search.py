def InterpolationSearch(arr, lo, hi, x):
 
    
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
 
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *(x - arr[lo]))
 
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            return interpolationSearch(arr, pos + 1,hi, x)
        else:
            return interpolationSearch(arr, lo,
                                       pos - 1, x)
    return False
arr=[1,2,3,4,5]    
InterpolationSearch(arr,0,len(arr)-1,5)
