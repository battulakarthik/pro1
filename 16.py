n=int(input())
lst=[int(x) for x in input().split()]
candy=n
for i in range(0,n-1):
   for j in range(i+1,n):
       if lst[i]==lst[j]:
           break
       elif lst[i]<lst[j]:
           candy+=1
print(candy)
