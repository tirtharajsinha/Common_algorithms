def insertionSort(arr):
  
    
    for i in range(1, len(arr)):
  
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr
      
arr = [int(x) for x in input("Enter values sepereted by space:").split()]
ar=insertionSort(arr)
for i in ar:
    print(i,end=" ")
