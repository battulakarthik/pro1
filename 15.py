nm=int(input())
lst=[int(x) for x in input().split()]
c=sorted(lst)
for i in range(nm-1,-1,-1):
    print(c[i])
