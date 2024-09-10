t=int(input())
for _ in range(t):
    n=int(input())
    l=[]
    for i in range(n):
        l1=list(map(int,input().split()))
        l.append(l1)
    found=False
    for i in range(n):
        for j in range(n):
            if l[i][j] == 0:
                found =0
                break
            if i>0 and l[i][j] == l[i-1][j]:
                found=True
                break
            if j>0 and l[i][j]==l[i][j-1]:
                found=True
                break
    if found:
        print("YES")
    else:
        print("NO")