n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n-1):
    r=abs(a[i]-a[i+1])
    s+=r
print(s)