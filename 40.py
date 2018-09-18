d=['d','h','o','n','i']
n=input()
n=list(n)
c=0
for i in range(0,len(n)):
    if n[i] in d:
        c+=1
    else:c=0
if c==len(d):print("yes")
else:print("no")
