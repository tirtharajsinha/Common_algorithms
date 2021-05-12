def bestfit(box,w):
    # counting num of usedbins ini 0
    used=0
    bin=[]
    n=len(box)
    
    for i in range(n):
        min=w+1
        bestbin=0
        for j in range(used):
            if bin[j]>=box[i] and bin[j]-box[i]<min:
                bestbin=j
                min=bin[j]-box[i]
        if min==w+1:
            bin.append(0)
            
            bin[used]=w-box[i]
            used+=1
        else:
            bin[bestbin]-=box[i]
    return used

box=[ 2, 5, 4, 7, 1, 3, 8 ]
capacity=10
print("Required bins to fit elements :",bestfit(box,capacity))
