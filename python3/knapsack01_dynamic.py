def KnapsackDynamic(w,wt,val,n):
    tab=[[0 for _ in range(w+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                tab[i][j]=0
            elif wt[i-1]<=j:
                tab[i][j] = max(val[i-1] + tab[i-1][j-wt[i-1]],  tab[i-1][j])
            else:
                tab[i][j]=tab[i-1][j]
    return tab[n][w]

#..............................................................................

w=50                                             
val = [60, 100, 120]
wt = [10, 20, 30]
n=len(wt)
KnapsackDynamic(w,wt,val,n)       
