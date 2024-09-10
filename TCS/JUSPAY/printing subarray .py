n=int(input())
l=list(map(int,input().split()))[:n]
for i in range(n):
    for j in range(i,n):
        for k in range(i,j+1):
            print(l[k],end=' ')
        print()