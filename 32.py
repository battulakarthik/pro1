n,m=map(int,input().split())
mx=[]
for x in range(0,n):
    row=[int(x) for x in input().split()]
    mx.append(sorted(row))
clmx=[]
mx=tuple(mx)
for i in range(0,m):
    cl=[]
    for j in range(0,n):
        cl.append(mx[j][i])
    clmx.append(sorted(cl))
for i in range(0,n):
    for j in range(0,m):
        if j<m-1:k=' '
        else:k=''
        print(clmx[j][i],end=k)
    print()

