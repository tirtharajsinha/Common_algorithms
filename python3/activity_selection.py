def activityselection(start,end,issorted=False):
    activity=zip(start,end)
    if issorted==False:
        activity=sorted(activity,key=lambda x :x[1])
    table=[]
    i=0
    table.append(activity[i])
    
    for j in range(1,len(activity)):
        if activity[j][0]>=activity[i][1]:
            i=j
            table.append(activity[i])
    return table
    
#..................................................

s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 5 , 7 , 9 , 9]
activityselection(s,f)
