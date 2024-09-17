t=int(input())
for _ in range(t):
    s=input().lower()
    w,n=[],[]
    x=s.split()
    for i in x:
        if i.isdigit():
            n.append(i)
        else:
            w.append(i)
    w.sort()
    n.sort()
    print(w,n)
    for i,j in zip(w,n):
        print(i,j,end=" ")