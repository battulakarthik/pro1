ip=input()
move=0
x=0
y=0
t=0
for z in range(len(ip)):
        if ip[0]=="G" and move==0:
            y+=1
            d="up"
            move+=1
        elif ip[0]=="R" and move==0:
            d="frwd"
            move+=1
            flag=0
            t+=1
        elif ip[0]=="L" and move==0:
            d="bck"
            move+=1
            flag=1
            t+=1
        elif ip[z]=="G" and d=="up" and t==0:
            y+=1
            d="up"
            move+=1
        elif ip[z]=="R" and d=="up":
            flag=0
            d="frwd"
            t+=1
        elif ip[z]=="R" and d=="frwd":
            flag=0
            d="dwn"
            t+=1
        elif ip[z]=="R" and d=="dwn":
                flag=0
                d="bck"
                t+=1
        elif ip[z]=="R" and d=="bck":
                flag=0
                d="up"
                t+=1
        elif ip[z]=="L" and d=="up":
                flag=1
                d="bck"
                t+=1
        elif ip[z]=="L" and d=="bck":
                flag=1
                d="dwn"
                t+=1
        elif ip[z]=="L" and d=="dwn":
                flag=1
                d="frwd"
                t+=1
        elif ip[z]=="L" and d=="frwd":
                flag=1
                d="up"
                t+=1
        elif ip[z]=="G" and flag==0 and d=="frwd":
                x+=1
        elif ip[z]=="G" and flag==0 and d=="dwn":
                y-=1
        elif ip[z]=="G" and flag==0 and d=="bck":
                x-=1
        elif ip[z]=="G" and flag==0 and d=="up":
                y+=1
        elif ip[z]=="G" and flag==1 and d=="bck":
                x=x-1
        elif ip[z]=="G" and flag==1  and d=="dwn":
                y-=1
        elif ip[z]=="G" and flag==1 and d=="frwd":
                x+=1
        elif ip[z]=="G" and flag==1 and d=="up":
                y+=1
if(x==y==0):
    print("yes")
else:
    print("no")
