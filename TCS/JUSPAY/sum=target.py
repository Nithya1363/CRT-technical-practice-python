n,target=map(int,input().split())
a=list(map(int,input().split()))[:n]
found=False
for i in range(0,n-1):
    for j in range(i+1,n):
        if a[i]+a[j]==target:
            found=True
            pair=(i,j)
if found==True:
        print(*pair)
else:
    print('-1')