def strassen(a,b):
    
    m1= (a[0][0] + a[1][1])*(b[0][0]+b[1][1])
    m2= (a[1][0]+a[1][1])*b[0][0]
    m3= a[0][0]*(b[0][1]-b[1][1])
    m4= a[1][1]*(b[1][0]-b[0][0])
    m5= (a[0][0]+a[0][1])*b[1][1]
    m6= (a[1][0]-a[0][0])*(b[0][0]+b[0][1])
    m7= (a[0][1]-a[1][1])*(b[1][0]+b[1][1])
    
    c=[[],[]]
    c[0].append(m1+m4-m5+m7)
    c[0].append(m3+m5)
    c[1].append(m2+m4)
    c[1].append(m1-m2+m3+m6)
    
    return c

    
if __name__=="__main__":
    a=[[int(x) for x in input("Enter values for first matrix of row "+str(i+1)+": ").split()] for i in range(2)]
    b=[[int(x) for x in input("Enter values for second matrix of row "+str(i+1)+": ").split()] for i in range(2)]
    
    print(strassen(a,b))
