c,d=input().split()
c=int(c)
d=int(d)
t=[]
temp=c
while c<0
rem=c%10
    c=c//10
    count=count+1
for r in range(count):
    u=temp%10
    temp=temp//10
    t.append(u)

for j in range(d):
    t.pop()


for i in range(len(t)):
    for m in range(i+1,len(t)):
        if(t[i]>t[m]):
            (t[i],t[m])=(t[m],t[i])
       
for i in range(len(t)):
        print(t[i],end="")
	
	
