#Minimize the sum:
n,k=map(int,input().split())
a=list(map(int,input().split()))
for i in range(k):
    f=max(a)
    fi=a.index(f)
    fac=f//2
    a[fi]=fac
print(sum(a))