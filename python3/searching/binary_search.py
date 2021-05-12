def binarysearch(arr,s,e,elm):
    mid = s + (e - s) // 2
    midelm=arr[mid]
    
    if e>=s:
        if elm==midelm:
            return mid
        elif elm<midelm:
            return binarysearch(arr,0,mid-1,elm)
        else:
            return binarysearch(arr,mid+1,e,elm)
    else:
        return False
# must be sorted arr
arr=[1,2,3,4,5]    
binarysearch(arr,0,len(arr)-1,3)
    
