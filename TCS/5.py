t=int(input())
for _ in range(t):
    m=0
    n=int(input())
    l=list(map(int,input().split()))[:n]
    for i in l:
        if l.count(i)>1:
            m=max(l)*l.count(i)
        else:
           m=max(l)
    print(m)
"""for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    m=l[0]
    c=0
    for i in range(1,n):
        if l[i-1]==l[i]:
            c=c+l[i]
        else:
            m=max(m,c)
            c=l[i]
    m=max(m,c)
    print(m)"""