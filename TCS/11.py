t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l=[]
    for i in range(n):
        a=list(map(int,input().split()))
        l.append(a)
    c=0
    for i in l:
        for j in i:
            if j%2!=0:
                c+=1
    if c%2==0:
        print("YES")
    else:
        print("NO")    