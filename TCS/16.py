n=int(input())
l=list(map(int,input().split()))[:n]
c=0
for i in range(1,n-1):
    if l[i-1]==1 and l[i]==0 and l[i+1]==1:
        c+=1
        l[i+1]=0
print(c)