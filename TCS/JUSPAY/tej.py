n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
for i in range(1,n,2):
    print(a[i],end=' ')
for i in range(n-2,-1,-2):
    print(a[i],end=' ')