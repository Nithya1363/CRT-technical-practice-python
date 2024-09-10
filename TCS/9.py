t=int(input())
for _ in range(t):
    n=int(input())
    q=list(map(int,input().split()))[:n]
    q.sort()
    for i in range(n-2):
        if q[i+2]-q[i]<=2 and (q[i]!= q[i+1] and q[i+1]!=q[i+2]):
            print("YES")
            break
    else:
        print("NO")