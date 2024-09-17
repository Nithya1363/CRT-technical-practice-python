n,r=map(int,input().split())
x=[int(i) for i in input().split(" ",n-1)]
res=[]
for i in range(r):
    st,en=map(int,input().split())
    c=0
    for j in x:
        if j>=st and j<=en:
            c+=1
    res.append(c)
print(*res)