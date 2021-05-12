def FractionalKnapsack(w,wt,val,n):
    frac=[val[i]/wt[i] for i in range(n)]
    branch=sorted(zip(frac,wt),reverse=True)
    cost=0
    for dual in branch:
        if w==0:
            break
        elif dual[1]<=w:
            w-=dual[1]
            cost+=dual[0]*dual[1]
        else:
            cost+=dual[0]*w
            w=0
    return cost
                
#..................................................    
w=50                                             
val = [60, 100, 120]
wt = [10, 20, 30]
n=len(wt)
FractionalKnapsack(w,wt,val,n)           
