n=int(input())
lst=[int(x) for x in input().split()]
c=sorted(lst)
candy1=[]
candy=n
for i in range(0,n-1):
   for j in range(i+1,n):
       if c[i]==c[j]:
           break
       elif c[i]<c[j]:
           candy+=1
print(candy)
