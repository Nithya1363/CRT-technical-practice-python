t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))[:n]
    c=0
    for i in range(x):
        if i not in a:
            c+=1
    if x in a:
        c+=1
    print(c)