n=input()
n=list(n)
for i in range(0,len(n)):
    if i%2!=0:
        print(n[i-1]*int(n[i]),end='')
