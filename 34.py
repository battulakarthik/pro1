a,b=input().split()
a=int(a)
b=int(b)
rows=[]
s='R'
y='G'
for i in range(0,a):
	c=input()
	rows.append(c)
k=[]
sum=0
for i in range(0,a):
	t=rows[i]
	for j in range(0,b):
		k.append(t[j])
	for j in range(0,b-1):
		if k[j]==k[j+1]:
			if k[j]==s:
				k[j]=y
				sum=sum+5
			else:
				k[j]=s
				sum=sum+3
	k=[]
print (sum)
