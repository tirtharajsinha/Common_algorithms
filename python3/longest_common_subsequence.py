def lcs(a,b):
    m=len(a)
    n=len(b)
    tab=[[None]*(n+1) for _ in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                tab[i][j]=0
            elif a[i-1]==b[j-1]:
                tab[i][j]=tab[i-1][j-1]+1
            else:
                tab[i][j]=max(tab[i-1][j],tab[i][j-1])
    
    i,j=m,n
    lcs=""
    
    while i>0 and j>0:
        if tab[i-1][j]==tab[i][j-1]:
            if a[i-1]==b[j-1]:
                lcs=a[i-1]+lcs
                print(tab[i-1][j],tab[i][j-1],a[i-1])
                i-=1
                j-=1
            else:
                i-=1
        elif tab[i-1][j]>tab[i][j-1]:
            i-=1
        else:
            j-=1
    
    return [tab[m][n],lcs]
a = "AGGTAB"
b = "GXTXAYB"
# a = "ACADB"
# b = "CBDA"
print("lcs of '",a,"' and '",b,"' :", lcs(a,b))

# time complexity for longest common subsequence
