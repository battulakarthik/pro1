n,m=map(int,input().split())
lst=[int(x) for x in input().split()]
lm=[]
for i in range(0,m):
    row=[int(x) for x in input().split()]
    lm.append(row)
for i in range(0,m):
    a=lst[lm[i][0]-1]
    b=lst[lm[i][1]-1]
    if a>b:
        max=a
    else:
        max=b
    for j in range(1,max+1):
       if(a%j==0) and (b%j==0):
           c=j
    print(c)
