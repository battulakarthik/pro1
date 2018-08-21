n,m=map(int,input().split())
g=[]
lst=[int(x) for x in input().split()]
for i in range(0,m):
    row=[int(x) for x in input().split()]
    g.append(row)
for i in range(0,m):
    a,b=g[i][0],g[i][1]
    c=[]
    for j in range(a-1,b):
        c.append(lst[j])
    print(min(c))
