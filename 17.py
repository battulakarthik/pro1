import sys
n,m=input().split()
n,m=int(n),int(m)
lst=[int(x) for x in input().split()]
for i in range(0,n-1):
    for j in range(i+1,n):
        if m==lst[i]+lst[j]:
            print("yes")
            sys.exit()
print("no")
