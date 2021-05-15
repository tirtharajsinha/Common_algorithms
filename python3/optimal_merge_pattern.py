def Optimalmerge(arr):
    arr.sort()
    count=0
    while len(arr)>1:
        a=min(arr)
        arr.remove(a)
        b=min(arr)
        arr.remove(b)
        count+=(a+b)
        arr.append(a+b)
        print(arr)
    return count
        
Optimalmerge([2, 3, 4, 5, 6, 7])
#by tirtharaj Sinha
