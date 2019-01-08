k= int(input())
n=[]
for i in range(k):
    n.extend(input().split())
n=[int(x) for x in n]
n.sort()
for i in n: print(i,end="" )
