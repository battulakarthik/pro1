n=int(input())
m=input().split()
sum=0
l=[]
for i in range(0,len(m)-1):
	if int(m[i+1])>=int(m[i]):
		sum=sum+1
	else:
		l.append(sum)
		sum=0
print(max(l)+1)
