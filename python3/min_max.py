def minmax(arr,k):
    arr.sort()
    resultmin=max(arr)
    for i in range((n - k) + 1):
        Diff = arr[i + k - 1] - arr[i]
        resultmin = min(resultmin, Diff)
    return resultmin

print(minmax([5,3,1,2,3,4,5],3))
