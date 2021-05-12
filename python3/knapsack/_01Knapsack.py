def knapsack(w,wt,val,n):
    
    if n==0 or w==0:
        return 0
    elif wt[n-1]>w:
        return knapsack(w,wt,val,n-1)
    else:
        return max(val[n-1]+knapsack(w-wt[n-1],wt,val,n-1),knapsack(w,wt,val,n-1))

w=50
val = [60, 100, 120]
wt = [10, 20, 30]
n=len(wt)

print(knapsack(w,wt,val,n))
            
